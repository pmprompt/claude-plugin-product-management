---
description: "Fast, rigorous validation before building."
argument-hint: "[product or feature idea]"
---

# /validate-idea — Idea Validation Workflow

Fast, rigorous validation before building.

## What It Does

Chains JTBD discovery, assumption testing, and experiment design to validate whether an idea is worth pursuing.

## When to Use

- New product or feature idea (pre-build)
- Need to test market demand quickly
- Want structured validation approach
- Avoiding "build it and they will come" trap

## Workflow

1. **Jobs to Be Done** — Uncover the real job customers are hiring a solution for (uses `jobs-to-be-done` skill)

2. **Identify Risky Assumptions** — Map Value, Usability, Viability, Feasibility risks (uses `trustworthy-experiments` skill)

3. **Design Pretotype Experiments** — Fast, cheap tests with "skin in the game" (uses `trustworthy-experiments` skill)

4. **PMF Checkpoint** — Plan how you'll measure product-market fit (uses `pmf-survey` skill)

## Usage

```
/validate-idea [product or feature idea]
```

**Example:**
```
/validate-idea Notion template marketplace for product managers
```

## Output

- JTBD analysis (When/Motivation/Outcome)
- Prioritized list of risky assumptions
- 3-5 pretotype experiments
- PMF measurement plan

## Next Steps After /validate-idea

- Run top 2-3 experiments
- If validated: `/strategy` → `/write-prd`
- If invalidated: pivot or kill
