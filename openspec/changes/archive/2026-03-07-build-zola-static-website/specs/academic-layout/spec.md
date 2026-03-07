## ADDED Requirements

### Requirement: Base layout template
The project SHALL include a base HTML template replicating the chloezapha.com layout structure.

#### Scenario: Header with avatar and info
- **WHEN** page renders
- **THEN** avatar image, name, position, affiliation, and email are displayed

#### Scenario: Social icons present
- **WHEN** page renders
- **THEN** social icons for Google Scholar and LinkedIn are displayed as clickable links

### Requirement: Homepage layout
The homepage SHALL render content sections in the correct order.

#### Scenario: Homepage sections render
- **WHEN** homepage is loaded
- **THEN** sections appear in order: About, Research Interests, Publications, Working Papers, Other

### Requirement: Tailwind styling applied
The templates SHALL use Tailwind CSS classes for all styling.

#### Scenario: Styles apply correctly
- **WHEN** page is rendered
- **THEN** Tailwind utility classes are applied to all elements
