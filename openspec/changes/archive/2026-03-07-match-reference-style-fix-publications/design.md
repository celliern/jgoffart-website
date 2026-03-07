## Context

The reference site (chloezapha.com) uses a specific layout pattern for publications that differs from our current implementation:

1. **Grid-based publication layout**: Uses a 3-column/9-column split (col-sm-3 / col-sm-9) where images occupy 25% width and content occupies 75% width
2. **No empty space for missing images**: When a publication has no image, the content spans the full width instead of leaving empty space
3. **Badge support**: Working papers have badge indicators (e.g., "WP" badge) in the image column
4. **Section separation**: Clear separation between Working Papers, Work in Progress, and Publications sections
5. **Autocolor elements**: Uses `<autocolor>` elements that automatically adapt text color for dark/light mode

Current issues:
- Our publication items always reserve space for images even when none exists
- We don't have badge support for distinguishing paper types
- We lack autocolor functionality for seamless dark mode support
- Our section structure doesn't clearly separate working papers from publications

## Goals / Non-Goals

**Goals:**
- Implement 3/9 column grid layout for publications (25% image / 75% content)
- Handle missing images gracefully (content spans full width when no image)
- Add badge support for working papers and publication types
- Create autocolor CSS class for automatic dark mode text adaptation
- Restructure content to separate Working Papers, Work in Progress, and Publications
- Maintain backward compatibility with existing content

**Non-Goals:**
- No changes to overall site layout or sidebar structure
- No new content creation (just restructuring existing content)
- No JavaScript functionality changes
- No external library additions beyond what's already used

## Decisions

### Decision 1: Use CSS Grid/Flexbox for publication layout instead of fixed columns
**Rationale**: Tailwind's grid and flexbox utilities provide responsive behavior without custom CSS. We'll use `grid grid-cols-12` with conditional spans: 3 cols when image present, 12 cols when absent.

**Alternative considered**: Using `col-sm-3` Bootstrap-style classes. Rejected in favor of Tailwind's native grid system.

### Decision 2: Implement autocolor via CSS custom properties + Tailwind dark mode
**Rationale**: The reference site uses `<autocolor>` elements. We'll implement this as a CSS class that switches between light and dark text colors based on the `dark` class on html element.

**Implementation**:
```css
.autocolor {
  color: #043361; /* Light mode - dark blue */
}
.dark .autocolor {
  color: #dadbdf; /* Dark mode - light gray */
}
```
Or via Tailwind: `text-slate-800 dark:text-gray-300`

### Decision 3: Support badge via frontmatter extra field
**Rationale**: Simplest approach is adding `badge` field to publication frontmatter. If present, rendered as a badge element in the image column.

**Frontmatter example**:
```toml
[extra]
badge = "WP"
image = "paper-image.png"
```

### Decision 4: Separate Working Papers from Publications at content level
**Rationale**: The reference site has distinct sections. We'll use page colocation by moving working papers to `content/working-papers/` and regular publications to `content/publications/`.

**Structure**:
- `content/working-papers/_index.md` - Section definition
- `content/working-papers/*.md` - Individual working papers
- `content/publications/` - Unchanged for published papers

### Decision 5: Content spans full width when no image AND no badge
**Rationale**: This matches the reference behavior. The grid should be conditional:
- Has image or badge: 3/9 split
- No image and no badge: Full width content

## Risks / Trade-offs

**[Risk] Breaking existing publication structure**
→ Mitigation: Create the new structure alongside existing one, verify before removing old structure. All existing publications continue to work in the publications/ folder.

**[Risk] Grid layout complexity with conditional spans**
→ Mitigation: Use simple if/else logic in template: if image or badge, use grid; else use full width.

**[Risk] Autocolor class might not match all text elements**
→ Mitigation: Apply autocolor only to link elements that need it, keep other text with explicit color classes.

**[Risk] Badge styling might conflict with image**
→ Mitigation: Badge overlays on image or sits above it. Position badge absolutely within the image container.

**[Risk] Content migration effort for working papers**
→ Mitigation: Create new working-papers section structure. Working papers from existing content/working-papers.md can be moved to individual files if needed.

## Migration Plan

1. **Phase 1: Template Updates**
   - Update index.html to add grid layout logic for publications
   - Add conditional rendering for image/badge column
   - Add autocolor class support

2. **Phase 2: Content Structure**
   - Create content/working-papers/ directory structure
   - Create _index.md for working papers section
   - Move working papers content if needed

3. **Phase 3: Frontmatter Updates**
   - Add badge field to working paper frontmatter
   - Verify all publications have proper extra fields

4. **Phase 4: CSS/Style Updates**
   - Add autocolor CSS class (either inline in template or minimal CSS)
   - Verify badge styling
   - Test dark mode behavior

5. **Phase 5: Validation**
   - Verify publications with images show 3/9 grid
   - Verify publications without images span full width
   - Verify badges display correctly
   - Test responsive behavior
   - Test dark mode appearance

**Rollback strategy**: Keep git history. Can revert to previous version if layout issues occur.

## Open Questions

1. **Should working papers be in a separate section or just filtered by badge?**
   - **Resolution**: Separate section for clearer organization, matching reference site structure.

2. **What should the badge look like?**
   - **Resolution**: Simple badge similar to reference site - small rectangle with text like "WP", positioned in the image area or as a standalone element.

3. **Should we support multiple badge types?**
   - **Resolution**: Start with text-based badge (WP, R&R, etc.). Can extend to color-coded badges later.
