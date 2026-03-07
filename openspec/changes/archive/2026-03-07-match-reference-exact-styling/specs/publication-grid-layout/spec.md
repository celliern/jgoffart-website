## MODIFIED Requirements

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
