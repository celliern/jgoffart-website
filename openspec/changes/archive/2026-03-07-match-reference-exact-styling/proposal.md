## Why

The current website styling has discrepancies with the reference site (chloezapha.com). The layout, colors, and overall appearance don't match the professional academic style of the reference. This change implements the exact CSS and HTML structure from the reference site.

## What Changes

- Completely rewrite templates/index.html to match reference site structure
- Use exact CSS from reference site (style.css + publications.css)
- Match heading colors, fonts, and spacing exactly
- Use proper Bootstrap-style grid classes (col-sm-3, col-sm-9, pub-row)
- Position badges absolutely like reference site
- Use exact color scheme (#002D72 for badges, #043361 for links)

## Capabilities

### New Capabilities
- None

### Modified Capabilities
- `tailwind-styling`: Replaced with exact reference CSS
- `publication-grid-layout`: Updated to use Bootstrap-style classes

## Impact

- templates/index.html: Complete rewrite with exact reference structure
- All CSS moved inline to match reference exactly
