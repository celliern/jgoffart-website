## ADDED Requirements

### Requirement: Template uses exact reference HTML
The system SHALL use the same HTML structure as chloezapha.com.

#### Scenario: Header structure
- **WHEN** rendering the header
- **THEN** it SHALL use semantic elements: `<position>`, `<email>`, `<autocolor>`
- **AND** it SHALL have the same class structure as reference

#### Scenario: Publication structure
- **WHEN** rendering publications
- **THEN** it SHALL use `<ol class="bibliography">` wrapper
- **AND** each item SHALL use `<li>` with `<div class="pub-row">`
- **AND** columns SHALL use `col-sm-3` and `col-sm-9` classes

### Requirement: CSS matches reference exactly
The system SHALL use identical CSS properties to chloezapha.com.

#### Scenario: Badge styling
- **WHEN** rendering a badge
- **THEN** it SHALL have background-color: #002D72
- **AND** it SHALL be positioned absolutely (top: 8px, left: 16px)
- **AND** it SHALL have box-shadow

#### Scenario: Link colors
- **WHEN** in light mode
- **THEN** links SHALL be color: #043361
- **WHEN** in dark mode
- **THEN** links SHALL be color: rgb(62, 183, 240)

## MODIFIED Requirements

### Requirement: All styles use Tailwind utility classes
The system SHALL use exact reference CSS from chloezapha.com, replacing Tailwind utility classes with inline CSS that matches the reference.

#### Scenario: Complete reference styling
- **WHEN** viewing any page
- **THEN** all styles SHALL match chloezapha.com exactly
- **AND** colors, fonts, spacing SHALL be identical
- **AND** CSS SHALL be inline in the template
