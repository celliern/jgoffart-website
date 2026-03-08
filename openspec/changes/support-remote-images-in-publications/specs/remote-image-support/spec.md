## ADDED Requirements

### Requirement: Local image paths continue to work
The template SHALL continue to support local image assets using `get_url(path=...)` when the `extra.image` value does not start with `http://` or `https://`.

#### Scenario: Local image path renders correctly
- **WHEN** a publication has `extra.image` set to a local path like `"images/paper-thumbnail.png"`
- **THEN** the template SHALL generate an img tag with src="/images/paper-thumbnail.png" (processed by get_url)

### Requirement: Remote URLs are rendered directly
The template SHALL render remote URLs directly in the img src attribute without applying `get_url()` transformation when the value starts with `http://` or `https://`.

#### Scenario: HTTP URL renders correctly
- **WHEN** a publication has `extra.image` set to `"http://example.com/image.png"`
- **THEN** the template SHALL generate an img tag with src="http://example.com/image.png" (no get_url transformation)

#### Scenario: HTTPS URL renders correctly
- **WHEN** a publication has `extra.image` set to `"https://example.com/image.png"`
- **THEN** the template SHALL generate an img tag with src="https://example.com/image.png" (no get_url transformation)

### Requirement: URL detection is case-insensitive
The template SHALL detect remote URLs regardless of case (HTTP, Http, https, HTTPS).

#### Scenario: Mixed case URL renders correctly
- **WHEN** a publication has `extra.image` set to `"HTTPS://example.com/image.png"`
- **THEN** the template SHALL generate an img tag with src="HTTPS://example.com/image.png" (treated as remote URL)
