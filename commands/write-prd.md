---
description: "Comprehensive product requirements document from feature idea to implementation plan."
argument-hint: "[feature name or description]"
---

# /write-prd — PRD Creation Workflow

Comprehensive product requirements document from feature idea to implementation plan.

## What It Does

Creates a structured PRD with problem statement, solution design, success metrics, requirements, and implementation details.

## When to Use

- Starting a new feature or product initiative
- Need to align engineering, design, and stakeholders
- Before beginning development work
- Documenting validated discovery findings

## Workflow

1. **Problem & Solution** — Articulate the problem, proposed solution, and success metrics (uses `prd-writer` skill)

2. **User Stories & Acceptance Criteria** — Break down into implementable stories (uses `prd-writer` skill)

3. **Requirements & Risks** — Define functional/technical requirements and mitigation plans (uses `prd-writer` skill)

## Usage

```
/write-prd [feature name or description]
```

**Example:**
```
/write-prd Smart notification system that reduces alert fatigue
```

## Output

- Complete PRD (8 sections)
- User stories with acceptance criteria
- Success metrics and measurement plan
- Implementation timeline and dependencies

## Next Steps After /write-prd

- Share with Product Trio for feedback
- `/plan-launch` — Create go-to-market plan
- Hand off to engineering for estimation
