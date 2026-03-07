## MODIFIED Requirements

### Requirement: Publication grid uses Tailwind grid system
The system SHALL implement the publication grid using a bibliography ordered list structure with pub-row classes, matching the reference site.

#### Scenario: Bibliography structure with pub-row
- **WHEN** rendering publications with images or badges
- **THEN** it SHALL use `<ol class="bibliography">` container
- **AND** each item SHALL be an `<li>` element
- **AND** each row SHALL use `pub-row` class with `col-sm-3 abbr` and `col-sm-9` columns
- **AND** there SHALL be `<br />` spacing between items

#### Scenario: Full width publications in bibliography
- **WHEN** rendering publications without images or badges
- **THEN** it SHALL use bibliography structure
- **AND** content SHALL span full width within the list item

### Requirement: Heading margins match reference
The system SHALL apply specific margins to Working Papers and Publications headings to match the reference site.

#### Scenario: Heading margin style
- **WHEN** rendering Working Papers or Publications heading
- **THEN** it SHALL have inline style `margin: 2px 0px -15px`
- **AND** this SHALL create the negative margin effect from the reference
