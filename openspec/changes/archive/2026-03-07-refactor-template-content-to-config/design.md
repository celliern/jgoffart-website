## Context

The current Zola static website has several maintainability issues:

1. **Hardcoded template content**: The `templates/index.html` contains personal information (name, position, university, email), social links, and content sections (About me, Research Interests, Working Papers, Other) directly embedded in the template. This violates the separation of concerns principle - templates should focus on presentation while content should be in markdown/config files.

2. **Custom CSS instead of Tailwind**: The `static/style.css` file contains 346 lines of custom CSS for layout, colors, typography, and responsive design. However, Tailwind CSS is already loaded via CDN in `templates/base.html` but is barely utilized. This redundancy creates maintenance overhead.

3. **Float-based layout**: The current layout uses CSS float for the sidebar/content split, which is outdated and harder to maintain compared to modern CSS Grid or Flexbox.

Current architecture:
- `config.toml`: Minimal configuration (base_url, title, description)
- `templates/index.html`: Hardcoded profile + publications loop
- `static/style.css`: Custom CSS for all styling
- `content/_index.md`: Partial content, not fully utilized

## Goals / Non-Goals

**Goals:**
- Move all hardcoded profile data (name, position, email, social links) to `config.toml` under `[extra]`
- Move content sections (About me, Research Interests, Working Papers, Other) to appropriate markdown files in `content/`
- Migrate all CSS styling to Tailwind utility classes
- Achieve feature parity with current design while improving maintainability
- Ensure responsive design works correctly
- Support dark mode through Tailwind's dark mode classes

**Non-Goals:**
- No visual redesign (keep current aesthetic)
- No new features beyond what's currently implemented
- No changes to the publications data structure
- No JavaScript functionality changes
- No build process modifications (keep CDN Tailwind)

## Decisions

### Decision 1: Use config.toml extra for profile data
**Rationale**: Zola's `[extra]` section is designed for custom configuration data. This is the idiomatic way to store personal information that templates need to access via `config.extra.field_name`.

**Alternative considered**: Frontmatter in content/_index.md. Rejected because config.toml is the standard location for site-wide metadata that doesn't change per-page.

### Decision 2: Keep CDN Tailwind instead of build-time
**Rationale**: The current setup uses CDN Tailwind via CDN. While a build-time setup would be more optimal for production, keeping CDN maintains simplicity and zero build configuration changes.

**Alternative considered**: Installing Tailwind via npm and configuring PostCSS. Rejected to avoid adding build complexity to a simple static site.

### Decision 3: Use Tailwind's dark mode via 'class' strategy
**Rationale**: Need to match the current `prefers-color-scheme: dark` behavior. Using `dark:` modifier classes allows explicit dark mode control.

**Configuration needed**:
```javascript
tailwind.config = {
  darkMode: 'class',
  // ... rest of config
}
```

Then add dark mode class detection:
```javascript
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
  document.documentElement.classList.add('dark');
}
```

### Decision 4: Replace float layout with Flexbox
**Rationale**: Float-based layouts are deprecated. Flexbox provides cleaner code and better responsive behavior. The 960px fixed-width wrapper will be replaced with max-width container + flex layout.

**Layout structure**:
- Desktop: Sidebar (w-60 fixed) + Main content (flex-1)
- Mobile: Stacked layout using flex-col

### Decision 5: Remove style.css entirely
**Rationale**: All styles can be expressed with Tailwind utilities. The few custom elements (like `pub-item`, `pub-content`) will become utility class combinations.

**Exception**: May keep minimal CSS for very specific styling that Tailwind can't easily express, or for Google Fonts loading optimization.

### Decision 6: Use prose classes for markdown content
**Rationale**: Tailwind's `@tailwindcss/typography` plugin (via CDN with prose classes) provides beautiful typography for markdown content. This will replace the current manual typography styles.

**CDN approach**: Use `https://cdn.jsdelivr.net/npm/@tailwindcss/typography@0.5.10/dist/umd/index.min.js` or include prose classes manually since typography is included in the Play CDN.

## Risks / Trade-offs

**[Risk] Tailwind CDN has larger payload than custom CSS**
→ Mitigation: The site is small and simple; CDN caching helps. Accept trade-off for maintainability.

**[Risk] Custom HTML elements in current CSS (like `<position>`, `<email>`, `<pubtitle>`) need migration**
→ Mitigation: These will be converted to semantic HTML (`<span>`, `<p>`, `<h3>`) with Tailwind classes. This is actually an improvement (custom elements are non-standard).

**[Risk] Responsive breakpoints may not match exactly**
→ Mitigation: Current breakpoint is 960px. Tailwind's `lg` breakpoint is 1024px, `md` is 768px. Will use `lg` for the main breakpoint and adjust spacing as needed.

**[Risk] Typography may look slightly different**
→ Mitigation: Carefully map current font sizes (16px base, 28px h1, etc.) to Tailwind equivalents. Use `text-base`, `text-2xl`, etc. with custom sizes in tailwind.config if needed.

**[Risk] Dark mode color scheme needs manual mapping**
→ Mitigation: Document the current color variables and map them to Tailwind colors or custom config.

Current colors (light mode):
- Background: #fff → `bg-white`
- Text: #595959 → `text-gray-600`
- Heading: #043361 → Custom or `text-slate-800`
- Link: #39c → `text-sky-500`
- Border: #e5e5e5 → `border-gray-200`

Dark mode:
- Background: #20212b → `bg-gray-900` or `dark:bg-[#20212b]`
- Text: #dadbdf → `dark:text-gray-300`
- Heading: #3eb7f0 → `dark:text-sky-400`

## Migration Plan

1. **Phase 1: Config and Content Setup**
   - Update config.toml with [extra] profile data
   - Update content/_index.md with about me and research interests
   - Ensure working-papers.md and other.md have proper frontmatter

2. **Phase 2: Template Refactoring**
   - Update base.html with proper Tailwind config and dark mode
   - Rewrite index.html to use Tailwind classes and read from config/content
   - Ensure all semantic HTML is preserved

3. **Phase 3: Style Migration**
   - Remove style.css (or minimize)
   - Verify all styling matches visually
   - Test responsive behavior at various breakpoints
   - Test dark mode toggle/detection

4. **Phase 4: Validation**
   - Run `zola serve` and verify site renders correctly
   - Compare side-by-side with original if possible
   - Check all links work
   - Verify publications display correctly

**Rollback strategy**: Keep original files backed up or in git. If issues arise, revert to previous commit.

## Open Questions

1. Should we add a manual dark mode toggle button, or stick with system preference detection?
   - **Resolution**: Stick with system preference for now to maintain current behavior. Manual toggle can be future enhancement.

2. How should social media links be structured in config.toml?
   - **Resolution**: Use a table array:
     ```toml
     [[extra.social]]
     name = "Google Scholar"
     url = "https://scholar.google.com/..."
     icon = "google-scholar"
     icon_type = "academicons"
     ```
