# publication-badges Specification

## Purpose
TBD - created by archiving change match-reference-style-fix-publications. Update Purpose after archive.
## Requirements
### Requirement: Publications support badge field in frontmatter
The system SHALL support a badge field in publication frontmatter to display paper type indicators.

#### Scenario: Working paper with WP badge
- **WHEN** a publication has `extra.badge = "WP"` in frontmatter
- **THEN** it SHALL display a "WP" badge in the image column
- **AND** the badge SHALL be styled distinctly from regular content

#### Scenario: Publication with custom badge
- **WHEN** a publication has any value in `extra.badge` field
- **THEN** that value SHALL be displayed as the badge text
- **AND** the badge SHALL render consistently across all papers

### Requirement: Badge styling is consistent
The system SHALL apply consistent styling to all badges.

#### Scenario: Badge appearance
- **WHEN** rendering a badge
- **THEN** it SHALL have a distinct visual style (background, border, or color)
- **AND** text SHALL be centered within the badge
- **AND** badge SHALL be appropriately sized (not overwhelming the layout)

### Requirement: Badge works with or without image
The system SHALL display badges whether or not an image is present.

#### Scenario: Badge with image
- **WHEN** a publication has both badge and image
- **THEN** both SHALL be visible in the image column
- **AND** badge MAY overlay the image or appear beside it

#### Scenario: Badge without image
- **WHEN** a publication has badge but no image
- **THEN** the badge SHALL occupy the image column alone
- **AND** the content SHALL still use the 9-column section

