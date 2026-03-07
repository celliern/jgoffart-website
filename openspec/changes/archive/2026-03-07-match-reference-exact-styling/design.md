## Context

After analyzing the reference site (chloezapha.com), the key differences are:

1. **HTML Structure**: Uses semantic elements like `<position>`, `<email>`, `<autocolor>`
2. **CSS Classes**: Uses Bootstrap-style classes (col-sm-3, col-sm-9, pub-row)
3. **Badge Positioning**: Badges are positioned absolutely within the image column
4. **Color Scheme**: Specific colors (#002D72, #043361, #3eb7f0)
5. **Typography**: Specific font sizes and weights from Crimson Pro font family

## Goals / Non-Goals

**Goals:**
- Match reference site appearance exactly
- Use same HTML structure
- Use same CSS properties
- Maintain dark mode support

**Non-Goals:**
- No new features
- No content changes

## Decisions

### Decision 1: Inline CSS
Placed all CSS inline in the template to match reference site approach exactly.

### Decision 2: Semantic HTML
Using `<position>`, `<email>`, `<autocolor>` elements like reference site.

### Decision 3: Exact Colors
Using #002D72 for badges, #043361 for light mode links, #3eb7f0 for dark mode.

## Risks / Trade-offs

**[Risk] Large inline CSS block**
→ Acceptable for exact matching of reference site.
