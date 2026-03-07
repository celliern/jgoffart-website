## ADDED Requirements

### Requirement: ORCID API fetch script
The project SHALL include a Python script to fetch publications from the ORCID public API.

#### Scenario: Script fetches works
- **WHEN** script is executed with ORCID ID
- **THEN** JSON/XML response containing works is retrieved

#### Scenario: Script outputs markdown
- **WHEN** script successfully fetches works
- **THEN** markdown files are created in `content/publications/`

### Requirement: Publication data mapping
The script SHALL map ORCID work fields to markdown frontmatter.

#### Scenario: Title mapped
- **WHEN** work has a title
- **THEN** title appears in markdown title and frontmatter

#### Scenario: Year extracted
- **WHEN** work has publication date
- **THEN** year is extracted and included in the publication entry

#### Scenario: Journal name extracted
- **WHEN** work has journal information
- **THEN** journal name appears in the publication entry

#### Scenario: DOI link included
- **WHEN** work has a DOI
- **THEN** link to DOI is included in the publication entry

### Requirement: Publications section
The publications SHALL be displayed on the website.

#### Scenario: Publications render
- **WHEN** publications markdown files exist
- **THEN** all publications are listed on the publications section of the homepage
