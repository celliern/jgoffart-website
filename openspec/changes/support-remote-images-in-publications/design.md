## Context

The current template at `templates/index.html` uses `get_url(path=page.extra.image)` to render publication images. This Zola/tera function only processes local assets and fails silently or produces broken links when given remote URLs.

The change affects two locations in the template:
- Lines 57-58: Working papers section
- Lines 111-112: Publications section

Both use identical logic that needs enhancement.

## Goals / Non-Goals

**Goals:**
- Support remote URLs (http/https) in `page.extra.image` field
- Maintain full backward compatibility with existing local image paths
- Keep template logic clean and maintainable
- Provide clear documentation for users

**Non-Goals:**
- Support other protocols (ftp, file://, etc.)
- Add image optimization or caching for remote images
- Change the data model or content structure
- Support dynamic image URLs from external APIs

## Decisions

### Decision: Use URL pattern detection in template
**Choice**: Detect if image value starts with `http://` or `https://`
**Rationale**: Simple, reliable, requires no external dependencies
**Alternative considered**: Using Zola's `is_external` filter (doesn't exist in current Zola version)

### Decision: Keep single `extra.image` field
**Choice**: Use the same field for both local and remote images
**Rationale**: Backward compatible, simpler for users, no content migration needed
**Alternative considered**: Adding separate `extra.image_url` field (rejected - adds complexity)

## Risks / Trade-offs

- **[Risk]** Remote image URLs may break if external site is down → **Mitigation**: Document that users should use reliable hosting; local assets recommended for critical images
- **[Risk]** Remote images may not follow site's security/CSP policies → **Mitigation**: No action - user responsibility when choosing external URLs
- **[Trade-off]** No automatic fallback if remote image fails

## Migration Plan

No migration needed - fully backward compatible. Existing sites continue to work unchanged.

To use the new feature, users simply add remote URLs to their frontmatter:
```yaml
extra:
  image: "https://example.com/paper-thumbnail.png"
```

## Open Questions

None - implementation approach is clear.
