## 1. Zola Project Setup

- [x] 1.1 Initialize Zola project with `zola init jeanne-goffart-website`
- [x] 1.2 Configure config.toml with base_url and settings
- [x] 1.3 Download Tailwind CSS CLI for current platform
- [x] 1.4 Create tailwind.config.js with content paths
- [x] 1.5 Create input.css with Tailwind directives

## 2. Academic Layout Templates

- [x] 2.1 Create base.html template with HTML structure
- [x] 2.2 Create homepage.html template extending base
- [x] 2.3 Add header with avatar, name, position, affiliation, email
- [x] 2.4 Add social icons (Google Scholar, LinkedIn)
- [x] 2.5 Add content sections (About, Research Interests, Publications, etc.)
- [x] 2.6 Apply Tailwind classes for styling

## 3. ORCID Integration Script

- [x] 3.1 Create fetch_orcid.py script
- [x] 3.2 Implement ORCID API fetch for works endpoint
- [x] 3.3 Parse JSON response to extract publication data
- [x] 3.4 Generate markdown files for each publication
- [x] 3.5 Add frontmatter with title, year, journal, DOI
- [x] 3.6 Run script to fetch 6 publications from ORCID 0000-0003-1234-8293

## 4. Placeholder Content

- [x] 4.1 Create content/_index.md with About section (Lorem Ipsum)
- [x] 4.2 Add Research Interests section with placeholder bullets
- [x] 4.3 Create content/working-papers.md with placeholder content
- [x] 4.4 Create content/other.md with placeholder blogs/awards
- [x] 4.5 Update homepage template to include all sections

## 5. Publications Display

- [x] 5.1 Create publications section in homepage template
- [x] 5.2 Loop through content/publications/ to list all papers
- [x] 5.3 Add publication cards with image, title, year, journal
- [x] 5.4 Style publications with Tailwind

## 6. Vercel Compatibility

- [x] 6.1 Create vercel.json with framework, buildCommand, outputDirectory
- [x] 6.2 Test local build with `zola build`
- [x] 6.3 Verify public/ directory contains static files
- [x] 6.4 Add build script to package.json or Makefile
