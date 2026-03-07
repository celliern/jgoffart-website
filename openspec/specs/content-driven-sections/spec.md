# content-driven-sections Specification

## Purpose
TBD - created by archiving change refactor-template-content-to-config. Update Purpose after archive.
## Requirements
### Requirement: About me section is content-driven
The system SHALL render the About me section from markdown content instead of hardcoded template text.

#### Scenario: About me from content
- **WHEN** rendering the About me section
- **THEN** it SHALL read from `content/_index.md`
- **AND** render the markdown content before the Research Interests section

### Requirement: Research interests are content-driven
The system SHALL render research interests from markdown content.

#### Scenario: Research interests from content
- **WHEN** rendering the Research Interests section
- **THEN** it SHALL read the list from `content/_index.md`
- **AND** render as a styled HTML list

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

### Requirement: Other section is content-driven
The system SHALL render other/miscellaneous content from a dedicated markdown file.

#### Scenario: Other from file
- **WHEN** rendering the Other section
- **THEN** it SHALL read from `content/other.md`
- **AND** render the markdown content

#### Scenario: Other file missing
- **WHEN** `content/other.md` does not exist or is empty
- **THEN** the Other section SHALL not render
- **OR** render a placeholder message

### Requirement: Content frontmatter is standardized
All content files SHALL have proper Zola frontmatter.

#### Scenario: Valid frontmatter
- **WHEN** a content file has frontmatter
- **THEN** it SHALL include `title` field
- **AND** optionally include `template` field
- **AND** optionally include `weight` for ordering

### Requirement: Working papers support badge field
The system SHALL support badge field for working papers to indicate paper type.

#### Scenario: Working paper with badge renders correctly
- **WHEN** a working paper has `extra.badge` in frontmatter
- **THEN** the badge SHALL be displayed alongside the paper
- **AND** the Working Papers section SHALL use the publication grid layout

