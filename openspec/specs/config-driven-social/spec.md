# config-driven-social Specification

## Purpose
TBD - created by archiving change refactor-template-content-to-config. Update Purpose after archive.
## Requirements
### Requirement: Social links are configurable via config.toml
The system SHALL define social media links in config.toml as an array of social link objects.

#### Scenario: Multiple social links render
- **WHEN** the template renders the social icons section
- **THEN** it SHALL iterate over `config.extra.social` array
- **AND** render each link with appropriate icon

### Requirement: Social link structure is standardized
Each social link SHALL have required and optional fields.

#### Scenario: Complete social link
- **WHEN** a social link entry has `name`, `url`, `icon`, and `icon_type`
- **THEN** it SHALL render with the specified icon from the appropriate icon library
- **AND** have a title attribute with the name
- **AND** open in a new tab with `target="_blank"` and `rel="noopener"`

#### Scenario: Social link with only required fields
- **WHEN** a social link entry has only `name`, `url`, and `icon`
- **THEN** it SHALL default `icon_type` to "fontawesome"
- **AND** render with Font Awesome classes

### Requirement: Icon library support
The system SHALL support both Font Awesome and Academicons.

#### Scenario: Font Awesome icon
- **WHEN** `icon_type` is "fontawesome"
- **THEN** the icon SHALL use the `fab fa-{icon}` class format

#### Scenario: Academicons icon
- **WHEN** `icon_type` is "academicons"
- **THEN** the icon SHALL use the `ai ai-{icon}` class format

