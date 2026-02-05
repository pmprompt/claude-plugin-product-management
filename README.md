# pmprompt Skills (Claude Code plugin)

A public **Claude Code plugin** that packages a curated set of **product management skills** (frameworks + reusable workflows) from **pmprompt**.

If you’re new to pmprompt, start here:
- Explore the prompt library: https://pmprompt.com/skills
- pmprompt home: https://pmprompt.com

## What you get

This plugin adds a namespaced set of Agent Skills you can invoke in Claude Code, e.g.:

- `/pmprompt:prd-writer`
- `/pmprompt:jobs-to-be-done`
- `/pmprompt:working-backwards`

These skills are designed to help you:
- write clearer product docs (PRDs, updates)
- run structured discovery (JTBD, Opportunity Solution Trees)
- make better decisions under uncertainty
- design experiments and growth systems

## Skill index (high level)

Frameworks and templates included (non-exhaustive):

- **Docs & execution**: PRD Writer, Stakeholder Update Generator
- **Discovery**: Jobs-to-be-Done (JTBD), Opportunity Solution Trees, Working Backwards
- **Planning**: Feature Prioritization (RICE), OKRs, Shape Up, Design Sprint
- **Strategy**: Positioning Canvas, 7 Powers
- **Growth & retention**: Growth Loops, Product-Led Growth, Product-Led SEO
- **Experiments**: A/B Test Designer, Trustworthy Experiments
- **People & leadership**: Radical Candor

Browse the full set in `skills/`.

## Install / test locally

Clone this repo and run Claude Code with the plugin loaded:

```bash
git clone https://github.com/pmprompt/skills.git
cd skills
claude --plugin-dir .
```

Once Claude Code starts, invoke a skill:

- `/pmprompt:prd-writer`
- `/pmprompt:shape-up`

## How to use (recommended workflow)

1. Start with a real problem you’re working on (a feature, a decision, a roadmap tradeoff).
2. Pick the matching skill.
3. Paste your context (users, constraints, success metrics, current state).
4. Treat the output as a **draft** and iterate.

If you want more of the “why” behind these workflows, the canonical versions live at:
- https://pmprompt.com/skills

## Repo structure

- `.claude-plugin/plugin.json` — plugin manifest
- `.claude-plugin/marketplace.json` — marketplace metadata (team/community installs)
- `skills/<skill-name>/SKILL.md` — individual Agent Skills

## Principles

- **No internal operating workflows**: This repo intentionally contains no private IDs, tokens, customer data, or internal content ops.
- **Practical over perfect**: Skills are meant to ship better decisions and documents, not theory.

## License

TBD (add once we decide public usage terms).
