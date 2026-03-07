#!/usr/bin/env python3
"""
Fetch publications from ORCID and generate markdown files.
"""

import os
import json
import urllib.request

ORCID_ID = os.environ.get("ORCID_ID", "0000-0003-1234-8293")
OUTPUT_DIR = "content/publications"


def fetch_orcid_works(orcid_id):
    """Fetch works from ORCID public API.

    Uses the pub.orcid.org endpoint which serves public data without authentication.
    See: https://info.orcid.org/what-is-orcid/services/public-api/
    """
    # pub.orcid.org serves public data - this is the correct endpoint for public API
    url = f"https://pub.orcid.org/v3.0/{orcid_id}/works"

    req = urllib.request.Request(url)
    req.add_header("Accept", "application/json")
    req.add_header("User-Agent", "Mozilla/5.0 (compatible; Academic Website/1.0)")

    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode())


def extract_value(field):
    """Extract value from field that might be a dict or string."""
    if isinstance(field, dict):
        return field.get("value", "")
    return field if field else ""


def parse_works(data):
    """Parse the ORCID works response and extract publication info."""
    publications = []

    for group in data.get("group", []):
        work_summary = group.get("work-summary", [None])[0]
        if not work_summary:
            continue

        # Get title
        title_elem = work_summary.get("title", {})
        title = extract_value(title_elem.get("title"))

        # Get year
        pub_date = work_summary.get("publication-date", {})
        year = extract_value(pub_date.get("year"))
        if not year:
            year = "n.d."

        # Get journal name
        journal = extract_value(work_summary.get("journal-title"))

        # Get URL
        url = extract_value(work_summary.get("url"))

        # Get work type
        work_type = work_summary.get("type", "")

        # Get external IDs for DOI
        external_ids = work_summary.get("common:external-ids", {})
        doi = ""
        for ext_id in external_ids.get("common:external-id", []):
            if ext_id.get("common:external-id-type") == "doi":
                doi = ext_id.get("common:external-id-value", "")
                break

        # Build URL if we have DOI
        if doi and not url:
            url = f"https://doi.org/{doi}"

        pub = {
            "title": title,
            "year": year,
            "journal": journal,
            "url": url,
            "doi": doi,
            "type": work_type,
        }
        publications.append(pub)

    return publications


def slugify(text):
    """Convert title to slug for filename."""
    import re

    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text)
    return text[:50]


def create_markdown(publication, index):
    """Create markdown file content for a publication."""
    title = publication["title"]
    year = publication["year"]
    journal = publication["journal"]
    url = publication["url"]
    doi = publication["doi"]

    filename = f"{index:02d}-{slugify(title)}.md"

    content = f"""+++
title = "{title}"
date = {year}-01-01

[extra]
authors = "{year}"
journal = "{journal}"
year = "{year}"
"""

    if url:
        content += f'url = "{url}"\n'

    content += f"""
+++

{title}

* {journal}, {year}
"""

    if doi:
        content += f"\nDOI: [{doi}](https://doi.org/{doi})"

    if url and not doi:
        content += f"\n[Link]({url})"

    return filename, content


def main():
    """Main function to fetch and generate publications."""
    print(f"Fetching publications from ORCID: {ORCID_ID}...")

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Fetch works
    data = fetch_orcid_works(ORCID_ID)

    # Parse publications
    publications = parse_works(data)

    print(f"Found {len(publications)} publications")

    # Generate markdown files
    for i, pub in enumerate(publications, 1):
        filename, content = create_markdown(pub, i)
        filepath = os.path.join(OUTPUT_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Created: {filepath}")

    print(f"\nDone! Created {len(publications)} publication files in {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
