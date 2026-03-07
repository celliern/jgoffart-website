## Why

The current website layout needs refinement to match the professional academic style of the reference site (chloezapha.com). Additionally, publications without images currently display with empty space where the image would be, creating an unbalanced layout. This change addresses both the visual styling and the publication layout issues.

## What Changes

- Update publication layout to use a 3-column/9-column grid system (image/content split)
- Fix publications without images to not have empty space - content should span full width
- Add badge support for working papers (e.g., "WP" badge)
- Match reference site color scheme and typography more closely
- Restructure content sections to separate Working Papers, Work in Progress, and Publications
- Add autocolor functionality for automatic dark/light mode text colors
- **BREAKING**: Restructure content/publications to separate working papers from publications
- **BREAKING**: Update publication frontmatter to support badge field

## Capabilities

### New Capabilities
- `publication-grid-layout`: 3/9 column grid for publications with image/content split
- `publication-badges`: Support for badge indicators (WP, Journal, etc.)
- `autocolor-elements`: Automatic text color adaptation for dark/light mode
- `content-section-separation`: Separate Working Papers, Work in Progress, and Publications sections

### Modified Capabilities
- `content-driven-sections`: Modified to support separate Working Papers section with badge support
- `tailwind-styling`: Modified to add autocolor classes and publication grid styles

## Impact

- Templates (`templates/index.html`): Significant refactoring for grid layout and section structure
- Content (`content/publications/`): Frontmatter updates to add badge field and separate working papers
- CSS: New autocolor classes and grid layout utilities needed
- Config: May need color variable updates for autocolor functionality
