## MODIFIED Requirements

### Requirement: ORCID API fetch script
The project SHALL include a Python script to fetch publications from the ORCID public API.

#### Scenario: Handles dict values correctly
- **WHEN** API returns field as `{'value': 'actual value'}`
- **THEN** script extracts `'actual value'` not the dict representation

#### Scenario: Clean markdown output
- **WHEN** publication markdown is generated
- **THEN** frontmatter shows clean values: `journal = "Journal Name"` not `journal = "{'value': 'Journal Name'}"`

### Requirement: Publication data mapping
The script SHALL map ORCID work fields to markdown frontmatter.

#### Scenario: Journal extracted correctly
- **WHEN** work has journal information
- **THEN** journal appears as clean string in frontmatter

#### Scenario: URL extracted correctly  
- **WHEN** work has URL
- **THEN** URL appears as clean string, not dict representation
