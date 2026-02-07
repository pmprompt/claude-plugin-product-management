# AGENTS.md

Standards for agents (and humans) working in this repository.

## Non-negotiables

- **No secrets**: never commit tokens, cookies, API keys, credentials, or private URLs.
- **No internal ops**: this repo must remain clean for public distribution.
- **Small PRs**: changes should be easy to review.
- **Truthful content**: no fabricated metrics/testimonials.

## What good looks like

- Skills are practical for professional PM workflows.
- Outputs are structured and shareable.
- The README stays accurate and concise.

## Workflow

1. Make changes in a branch.
2. Validate JSON:
   - `.claude-plugin/plugin.json`
   - `.claude-plugin/marketplace.json`
3. Sanity check skills:
   - each `skills/*/SKILL.md` has frontmatter `name` + `description`
4. Update `CHANGELOG.md` for user-facing changes.
