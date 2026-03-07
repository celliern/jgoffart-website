## Context

The website at chloezapha.com uses the "Minimal Light" Jekyll theme with:
- Left sidebar: avatar, name, position, affiliation, email, social icons
- Main content: About, Research Interests, Publications, Working Papers, Other
- Fonts: Lato (serif), Lora (for content)
- Academic icons from academicons
- Publication cards: image on left, title/journal/links on right

Current Zola implementation uses different styling that doesn't match.

## Goals / Non-Goals

**Goals:**
- Match chloezapha.com layout exactly
- Fix journal/URL display (currently shows dict values)
- Maintain Zola + Tailwind tech stack

**Non-Goals:**
- Add dark mode support
- Add additional features beyond matching reference

## Decisions

### 1. Font Handling

**Decision:** Use CDN-hosted fonts (Lato, Lora) similar to reference site

**Rationale:** Reference site uses Google Fonts CDN - matching ensures visual consistency

### 2. Layout Structure

**Decision:** Use CSS Grid/Flexbox to replicate sidebar layout

**Rationale:** Zola templates use Tera templating - CSS Grid provides clean responsive layout matching reference

### 3. Publication Cards

**Decision:** Match reference structure: image left, text right with proper formatting

**Rationale:** Reference uses specific HTML structure for publications - replicating ensures visual match

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| Tailwind classes may conflict with reference CSS | Use custom CSS for reference-specific styling |
| Dict values in other fields | Audit all ORCID field parsing |

## Open Questions

- None - reference site provides clear target
