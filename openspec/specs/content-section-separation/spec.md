# content-section-separation Specification

## Purpose
TBD - created by archiving change match-reference-style-fix-publications. Update Purpose after archive.
## Requirements
### Requirement: Working Papers section is separate from Publications
The system SHALL maintain separate sections for Working Papers and Publications.

#### Scenario: Working Papers section exists
- **WHEN** the site has a `content/working-papers/` directory with `_index.md`
- **THEN** a "Working Papers" section SHALL be rendered on the main page
- **AND** it SHALL appear before the Publications section

#### Scenario: Work in Progress section
- **WHEN** a Work in Progress section is defined in content
- **THEN** it SHALL render as a separate section
- **AND** it SHALL appear between Working Papers and Publications

### Requirement: Section ordering is configurable
The system SHALL allow control over section ordering via frontmatter.

#### Scenario: Section ordering via weight
- **WHEN** sections have `weight` field in their `_index.md` frontmatter
- **THEN** they SHALL be sorted by weight in ascending order
- **AND** sections without weight SHALL appear after weighted sections

### Requirement: Empty sections are handled gracefully
The system SHALL handle sections that have no content.

#### Scenario: Empty Working Papers section
- **WHEN** the working-papers section has no pages
- **THEN** the section header SHALL not render
- **OR** it SHALL render with a "No working papers" placeholder message

