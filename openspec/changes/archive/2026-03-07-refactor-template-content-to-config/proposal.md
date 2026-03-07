## Why

The current Zola website has hardcoded content directly in templates (name, position, university, email, bio, research interests, working papers, footer) which makes it difficult to maintain and update. Additionally, most styling is done using standard CSS in `style.css` instead of leveraging Tailwind CSS which is already loaded via CDN. This creates unnecessary complexity and misses out on Tailwind's utility-first benefits.

## What Changes

- Move hardcoded personal information from templates to config.toml:
  - Name, position, university, email
  - Social media links (Google Scholar, CV, LinkedIn)
  - Avatar path
  - Footer content and credits

- Move content sections from templates to markdown:
  - About me section → content/_index.md
  - Research interests → content/_index.md
  - Working papers content → content/working-papers.md
  - Other content → content/other.md

- Convert all CSS styling to Tailwind utility classes:
  - Replace custom CSS variables with Tailwind's built-in colors and dark mode support
  - Convert all layout styles (float-based sidebar) to Tailwind flex/grid layouts
  - Replace custom responsive breakpoints with Tailwind's responsive modifiers
  - Use Tailwind's typography, spacing, and color utilities
  - **BREAKING**: Remove style.css entirely or minimize to only essential custom styles

- Update templates to read from config and content:
  - Use `config.extra` for personal data
  - Use `section.content` for markdown-rendered content
  - Apply Tailwind classes instead of custom CSS classes

## Capabilities

### New Capabilities
- `config-driven-profile`: Profile information (name, position, contact) configurable via config.toml
- `config-driven-social`: Social media links configurable via config.toml
- `content-driven-sections`: About me, research interests, working papers, other sections moved to markdown
- `tailwind-styling`: Complete migration from custom CSS to Tailwind utility classes
- `responsive-layout`: Responsive sidebar/main layout using Tailwind flexbox

### Modified Capabilities
- None (no existing specs to modify)

## Impact

- Templates (`templates/base.html`, `templates/index.html`): Significant refactoring to use Tailwind classes and read from config
- Config (`config.toml`): New extra fields added for profile and social data
- Content (`content/_index.md`, `content/working-papers.md`, `content/other.md`): New content sections to be added or enhanced
- Static (`static/style.css`): Will be removed or drastically reduced
- No external dependencies added (Tailwind is already loaded via CDN)
