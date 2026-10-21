---
description: "Structured OKR creation aligned with company objectives."
argument-hint: "[team and context]"
---

# /okr-planning — OKR Planning Workflow

Structured OKR creation aligned with company objectives.

## What It Does

Creates team-level OKRs that roll up to company objectives, with clear key results and confidence levels.

## When to Use

- Quarterly or annual planning cycle
- New team forming
- OKRs feel disconnected from strategy
- Need better measurement discipline

## Workflow

1. **Company Context** — Understand top-level company OKRs (uses `okrs` skill)

2. **Team Objectives** — Define 3-5 aspirational outcomes (uses `okrs` skill)

3. **Key Results** — Quantify success with measurable KRs (uses `okrs` skill)

4. **Confidence & Dependencies** — Assess feasibility and blockers (uses `okrs` skill)

## Usage

```
/okr-planning [team and context]
```

**Example:**
```
/okr-planning Product team for B2B SaaS, company objective is expand into enterprise
```

## Output

- 3-5 team Objectives
- 3-4 Key Results per Objective (quantified)
- Confidence levels (1-10)
- Dependencies and blockers
- Weekly check-in cadence recommendation

## Next Steps After /okr-planning

- Review with team and manager
- Align with cross-functional partners
- Set up weekly progress tracking
