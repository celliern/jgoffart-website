## 1. Template Logic Enhancement

- [x] 1.1 Modify `templates/index.html` - Update working papers section (lines 57-58) to detect remote URLs using `page.extra.image is starting_with("http")`
- [x] 1.2 Modify `templates/index.html` - Update publications section (lines 111-112) with same logic
- [x] 1.3 Ensure both locations use consistent conditional logic: `{% if page.extra.image is starting_with("http") %}{{ page.extra.image }}{% else %}{{ get_url(path=page.extra.image) }}{% endif %}`

## 2. Testing & Validation

- [x] 2.1 Test with local image path - verify `get_url()` is still applied correctly
- [x] 2.2 Test with HTTP URL - verify URL renders directly without transformation
- [x] 2.3 Test with HTTPS URL - verify URL renders correctly
- [x] 2.4 Test with uppercase HTTP/HTTPS - verify case-insensitive detection works

## 3. Documentation

- [x] 3.1 Update README or documentation to mention both local and remote image support
- [x] 3.2 Add example showing remote URL usage in frontmatter
