## ADDED Requirements

### Requirement: Working papers support badge field
The system SHALL support badge field for working papers to indicate paper type.

#### Scenario: Working paper with badge renders correctly
- **WHEN** a working paper has `extra.badge` in frontmatter
- **THEN** the badge SHALL be displayed alongside the paper
- **AND** the Working Papers section SHALL use the publication grid layout

## MODIFIED Requirements

### Requirement: Working papers section is content-driven
The system SHALL render working papers content from a dedicated section or markdown file, with support for the publication grid layout and badges.

#### Scenario: Working papers from section
- **WHEN** rendering the Working Papers section
- **THEN** it SHALL read from `content/working-papers/` section
- **AND** render each paper using the publication grid layout
- **AND** support badge field for each paper

#### Scenario: Working papers from file (fallback)
- **WHEN** `content/working-papers/` section does not exist
- **THEN** it SHALL fall back to `content/working-papers.md` file
- **AND** render the markdown content without grid layout
