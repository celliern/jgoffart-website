## Why

The Zola website has two issues:
1. Style mismatch with reference site (chloezapha.com) - layout, fonts, and publication card styling differ significantly
2. Journal display bug - ORCID script outputs dict values like `{'value': 'Journal Name'}` instead of clean strings

## What Changes

- Fix ORCID script to properly handle dict values from API response
- Restyle base template to match reference site (fonts, CDN links, structure)
- Restyle index template to use same sidebar layout and publication card style
- Rebuild and verify

## Capabilities

### New Capabilities

- None (bug fixes and styling updates)

### Modified Capabilities

- **academic-layout**: Update templates to match reference site style
- **orcid-integration**: Fix script to handle dict values properly

## Impact

- `scripts/fetch_orcid.py` - fixed dict handling
- `templates/base.html` - added fonts and CDN links
- `templates/index.html` - matching reference layout and publication styling
- `content/publications/*.md` - regenerated with clean values
