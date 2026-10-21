# PMPrompt Commands

Commands are workflow orchestrators that chain multiple skills together into end-to-end PM processes.

## Available Commands

| Command | Purpose | Skills Used |
|---------|---------|-------------|
| `/discover` | Product discovery (OST → experiments) | opportunity-solution-trees, trustworthy-experiments, feature-prioritization-assistant |
| `/strategy` | Product strategy (positioning → narrative) | positioning-canvas, seven-powers, strategic-narrative |
| `/write-prd` | PRD creation | prd-writer |
| `/plan-launch` | Launch planning (positioning → metrics) | positioning-canvas, pmf-survey, okrs |
| `/validate-idea` | Idea validation (JTBD → experiments) | jobs-to-be-done, trustworthy-experiments, pmf-survey |
| `/growth` | Growth strategy (loops → retention) | growth-loops, hooked-model, product-led-growth, hierarchy-of-engagement |
| `/pricing` | Pricing strategy (value metric → validation) | monetizing-innovation |
| `/competitive-intel` | Competitive analysis (landscape → differentiation) | competitive-analysis-framework, seven-powers, positioning-canvas |
| `/okr-planning` | OKR creation | okrs |

## How Commands Work

1. **User invokes command** with `/command-name [context]`
2. **Command chains skills** in a specific sequence
3. **Output suggests next steps** (other commands to run)

## Design Pattern

Each command file includes:
- **What It Does** — One-line summary
- **When to Use** — Specific use cases
- **Workflow** — Step-by-step skill chain
- **Usage** — Example invocation
- **Output** — What you'll get
- **Next Steps** — Suggested follow-on commands

## Invoking Commands

### In Claude Code/Cowork
```
/discover AI meeting summarizer
```

### In natural conversation
```
"Help me with product discovery for an AI meeting summarizer"
```
(Claude will recognize the intent and suggest `/discover`)

### Chaining commands
```
/discover AI meeting summarizer
# After reviewing output:
/strategy AI meeting tools market
/write-prd Smart transcription with action items
/plan-launch AI meeting assistant
```

## Creating New Commands

See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for command creation guidelines. Key principles:
- Commands orchestrate, skills execute
- Clear handoffs between steps
- Suggest next commands at the end
- Map to real PM workflows
