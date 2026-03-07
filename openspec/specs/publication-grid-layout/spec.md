# publication-grid-layout Specification

## Purpose
TBD - created by archiving change match-reference-style-fix-publications. Update Purpose after archive.
## Requirements
### Requirement: Publications use 3/9 column grid layout
The system SHALL use Bootstrap-style classes from the reference site (col-sm-3, col-sm-9, pub-row).

#### Scenario: Bootstrap grid layout
- **WHEN** rendering publications
- **THEN** image column SHALL use `col-sm-3` class (25% width)
- **AND** content column SHALL use `col-sm-9` class (75% width)
- **AND** row SHALL use `pub-row` class with flex display
- **AND** items SHALL align to center

#### Scenario: Bibliography structure
- **WHEN** rendering publication list
- **THEN** it SHALL use `<ol class="bibliography">`
- **AND** items SHALL have min-height: 110px
- **AND** spacing SHALL use `<br />` between items

### Requirement: Publications without images span full width
The system SHALL render publications without images or badges to span the full width.

#### Scenario: Publication without image or badge
- **WHEN** a publication has neither image nor badge in frontmatter
- **THEN** the content SHALL span the full 12-column width
- **AND** there SHALL be no empty space reserved for an image

### Requirement: Grid is responsive
The system SHALL make the publication grid responsive on smaller screens.

#### Scenario: Mobile layout
- **WHEN** viewing on screens below 768px
- **THEN** the grid SHALL stack vertically (image/badge on top, content below)
- **AND** both sections SHALL be full width

