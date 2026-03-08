## Why

Currently, the publication template (`templates/index.html`) only supports local image assets via `get_url(path=page.extra.image)`. Users cannot use remote URLs (e.g., `https://example.com/image.png`) for publication images, which limits flexibility when referencing images hosted externally or on CDNs.

## What Changes

- Modify the template logic to detect whether `extra.image` is a local path or a remote URL
- For local paths: continue using `get_url(path=...)` as before
- For remote URLs: use the URL directly without transformation
- Update documentation to clarify both local and remote image support

## Capabilities

### New Capabilities
- `remote-image-support`: Support for both local asset paths and remote URLs in `extra.image` field

### Modified Capabilities
<!-- No existing spec-level requirements are changing - this is purely template logic enhancement -->

## Impact

- **Template**: `templates/index.html` - Lines 57-58 and 111-112 where `get_url(path=page.extra.image)` is used
- **Documentation**: May need updates to show examples of both local and remote images
- **Backward compatibility**: Fully backward compatible - existing local image paths continue to work
