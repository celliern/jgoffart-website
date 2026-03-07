## MODIFIED Requirements

### Requirement: Base layout template
The project SHALL include a base HTML template replicating the chloezapha.com layout structure.

#### Scenario: Fonts loaded from CDN
- **WHEN** page renders
- **THEN** Lato and Lora fonts are loaded from Google Fonts CDN

#### Scenario: Academic icons loaded
- **WHEN** page renders
- **THEN** academicons and font-awesome are loaded from CDN

#### Scenario: Header with avatar and info
- **WHEN** page renders
- **THEN** avatar image, name, position, affiliation, and email are displayed

#### Scenario: Social icons present
- **WHEN** page renders
- **THEN** social icons for Google Scholar, LinkedIn are displayed as clickable links
