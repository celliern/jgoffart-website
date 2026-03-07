## ADDED Requirements

### Requirement: Publications use 3/9 column grid layout
The system SHALL render publications using a grid layout with 3 columns for images/badges and 9 columns for content.

#### Scenario: Publication with image
- **WHEN** a publication has an image in its frontmatter
- **THEN** it SHALL render in a 3/9 grid (25% image, 75% content)
- **AND** the image SHALL be in the left 3-column section
- **AND** the title, author, journal, and links SHALL be in the right 9-column section

#### Scenario: Publication with badge
- **WHEN** a publication has a badge but no image
- **THEN** it SHALL still render in a 3/9 grid
- **AND** the badge SHALL occupy the left 3-column section
- **AND** the content SHALL occupy the right 9-column section

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
