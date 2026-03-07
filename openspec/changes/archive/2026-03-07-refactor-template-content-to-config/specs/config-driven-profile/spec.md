## ADDED Requirements

### Requirement: Profile data is configurable via config.toml
The system SHALL read all profile information from config.toml under the `[extra]` section instead of hardcoding in templates.

#### Scenario: Profile renders from config
- **WHEN** the template renders the header/profile section
- **THEN** it SHALL read name from `config.extra.name`
- **AND** position from `config.extra.position`
- **AND** university from `config.extra.university`
- **AND** email from `config.extra.email`
- **AND** avatar path from `config.extra.avatar`

### Requirement: University link is configurable
The system SHALL support an optional university URL in config.toml.

#### Scenario: University with link
- **WHEN** `config.extra.university_url` is set
- **THEN** the university name SHALL be rendered as a link to that URL

#### Scenario: University without link
- **WHEN** `config.extra.university_url` is not set
- **THEN** the university name SHALL be rendered as plain text

### Requirement: Template uses semantic HTML
The system SHALL replace custom HTML elements with semantic alternatives.

#### Scenario: Position element replaced
- **WHEN** rendering the position field
- **THEN** it SHALL use `<span>` or `<p>` with Tailwind classes instead of `<position>`

#### Scenario: Email element replaced
- **WHEN** rendering the email field
- **THEN** it SHALL use `<span>` or `<a>` with Tailwind classes instead of `<email>`
