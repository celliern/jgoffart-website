## MODIFIED Requirements

### Requirement: Publications use 3/9 column grid layout
The system SHALL render publications using a grid layout with 3 columns for images/badges and 9 columns for content, wrapped in a bibliography ordered list.

#### Scenario: Publication with bibliography structure
- **WHEN** rendering a publication list
- **THEN** it SHALL be wrapped in `<ol class="bibliography">`
- **AND** each publication SHALL be an `<li>` element
- **AND** there SHALL be a `<br />` element between each publication item
- **AND** the row SHALL use `pub-row` class structure with `col-sm-3` and `col-sm-9` columns

#### Scenario: Publication with image in bibliography
- **WHEN** a publication has an image
- **THEN** it SHALL render in a 3/9 grid within the bibliography list
- **AND** use `col-sm-3 abbr` class for image column with relative positioning
- **AND** use `col-sm-9` class for content column

#### Scenario: Publication without image in bibliography
- **WHEN** a publication has no image or badge
- **THEN** it SHALL render as full-width within the bibliography list
- **AND** content SHALL span the full width without empty image space

## REMOVED Requirements

### Requirement: Grid is responsive
**Reason**: Using bibliography structure with Bootstrap-style classes instead of Tailwind grid
**Migration**: Use pub-row and col-sm-* classes for layout
