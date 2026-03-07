## Context

Build a personal academic website for Jeanne Goffart using Zola static site generator. The site should mirror the layout and structure of chloezapha.com (a Jekyll Minimal Light theme) but use Zola with Tailwind CSS instead.

**Reference site structure:**
- Left sidebar: Avatar, Name, Position, Affiliation, Email, Social icons
- Main content: About, Research Interests, Working Papers, Publications, Work in Progress, Other

**Data source:** ORCID 0000-0003-1234-8293 (6 publications in building performance / sensitivity analysis)

**Constraints:**
- Use Zola as SSG
- Use Tailwind CSS for styling
- Content in Markdown files
- Hosting on Vercel
- Placeholder content (Lorem Ipsum) for non-ORCID sections

## Goals / Non-Goals

**Goals:**
- Replicate chloezapha.com layout with Zola + Tailwind
- Fetch publications from ORCID API automatically
- Support social buttons (Google Scholar, LinkedIn)
- Ensure Vercel deployment compatibility

**Non-Goals:**
- Actual deployment (just ensure compatibility)
- Dynamic content updates (static build only)
- Multiple languages support

## Decisions

### 1. Tailwind Integration

**Decision:** Use Tailwind CLI (no Node.js/npm dependency for Tailwind)

**Rationale:** Zola doesn't have native Tailwind integration. Using the standalone Tailwind CLI:
- No package.json required
- Build step runs `tailwindcss -i input.css -o static/style.css`
- Matches Zola's Sass compilation workflow

### 2. ORCID Data Fetching

**Decision:** Python script using requests library

**Rationale:**
- ORCID public API returns XML/JSON - simple to parse
- Python is universally available
- Script outputs markdown files directly to `content/publications/`

**Alternative:** Use curl + jq (more complex, less maintainable)

### 3. Content Structure

**Decision:** All data in markdown files under `content/`

```
content/
├── _index.md          # Homepage with About, Research Interests
├── publications/
│   ├── _index.md      # Publications list section
│   └── *.md           # Individual publication pages
├── working-papers.md  # Working papers (placeholder)
└── other.md           # Blogs, Awards (placeholder)
```

**Alternative:** Use Zola's data files (`data/`), but markdown allows more flexibility for future expansion

### 4. Vercel Configuration

**Decision:** Include `vercel.json` for explicit framework detection

```json
{
  "framework": "zola",
  "buildCommand": "zola build",
  "outputDirectory": "public"
}
```

**Rationale:** Vercel auto-detects Zola, but explicit config prevents issues

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| ORCID API rate limiting | Cache results, run fetch manually when needed |
| Tailwind updates breaking | Pin to specific version in build script |
| Layout differences from reference | Iterate on templates, use reference CSS as guide |

## Open Questions

- Should the ORCID script run as part of the build or separately?
  - **Recommendation:** Run separately, commit results (static site principle)
- What placeholder image for avatar?
  - **Recommendation:** Use a solid color placeholder, user can replace
