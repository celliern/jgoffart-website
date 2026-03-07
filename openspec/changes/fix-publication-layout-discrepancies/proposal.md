## Why

The current implementation has layout discrepancies compared to the reference site (chloezapha.com). Key issues include: missing `<ol class="bibliography">` wrapper for publications, inconsistent heading margins, and styling differences in the publication rows.

## What Changes

- Add `<ol class="bibliography">` wrapper around publication lists
- Fix publication row structure to match reference (pub-row class with proper columns)
- Update heading margins to match reference site (2px 0px -15px)
- Fix badge styling and positioning
- Ensure proper spacing between publications (using `<br />` between items like reference)

## Capabilities

### New Capabilities
- None (this is a styling fix only)

### Modified Capabilities
- `publication-grid-layout`: Modify to use proper bibliography list structure
- `tailwind-styling`: Modify to match reference site CSS classes

## Impact

- `templates/index.html`: Update publication section HTML structure
- CSS classes: Add bibliography, pub-row styling
