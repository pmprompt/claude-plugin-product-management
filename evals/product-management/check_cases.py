#!/usr/bin/env python3
"""Check that cases.jsonl is well formed and covers every skill in skills/."""

import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FIELDS = {"id", "input", "expected_outcome"}

skills = sorted(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md"))
counts = Counter()
errors = []
seen = set()

for n, line in enumerate((HERE / "cases.jsonl").read_text(encoding="utf-8").splitlines(), 1):
    if not line.strip():
        continue
    try:
        case = json.loads(line)
    except json.JSONDecodeError as e:
        errors.append(f"line {n}: invalid JSON ({e})")
        continue
    if set(case) != FIELDS:
        errors.append(f"line {n}: fields must be exactly {sorted(FIELDS)}")
    if not all(isinstance(case.get(k), str) and case[k].strip() for k in FIELDS):
        errors.append(f"line {n}: every field must be a non-empty string")
        continue
    if case["id"] in seen:
        errors.append(f"line {n}: duplicate id {case['id']}")
    seen.add(case["id"])
    skill, sep, name = case["id"].partition(":")
    if not sep or not name.strip():
        errors.append(f"line {n}: id {case['id']} must be <skill>:<case>")
        continue
    if skill not in skills:
        errors.append(f"line {n}: id {case['id']} names unknown skill {skill}")
    counts[skill] += 1

for skill in skills:
    if counts[skill] == 0:
        errors.append(f"skill {skill} has no eval case")

for skill in skills:
    print(f"{counts[skill]:>3}  {skill}")
print(f"{sum(counts.values()):>3}  total cases, {len(skills)} skills")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
