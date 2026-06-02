#!/usr/bin/env python3
"""
Fetch CycloneDX JSON SBOMs from a public GCS bucket and render them as Markdown.

Usage:
    python sbom_to_markdown.py --bucket my-public-bucket
    python sbom_to_markdown.py --bucket my-public-bucket --prefix releases/v1.0/
    python sbom_to_markdown.py --bucket my-public-bucket --output report.md
    python sbom_to_markdown.py --url https://storage.googleapis.com/my-bucket/sbom.cdx.json
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
import xml.etree.ElementTree as ET


GCS_BASE = "https://storage.googleapis.com"


def list_sbom_objects(bucket: str, prefix: str) -> list[dict]:
    """List objects in a public GCS bucket matching the prefix."""
    params = {"prefix": prefix} if prefix else {}
    query = ("?" + urlencode(params)) if params else ""
    url = f"{GCS_BASE}/storage/v1/b/{bucket}/o{query}"
    try:
        with urlopen(url) as resp:
            data = json.loads(resp.read())
    except HTTPError as e:
        sys.exit(f"Error listing bucket '{bucket}': HTTP {e.code} {e.reason}")
    except URLError as e:
        sys.exit(f"Error reaching GCS: {e.reason}")

    items = data.get("items", [])
    return [
        item for item in items
        if item["name"].endswith(".cdx.json") or item["name"].endswith(".json")
    ]


def fetch_json(url: str) -> dict:
    try:
        with urlopen(url) as resp:
            return json.loads(resp.read())
    except HTTPError as e:
        sys.exit(f"Error fetching {url}: HTTP {e.code} {e.reason}")
    except URLError as e:
        sys.exit(f"Error fetching {url}: {e.reason}")
    except json.JSONDecodeError as e:
        sys.exit(f"Invalid JSON at {url}: {e}")


def format_licenses(licenses: list) -> str:
    if not licenses:
        return "—"
    names = []
    for lic in licenses:
        if isinstance(lic, dict):
            inner = lic.get("license", lic)
            names.append(inner.get("id") or inner.get("name") or "Unknown")
    return ", ".join(names) if names else "—"


def format_hashes(hashes: list) -> str:
    if not hashes:
        return ""
    return " ".join(f"`{h['alg']}:{h['content'][:12]}…`" for h in hashes[:2])


def cyclonedx_to_markdown(sbom: dict, source_url: str) -> str:
    lines: list[str] = []

    # Header
    spec_version = sbom.get("specVersion", "unknown")
    serial = sbom.get("serialNumber", "")
    lines.append(f"# SBOM Report")
    lines.append(f"")
    lines.append(f"> **Source:** {source_url}  ")
    lines.append(f"> **CycloneDX spec version:** {spec_version}  ")
    if serial:
        lines.append(f"> **Serial number:** `{serial}`  ")
    lines.append(f"> **Generated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append("")

    # Metadata
    metadata = sbom.get("metadata", {})
    if metadata:
        lines.append("## Metadata")
        lines.append("")
        ts = metadata.get("timestamp", "")
        if ts:
            lines.append(f"- **Timestamp:** {ts}")
        component = metadata.get("component", {})
        if component:
            lines.append(f"- **Subject component:** {component.get('name', '')} {component.get('version', '')}".strip())
            ctype = component.get("type", "")
            if ctype:
                lines.append(f"- **Type:** {ctype}")
        tools = metadata.get("tools", [])
        if isinstance(tools, dict):
            tools = tools.get("components", [])
        if tools:
            tool_names = [f"{t.get('name','')} {t.get('version','')}".strip() for t in tools]
            lines.append(f"- **Tools:** {', '.join(tool_names)}")
        lines.append("")

    # Components summary
    components = sbom.get("components", [])
    lines.append(f"## Components ({len(components)} total)")
    lines.append("")

    if not components:
        lines.append("_No components listed._")
        lines.append("")
    else:
        # Group by type
        by_type: dict[str, list] = {}
        for c in components:
            t = c.get("type", "unknown")
            by_type.setdefault(t, []).append(c)

        for ctype, comps in sorted(by_type.items()):
            lines.append(f"### {ctype.capitalize()} ({len(comps)})")
            lines.append("")
            lines.append("| Name | Version | License(s) | Hash |")
            lines.append("|------|---------|------------|------|")
            for c in sorted(comps, key=lambda x: x.get("name", "").lower()):
                name = c.get("name", "—")
                purl = c.get("purl", "")
                version = c.get("version", "—")
                lic = format_licenses(c.get("licenses", []))
                hsh = format_hashes(c.get("hashes", []))
                name_cell = f"[{name}]({purl})" if purl else name
                lines.append(f"| {name_cell} | `{version}` | {lic} | {hsh} |")
            lines.append("")

    # Dependencies summary
    dependencies = sbom.get("dependencies", [])
    if dependencies:
        lines.append(f"## Dependency Graph ({len(dependencies)} entries)")
        lines.append("")
        lines.append("| Component | Direct Dependencies |")
        lines.append("|-----------|---------------------|")
        for dep in dependencies:
            ref = dep.get("ref", "—")
            deps_on = dep.get("dependsOn", [])
            count = len(deps_on)
            if count:
                lines.append(f"| `{ref}` | {count} |")
        lines.append("")

    # Vulnerabilities
    vulnerabilities = sbom.get("vulnerabilities", [])
    if vulnerabilities:
        lines.append(f"## Vulnerabilities ({len(vulnerabilities)})")
        lines.append("")
        lines.append("| ID | Severity | Description | Affects |")
        lines.append("|----|----------|-------------|---------|")
        for v in vulnerabilities:
            vid = v.get("id", "—")
            ratings = v.get("ratings", [{}])
            severity = ratings[0].get("severity", "unknown") if ratings else "unknown"
            desc = (v.get("description") or v.get("detail") or "")[:80]
            affects = ", ".join(a.get("ref", "") for a in v.get("affects", [])[:3])
            lines.append(f"| `{vid}` | {severity} | {desc} | {affects} |")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Convert public GCS CycloneDX JSON SBOMs to Markdown."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--bucket", help="Public GCS bucket name")
    group.add_argument("--url", help="Direct URL to a single CycloneDX JSON file")
    parser.add_argument("--prefix", default="", help="Object prefix to filter (used with --bucket)")
    parser.add_argument("--output", default="sbom_report.md", help="Output Markdown file (default: sbom_report.md)")
    args = parser.parse_args()

    sections: list[str] = []

    if args.url:
        sbom = fetch_json(args.url)
        sections.append(cyclonedx_to_markdown(sbom, args.url))
    else:
        objects = list_sbom_objects(args.bucket, args.prefix)
        if not objects:
            sys.exit(f"No .cdx.json / .json files found in bucket '{args.bucket}' with prefix '{args.prefix}'")

        print(f"Found {len(objects)} SBOM file(s).")
        for obj in objects:
            url = f"{GCS_BASE}/{args.bucket}/{obj['name']}"
            print(f"  Fetching: {url}")
            sbom = fetch_json(url)
            sections.append(cyclonedx_to_markdown(sbom, url))

    output_path = Path(args.output)
    separator = "\n\n---\n\n"
    output_path.write_text(separator.join(sections), encoding="utf-8")
    print(f"\nMarkdown written to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
