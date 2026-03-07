## Context

The reference site (chloezapha.com) uses a specific HTML structure for publications:

```html
<div class="publications">
<ol class="bibliography">
<li>
<div class="pub-row">
  <div class="col-sm-3 abbr" style="position: relative;">
    <img src="..." class="teaser img-fluid z-depth-1" />
    <abbr class="badge">WP</abbr>
  </div>
  <div class="col-sm-9" style="position: relative;">
    <div class="title"><a href="...">Title</a></div>
    <div class="author">...</div>
    <div class="periodical"><em>Journal</em></div>
    <div class="links"><a href="..." class="btn btn-sm z-depth-0">PDF</a></div>
  </div>
</div>
</li>
<br />
</ol>
</div>
```

Current issues:
- We're not using the `<ol class="bibliography">` wrapper
- Missing `<br />` between list items
- Not using `pub-row`, `col-sm-3`, `col-sm-9` classes
- Heading margins need adjustment

## Goals / Non-Goals

**Goals:**
- Match reference site HTML structure exactly
- Use proper bibliography ordered list
- Fix publication row layout
- Match heading margins (2px 0px -15px)

**Non-Goals:**
- No new functionality
- No content changes

## Decisions

### Decision 1: Use Tailwind to replicate Bootstrap classes
Use Tailwind utilities to match the visual appearance of `col-sm-3`, `col-sm-9`, `pub-row` classes without adding custom CSS.

### Decision 2: Add br elements between publications
Reference site has `<br />` between list items. We'll add these for visual spacing.

### Decision 3: Keep bibliography semantic
Use `<ol class="bibliography">` for semantic correctness and styling hooks.

## Risks / Trade-offs

**[Risk] Tailwind classes may not match Bootstrap exactly**
→ Mitigation: Use closest Tailwind equivalents and adjust as needed.

**[Risk] br elements may affect accessibility**
→ Mitigation: Use CSS spacing instead if possible, or keep minimal br usage.
