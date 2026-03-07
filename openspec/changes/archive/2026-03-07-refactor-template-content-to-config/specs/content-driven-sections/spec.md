## ADDED Requirements

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
The system SHALL render working papers content from a dedicated markdown file.

#### Scenario: Working papers from file
- **WHEN** rendering the Working Papers section
- **THEN** it SHALL read from `content/working-papers.md`
- **AND** render the markdown content

#### Scenario: Working papers file missing
- **WHEN** `content/working-papers.md` does not exist or is empty
- **THEN** the Working Papers section SHALL not render
- **OR** render a placeholder message

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
