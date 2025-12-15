# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Add `extrakwargs` parameter to `{% icon %}` template tag allowing a mapping of attributes to be merged with direct kwargs (direct kwargs override collisions).

## [0.4.0] - 2025-12-03

### 🚀 Features

- feat: add show_icon_registry management command
- feat: add automatic icon renderer detection

### 🐛 Fixes

- fix: correct icon mappings in sprites renderer tests

### 🧪 Tests

- test: add comprehensive tests for show_icon_registry command
- test: add tests for icon registry and auto-detection

### 🔧 Chores

- chore: update development tooling and dependencies
- chore: update example template formatting

### Other

- updated package meta files
- update release notes based on commit messages

## [0.3.0] - 2025-09-26

### Added

- Support attr dict to icon tag

## [0.2.4] - 2025-09-10

- no changes

## [0.2.3] - 2025-09-10

- no changes

## [0.1.0] - Initial Release

### Added

- Initial release
- SVG, Provider, and Sprites renderers
- Template tag support
- Configuration system
- Comprehensive test suite

[Unreleased]: https://github.com/SamuelJennings/django-easy-icons/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/SamuelJennings/django-easy-icons/releases/tag/v0.4.0
[0.3.0]: https://github.com/SamuelJennings/django-easy-icons/releases/tag/v0.3.0
[0.2.4]: https://github.com/SamuelJennings/django-easy-icons/releases/tag/v0.2.4
[0.2.3]: https://github.com/SamuelJennings/django-easy-icons/releases/tag/v0.2.3
[0.1.0]: https://github.com/SamuelJennings/django-easy-icons/releases/tag/v0.1.0
