#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates papers.csv and every publications/<slug>/index.html page from
scripts/papers_data.py. Run from anywhere; paths are resolved relative to
the repository root (the parent of this script's directory).

    python3 scripts/generate_pages.py

Author position (first / co-first / middle) is recorded in papers.csv for
internal metadata and future automation only. It is deliberately NOT
rendered on public pages: pages list the complete published author order
and describe the study neutrally, without labeling anyone's contribution
level or naming a "lead" author.
"""
import csv
import html
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
from papers_data import PAPERS, SITE, ORCID  # noqa: E402


def esc(s):
    return html.escape(s, quote=True)


# ---------- CSV ----------
CSV_PATH = os.path.join(REPO, "papers.csv")
fieldnames = ["slug", "title", "authors", "author_position", "journal", "year", "volume", "issue",
              "pages_or_article_number", "doi", "pmid", "pmcid", "publisher_url", "open_access_status",
              "publication_type", "primary_category", "secondary_categories", "has_dedicated_page",
              "verification_status", "verification_sources", "verification_date", "notes"]


def author_position_value(p):
    rn = p["role_note"].lower()
    if rn.startswith("first"):
        return "first"
    if rn.startswith("co-first"):
        return "co-first"
    return "middle"


with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for p in PAPERS:
        notes = p.get("pmcid_note", "") or p.get("extra_note", "")
        w.writerow({
            "slug": p["slug"],
            "title": p["title"],
            "authors": "; ".join(p["authors_full"]),
            "author_position": author_position_value(p),
            "journal": p["journal"],
            "year": p["year"],
            "volume": p["volume"],
            "issue": p["issue"],
            "pages_or_article_number": p["pages"],
            "doi": p["doi"],
            "pmid": p["pmid"],
            "pmcid": p["pmcid"],
            "publisher_url": p["publisher_url"],
            "open_access_status": p["oa"],
            "publication_type": p["pub_type"],
            "primary_category": p["primary_category"],
            "secondary_categories": "; ".join(p["secondary_categories"]),
            "has_dedicated_page": "yes",
            "verification_status": "user-confirmed" if p["slug"] in (
                "ehr-machine-learning-icu-clinical-deterioration",
                "pex11-rim20-lithium-chloride-pgm2-translation",
                "spinal-cord-tissue-procurement-governance",
            ) else "search-corroborated (secondary sources; not fetched from primary source directly)",
            "verification_sources": p["publisher_url"],
            "verification_date": "2026-09-19",
            "notes": notes,
        })

print(f"Wrote {CSV_PATH} with {len(PAPERS)} rows")

# ---------- HTML template ----------
STYLE = """
  <style>
    body { font-family: Arial, Helvetica, sans-serif; margin: 0; background: #f7f9fc; color: #1f2937; line-height: 1.65; }
    .container { max-width: 980px; margin: auto; padding: 50px 25px; }
    a { color: #1d4ed8; text-decoration: none; }
    a:hover { text-decoration: underline; }
    .back { margin-bottom: 30px; font-weight: 600; }
    h1 { font-size: 32px; line-height: 1.25; color: #111827; }
    h2 { margin-top: 45px; border-bottom: 2px solid #e5e7eb; padding-bottom: 8px; color: #111827; }
    .meta { background: white; padding: 20px 24px; border-radius: 10px; margin-top: 20px; }
    .section { background: white; padding: 22px 25px; border-radius: 10px; margin-top: 18px; }
    .tag { display: inline-block; background: #eef2ff; padding: 5px 10px; margin: 4px 5px 4px 0; border-radius: 6px; font-size: 14px; }
    .caveat { background: #fffbeb; border: 1px solid #fde68a; padding: 14px 18px; border-radius: 8px; margin-top: 18px; font-size: 14px; }
    footer { margin-top: 60px; color: #6b7280; font-size: 14px; }
  </style>
"""


def links_block(p):
    parts = [f'<a href="{p["publisher_url"]}">Publisher article</a>']
    if p["pmid"]:
        parts.append(f'<a href="https://pubmed.ncbi.nlm.nih.gov/{p["pmid"]}/">PubMed</a>')
    if p["pmcid"]:
        parts.append(f'<a href="https://pmc.ncbi.nlm.nih.gov/articles/{p["pmcid"]}/">PubMed Central full text</a>')
    parts.append(f'<a href="https://doi.org/{p["doi"]}">DOI</a>')
    return " |\n      ".join(parts)


def jsonld(p):
    ids = [f'"https://doi.org/{p["doi"]}"']
    same_as = [f'"https://doi.org/{p["doi"]}"']
    if p["pmid"]:
        ids.append(f'"PMID:{p["pmid"]}"')
        same_as.append(f'"https://pubmed.ncbi.nlm.nih.gov/{p["pmid"]}/"')
    if p["pmcid"]:
        ids.append(f'"PMCID:{p["pmcid"]}"')
        same_as.append(f'"https://pmc.ncbi.nlm.nih.gov/articles/{p["pmcid"]}/"')
    same_as.append(f'"{p["publisher_url"]}"')
    authors_json = []
    for name in p["authors_full"]:
        if name == "Sasi Kumar Jagadeesan":
            authors_json.append(f'{{"@type": "Person", "name": "Sasi Kumar Jagadeesan", "sameAs": "https://orcid.org/{ORCID}"}}')
        else:
            authors_json.append(f'{{"@type": "Person", "name": "{esc(name)}"}}')
    authors_str = ",\n      ".join(authors_json)
    keywords_str = ",\n      ".join(f'"{esc(t)}"' for t in p["topics"])
    extra_fields = ""
    if p["volume"]:
        extra_fields += f'    "volumeNumber": "{p["volume"]}",\n'
    if p["issue"]:
        extra_fields += f'    "issueNumber": "{p["issue"]}",\n'
    if p["pages"]:
        extra_fields += f'    "pagination": "{esc(p["pages"])}",\n'
    return f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ScholarlyArticle",
    "headline": "{esc(p['title'])}",
    "name": "{esc(p['title'])}",
    "datePublished": "{p['pub_date']}",
    "identifier": [{", ".join(ids)}],
    "author": [
      {authors_str}
    ],
    "isPartOf": {{
      "@type": "Periodical",
      "name": "{esc(p['journal'])}"
    }},
{extra_fields}    "keywords": [
      {keywords_str}
    ],
    "sameAs": [{", ".join(same_as)}]
  }}
  </script>
"""


def citation_meta(p):
    lines = [f'  <meta name="citation_title" content="{esc(p["title"])}">', ""]
    for name in p["authors_full"]:
        lines.append(f'  <meta name="citation_author" content="{esc(name)}">')
    lines.append("")
    lines.append(f'  <meta name="citation_publication_date" content="{p["pub_date"]}">')
    lines.append(f'  <meta name="citation_journal_title" content="{esc(p["journal"])}">')
    if p["volume"]:
        lines.append(f'  <meta name="citation_volume" content="{p["volume"]}">')
    if p["issue"]:
        lines.append(f'  <meta name="citation_issue" content="{p["issue"]}">')
    if p["pages"]:
        lines.append(f'  <meta name="citation_firstpage" content="{esc(p["pages"])}">')
    lines.append(f'  <meta name="citation_doi" content="{p["doi"]}">')
    return "\n".join(lines)


def bib_meta_box(p):
    # NOTE: deliberately no author-position / role-note line here. Public
    # pages show the complete published author order and nothing about who
    # led the work — see CLAUDE.md "Author-position policy".
    rows = [f'    <strong>Authors:</strong>\n    {", ".join(esc(a) for a in p["authors_full"])}']
    rows.append(f'    <br><br>\n    <strong>Journal:</strong> {esc(p["journal"])}')
    rows.append(f'    <br>\n    <strong>Year:</strong> {p["year"]}')
    if p["volume"]:
        rows.append(f'    <br>\n    <strong>Volume:</strong> {p["volume"]}')
    if p["issue"]:
        rows.append(f'    <br>\n    <strong>Issue:</strong> {p["issue"]}')
    if p["pages"]:
        rows.append(f'    <br>\n    <strong>Pages / Article number:</strong> {esc(p["pages"])}')
    rows.append(f'    <br>\n    <strong>DOI:</strong>\n    <a href="https://doi.org/{p["doi"]}">{p["doi"]}</a>')
    if p["pmid"]:
        rows.append(f'    <br>\n    <strong>PMID:</strong>\n    <a href="https://pubmed.ncbi.nlm.nih.gov/{p["pmid"]}/">{p["pmid"]}</a>')
    if p["pmcid"]:
        rows.append(f'    <br>\n    <strong>PMCID:</strong>\n    <a href="https://pmc.ncbi.nlm.nih.gov/articles/{p["pmcid"]}/">{p["pmcid"]}</a>')
    rows.append(f'    <br>\n    <strong>Publication type:</strong> {esc(p["pub_type"])}')
    rows.append(f'    <br>\n    <strong>Open access:</strong> {esc(p["oa"])}')
    return "\n".join(rows)


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>{title_tag} | Sasi Jagadeesan</title>

  <meta name="description"
        content="{description}">

  <meta name="keywords"
        content="{keywords_meta}">

  <meta name="author" content="Sasi Kumar Jagadeesan">
  <meta name="robots" content="index, follow">

  <!-- Google Scholar / citation metadata -->
{citation_meta}

  <link rel="canonical"
        href="{canonical}">

{jsonld}
{style}
</head>

<body>

<div class="container">

  <div class="back">
    <a href="/">← Back to Sasi Jagadeesan publication hub</a>
  </div>

  <h1>
    {title_html}
  </h1>

  <div class="meta">
{meta_box}
  </div>

  <h2>Study Overview</h2>

  <div class="section">
{overview_html}
  </div>

  <h2>{findings_heading}</h2>

  <div class="section">
    <ul>
{findings_html}
    </ul>
  </div>

  <h2>Why This Study Matters</h2>

  <div class="section">
    <p>{why_matters}</p>
  </div>

  <h2>Scientific Questions This Paper Informs</h2>

  <div class="section">
    <ul>
{questions_html}
    </ul>
  </div>

  <h2>Relevant Research Topics</h2>

  <div class="section">
{topics_html}
  </div>

  <h2>Citation</h2>

  <div class="section">
    <p>
      {authors_citation}.
      {title_html_inline}.
      <em>{journal}</em>. {year}{vol_issue_pages}.
      doi:{doi}.
    </p>
  </div>
{extra_caveat}
  <h2>Original Article</h2>

  <div class="section">
    <p>
      {links}
    </p>
  </div>

  <footer>
    Sasi Kumar Jagadeesan · ORCID {orcid}
  </footer>

</div>

</body>
</html>
"""


def build_page(p):
    canonical = f"{SITE}/publications/{p['slug']}/"
    overview_html = "\n".join(f"    <p>{esc(par)}</p>" for par in p["overview"])
    findings_html = "\n".join(f"      <li>{esc(f)}</li>\n" for f in p["findings"])
    questions_html = "\n".join(f"      <li>{esc(q)}</li>\n" for q in p["questions"])
    topics_html = "\n".join(f'    <span class="tag">{esc(t)}</span>' for t in p["topics"])
    vol_issue_pages = ""
    if p["volume"]:
        vip = f";{p['volume']}"
        if p["issue"]:
            vip += f"({p['issue']})"
        if p["pages"]:
            vip += f":{p['pages']}"
        vol_issue_pages = vip
    elif p["pages"]:
        vol_issue_pages = f";{p['pages']}"
    extra_caveat = ""
    if p.get("extra_note"):
        extra_caveat = f'\n  <div class="caveat"><strong>Note:</strong> {esc(p["extra_note"])}</div>\n'
    description = p["overview"][0][:280] if p["overview"] else p["title"]
    return PAGE_TEMPLATE.format(
        title_tag=esc(p["title"]),
        description=esc(description),
        keywords_meta=esc(", ".join(t.lower() for t in p["topics"])),
        citation_meta=citation_meta(p),
        canonical=canonical,
        jsonld=jsonld(p),
        style=STYLE,
        title_html=esc(p["title"]),
        title_html_inline=esc(p["title"]),
        meta_box=bib_meta_box(p),
        overview_html=overview_html,
        findings_heading=esc(p["findings_heading"]),
        findings_html=findings_html,
        why_matters=esc(p["why_matters"]),
        questions_html=questions_html,
        topics_html=topics_html,
        authors_citation=esc(p["authors_citation"]),
        journal=esc(p["journal"]),
        year=p["year"],
        vol_issue_pages=esc(vol_issue_pages),
        doi=p["doi"],
        extra_caveat=extra_caveat,
        links=links_block(p),
        orcid=ORCID,
    )


created = []
for p in PAPERS:
    if p.get("existing"):
        continue
    outdir = os.path.join(REPO, "publications", p["slug"])
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "index.html")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(build_page(p))
    created.append(outpath)

print(f"Wrote {len(created)} publication pages")
