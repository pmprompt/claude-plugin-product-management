---
description: "Structured product discovery from problem to validated experiments."
argument-hint: "[product idea or problem statement]"
---

# /discover — Product Discovery Workflow

Structured product discovery from problem to validated experiments.

## What It Does

Chains together Opportunity Solution Trees, assumption testing, and experiment design to take you from a product idea to validated next steps.

## When to Use

- New product or feature idea that needs structured discovery
- Customer problem that could be solved multiple ways
- Need to validate assumptions before building
- Want to map opportunities to outcomes

## Workflow

1. **Build an Opportunity Solution Tree** — Map desired outcome → customer opportunities → solution ideas → experiments (uses `opportunity-solution-trees` skill)

2. **Identify Assumptions** — Surface risky assumptions across Value, Usability, Viability, Feasibility (uses `trustworthy-experiments` skill)

3. **Prioritize Assumptions** — Rank by impact × risk (uses `feature-prioritization-assistant` skill)

4. **Design Experiments** — Create fast, cheap tests for top assumptions (uses `trustworthy-experiments` skill)

## Usage

```
/discover [product idea or problem statement]
```

**Example:**
```
/discover AI-powered meeting summarizer for remote teams
```

## Output

- Complete Opportunity Solution Tree
- Prioritized list of risky assumptions
- 3-5 experiment designs with success criteria
- Suggested next steps

## Next Steps After /discover

- `/strategy` — Define positioning and strategic narrative
- `/write-prd` — Document the validated solution
- Run the top experiments and return with learnings
