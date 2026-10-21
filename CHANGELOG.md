# Changelog

All notable changes to this Claude plugin will be documented here.

## [Unreleased]

### Fixed
- Plugin failed to load in current Claude Code with "conflicting manifests" because the marketplace entry set `strict: false` and also listed `skills` while the plugin ships its own `plugin.json`. The entry no longer declares components; skills and commands are discovered from `skills/` and `commands/` (#4)

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
