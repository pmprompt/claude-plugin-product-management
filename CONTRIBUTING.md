# Contributing

Thanks for helping improve the **pmprompt** Claude plugin.

## What this repo is

This is a public plugin that packages product management skills (workflows) for Claude (Claude Code + Cowork).

## Ground rules

- **No secrets**: never commit tokens, cookies, API keys, IDs, or private URLs.
- **No internal ops**: keep anything specific to Andy/pmprompt operations out of this repo.
- **Keep skills generic**: write skills so they work for professional PMs across industries.
- **Be honest**: don’t invent metrics, testimonials, or results.

## How to add or modify a skill

1. Skills live in `skills/<skill-name>/SKILL.md`
2. Each `SKILL.md` must include YAML frontmatter with at least:
   - `name:` (kebab-case)
   - `description:`
3. Keep instructions:
   - specific
   - tool-agnostic where possible
   - written for professional PM workflows

## Testing locally (Claude Code)

```bash
git clone https://github.com/pmprompt/claude-plugin-product-management.git
cd claude-plugin-product-management
claude --plugin-dir .
```

Then run a skill like:

- `/pmprompt:prd-writer`

## Submitting changes

- Open a PR with:
  - what changed
  - why
  - how you tested
- Keep PRs small and focused.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
