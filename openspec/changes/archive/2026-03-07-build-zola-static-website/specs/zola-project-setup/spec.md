## ADDED Requirements

### Requirement: Zola project initialization
The project SHALL be initialized with `zola init` command creating the standard directory structure.

#### Scenario: Zola init creates base structure
- **WHEN** `zola init jeanne-goffart-website` is run
- **THEN** directories `content/`, `templates/`, `static/`, `themes/` are created

### Requirement: Tailwind CSS integration
The project SHALL include Tailwind CSS built via CLI for styling.

#### Scenario: Tailwind CLI is available
- **WHEN** Tailwind CLI is downloaded for the current platform
- **THEN** `static/tailwindcss` executable exists

#### Scenario: CSS build configuration exists
- **WHEN** build is run
- **THEN** `static/style.css` is generated from Tailwind input

### Requirement: Project configuration
The project SHALL include a `config.toml` with proper base_url and settings.

#### Scenario: Config specifies base URL
- **WHEN** config.toml is created
- **THEN** `base_url` is set to the production URL
