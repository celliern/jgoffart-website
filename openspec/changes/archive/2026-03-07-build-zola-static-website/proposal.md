## Why

Create a personal academic website for Jeanne Goffart using Zola static site generator, matching the layout and structure of the reference site chloezapha.com. The site will display publications fetched from ORCID (0000-0003-1234-8293) with placeholder content for other sections.

## What Changes

- Initialize Zola project with Tailwind CSS integration
- Create base templates matching the reference layout (header, sidebar, content sections)
- Implement ORCID fetch script to automatically import publications
- Add placeholder content (Lorem Ipsum) for About, Research Interests, Working Papers, Other sections
- Configure Vercel deployment compatibility
- Add social buttons (Google Scholar, LinkedIn)

## Capabilities

### New Capabilities

- **zola-project-setup**: Initialize Zola project with Tailwind CSS and proper directory structure
- **academic-layout**: Create base templates replicating chloezapha.com layout (avatar, name, position, affiliation, social icons)
- **orcid-integration**: Script to fetch publications from ORCID API and generate markdown content
- **placeholder-content**: Lorem Ipsum content for About, Research Interests, Working Papers, and Other sections
- **vercel-compatibility**: Configuration files for Vercel deployment

### Modified Capabilities

- None (new project)

## Impact

- New project directory with Zola structure
- Tailwind CSS integration via CLI
- Python script for ORCID data fetching
- Markdown content files in `content/` directory
- Vercel configuration (vercel.json)
