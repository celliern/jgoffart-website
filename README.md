# Jeanne Goffart - Personal Academic Website

A static academic website built with [Zola](https://getzola.org/) and Tailwind CSS via CDN, featuring automatic publication fetching from ORCID.

## Installation

### With mise (Recommended)

```bash
# Install mise if not already installed
curl https://mise.run | sh

# Install dependencies
mise install

# Set ORCID_ID environment variable
cp .env.example .env
# Edit .env and set your ORCID_ID
```

### Without mise

```bash
# Install dependencies manually
# - Zola: https://getzola.org/getting-started/installation/
# - Python 3.13+: https://www.python.org/downloads/

# Set ORCID_ID environment variable
cp .env.example .env
# Edit .env and set your ORCID_ID
```

## Making Changes

### 1. Set Environment Variable

```bash
# With mise (automatic)
eval "$(mise activate zsh)"  # or your shell

# Or manually
export ORCID_ID=0000-0003-1234-8293
```

### 2. Edit Content

- **Homepage/About**: Edit `content/_index.md`
- **Research Interests**: Edit `content/_index.md`
- **Working Papers**: Edit `content/working-papers.md`
- **Other (Blogs, Awards)**: Edit `content/other.md`
- **Publications**: Managed via ORCID - edit `scripts/fetch_orcid.py` if needed

### 3. Edit Templates

- **Layout**: Edit `templates/base.html`
- **Homepage**: Edit `templates/index.html`

### 4. Edit Styles

- **Custom styles**: Edit `static/style.css` (regular CSS)

## Building the Site

### Full Build (recommended)

```bash
mise run build-site
```

This will:
1. Fetch publications from ORCID
2. Build the Zola site

Output is in the `public/` directory.

### Individual Commands

```bash
# Fetch publications from ORCID
mise run fetch-orcid

# Build Zola site only
mise run build-site

# Serve locally (development)
mise run serve
```

### Clean Build Artifacts

```bash
mise run clean
```

## ORCID Integration

Publications are automatically fetched from ORCID using the public API.

The script (`scripts/fetch_orcid.py`):
1. Fetches works from `https://pub.orcid.org/v3.0/{ORCID_ID}/works`
2. Parses title, year, journal, and DOI
3. Generates markdown files in `content/publications/`

To update publications:
```bash
mise run fetch-orcid
```

## Deployment

### GitHub Pages

The repository includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that:
1. Builds the site on every push to `main`
2. Uploads the `public/` directory as an artifact
3. Deploys to GitHub Pages

To enable:
1. Go to repository Settings → Pages
2. Set "Source" to "GitHub Actions"
3. Push to `main` branch

### Vercel

The project includes `vercel.json` for Vercel deployment:

```json
{
  "framework": "zola",
  "buildCommand": "zola build",
  "outputDirectory": "public"
}
```

Connect your GitHub repository to Vercel for automatic deployments.

## Project Structure

```
├── content/
│   ├── _index.md          # Homepage
│   ├── publications/       # Auto-generated from ORCID
│   ├── working-papers.md
│   └── other.md
├── templates/
│   ├── base.html          # Base layout
│   └── index.html         # Homepage template
├── scripts/
│   └── fetch_orcid.py     # ORCID fetching script
├── static/
│   └── style.css          # Custom styles (manually edited)
├── config.toml            # Zola configuration
├── mise.toml             # mise configuration
└── vercel.json          # Vercel configuration
```

## License

CC0-1.0 (see reference site)
