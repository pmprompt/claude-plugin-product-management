# Changelog

All notable changes to this Claude plugin will be documented here.

## [Unreleased]

### Added
- Codex support: a Codex plugin manifest (`.codex-plugin/plugin.json`, version 0.5.0, same name, description, author, links, license, and keywords as `.claude-plugin/plugin.json`) and a repo marketplace (`.agents/plugins/marketplace.json`), plus Codex install steps in the README. Thanks to @rforgeon, whose #3 first added these
- `evals/product-management/`: 35 harness-neutral eval cases covering all 30 skills, a scoring rubric with pass/fail rules, and `check_cases.py` to check that every skill has a case. Builds on the eval format from @rforgeon's #3

## [0.5.0] - 2026-10-21

### Added
- `/pmprompt:agent-spec-generator`: interviews you, then writes a spec for an AI agent covering scope, tools and permissions, autonomy levels (suggest only, act with approval, act and notify, fully autonomous) with criteria for each, approval boundaries, stop rules, escalation, memory, data access, failure modes, must-never-do rules, evals, observability, and rollout
- `/pmprompt:ai-ship-bar`: a ship-bar doc for AI features with task completion, precision and recall, p95 latency, cost per successful request, eval set design, thresholds and sign-off, regression gates, and post-launch monitoring. Example thresholds are labeled as examples

### Changed
- Version bumped to 0.5.0 in `plugin.json` and `marketplace.json`, so `claude plugin update` delivers the two new skills to existing installs

## [0.4.0] - 2026-10-21

### Fixed
- Frontmatter in 8 skills (`ab-test-designer`, `breadboarding`, `competitive-analysis-framework`, `feature-prioritization-assistant`, `prd-writer`, `shaping`, `stakeholder-update-generator`, `user-feedback-synthesizer`) now parses as strict YAML. Descriptions containing `: ` and bracketed `argument-hint` values are quoted. `shaping`, `breadboarding` and `competitive-analysis-framework` previously did not parse at all. Thanks to @timdp, whose #2 first fixed three of these
- `commands/README.md` no longer loads as a `/pmprompt:README` command; it moved to `docs/commands.md`
- Plugin failed to load in current Claude Code with "conflicting manifests" because the marketplace entry set `strict: false` and also listed `skills` while the plugin ships its own `plugin.json`. The entry no longer declares components; skills and commands are discovered from `skills/` and `commands/` (#4)

### Added
- `description` and `argument-hint` frontmatter on all 9 workflow commands
- `NOTICE` and README credit for the skills adapted from David Turner's [product-skills](https://github.com/wdavidturner/product-skills) (MIT)

### Changed
- README: one-step install line (`/plugin install pmprompt --marketplace pmprompt/claude-plugin-product-management`) and the full marketplace install name `pmprompt@pmprompt-skills`
- Contributor notes moved from the plugin root `CLAUDE.md` to `.claude/CLAUDE.md` (a root `CLAUDE.md` isn't loaded by installed plugins and fails `claude plugin validate --strict`)
- Removed the unrecognized `metadata.repository` field from `marketplace.json`
- Version bumped to 0.4.0 in `plugin.json` and `marketplace.json`, so `claude plugin update` delivers the fixes above (and the #4 fix) to existing installs

## [0.3.0] - 2026-02-08

### Added
- Added `/pmprompt:shaping` and `/pmprompt:breadboarding` skills (original implementations; inspired by rjs/shaping-skills)

## [0.2.0] - 2026-02-06

### Changed
- Reframed as a **Claude plugin for product managers** (Claude Code + Cowork)
- Added clearer install instructions and marketplace commands
- Improved plugin metadata (keywords, links)

## [0.1.0] - 2026-02-05

### Added
- Initial public release of pmprompt skills as a Claude plugin
