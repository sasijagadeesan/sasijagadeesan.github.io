#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates index.html and sitemap.xml from scripts/papers_data.py. Run
from anywhere; paths are resolved relative to the repository root.

    python3 scripts/generate_homepage.py

Publication cards deliberately show only title, full author order,
journal, and year — no author-position labels (see CLAUDE.md
"Author-position policy"; that data still lives in papers.csv).
"""
import html
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
from papers_data import PAPERS, SITE, ORCID  # noqa: E402


def esc(s):
    return html.escape(s, quote=True)


CATEGORY_ORDER = [
    ("Human Spinal Cord Biology & Regenerative Neuroscience",
     "Adult human spinal cord biology, spinal cord injury, neural stem/progenitor cells (NSPCs), "
     "iPSC-derived neural progenitors, spinal interneurons, and regenerative neuroscience."),
    ("Neurosurgery & Clinical / Translational Research",
     "Human spinal cord tissue procurement in an organ-donation setting, donor-cohort characterization, "
     "procurement governance, and clinical neurosurgical case research."),
    ("Clinical Machine Learning & Predictive Medicine",
     "Electronic health record (EHR)-based machine learning for prediction of clinical deterioration in "
     "critically ill patients."),
    ("Molecular Genetics & Functional Genomics",
     "Computational and experimental discovery of gene function, DNA damage repair, and molecular "
     "mechanisms of translation and RNA biology."),
    ("Yeast Genetics & Cellular Stress Biology",
     "Saccharomyces cerevisiae genetics underlying lithium chloride sensitivity, oxidative stress "
     "responses, and translational regulation of structured mRNAs."),
]


def paper_card(p):
    return f"""
  <div class="publication">
    <h3>
      <a href="/publications/{p['slug']}/">
        {esc(p['title'])}
      </a>
    </h3>
    <p>
      <strong>{esc(p['authors_citation'])}.</strong>
      <em>{esc(p['journal'])}</em>. {p['year']}.
    </p>
    <p class="publication-link">
      <a href="/publications/{p['slug']}/">View publication summary and citation details →</a>
    </p>
  </div>"""


sections_html = []
for cat_name, cat_desc in CATEGORY_ORDER:
    papers_in_cat = [p for p in PAPERS if p["primary_category"] == cat_name]
    cards = "\n".join(paper_card(p) for p in papers_in_cat)
    sections_html.append(f"""
  <h2>{esc(cat_name)}</h2>

  <div class="research">
    <p>{esc(cat_desc)}</p>
  </div>
{cards}
""")

sections_str = "\n".join(sections_html)

knows_about = [
    "Adult human spinal cord biology", "Spinal cord injury", "Neural stem and progenitor cells",
    "iPSC-derived neural progenitors", "Spinal interneurons", "Regenerative neuroscience",
    "Human spinal cord tissue procurement", "Organ donation", "Neurosurgery",
    "Clinical machine learning", "Electronic health records", "MIMIC-IV",
    "Clinical deterioration prediction", "Molecular genetics", "Functional genomics",
    "DNA damage repair", "Yeast genetics", "Saccharomyces cerevisiae", "Oxidative stress",
    "Translational regulation",
]
knows_about_json = ",\n      ".join(f'"{esc(k)}"' for k in knows_about)

INDEX_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>

  <meta charset="UTF-8">
  <meta name="viewport"
        content="width=device-width, initial-scale=1.0">

  <title>
    Sasi Jagadeesan | Neuroscience, Human Spinal Cord Biology, Genetics & Clinical Machine Learning
  </title>

  <meta name="description"
        content="Academic publication hub of Sasi Kumar Jagadeesan: peer-reviewed research in adult human spinal cord biology, spinal cord injury, neural stem/progenitor cells, regenerative neuroscience, neurosurgical and translational spinal cord research, molecular and medical genetics, yeast functional genomics, and clinical machine learning for predicting patient deterioration.">

  <meta name="author"
        content="Sasi Kumar Jagadeesan">

  <meta name="robots"
        content="index, follow">

  <link rel="canonical"
        href="https://sasijagadeesan.github.io/">

  <!-- Open Graph metadata -->
  <meta property="og:title"
        content="Sasi Jagadeesan | Academic Publications">

  <meta property="og:description"
        content="Peer-reviewed research in human spinal cord biology, spinal cord injury and neurosurgery, molecular genetics and functional genomics, yeast cellular stress biology, and clinical machine learning.">

  <meta property="og:type"
        content="website">

  <meta property="og:url"
        content="https://sasijagadeesan.github.io/">

  <!-- Structured researcher metadata -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Sasi Kumar Jagadeesan",
    "alternateName": "Sasi Jagadeesan",
    "url": "https://sasijagadeesan.github.io/",
    "sameAs": [
      "https://orcid.org/{ORCID}",
      "https://github.com/sasijagadeesan",
      "https://scholar.google.com/citations?user=epnSboAAAAAJ&hl=en",
      "https://www.researchgate.net/profile/Sasi-Jagadeesan"
    ],
    "affiliation": {{
      "@type": "Organization",
      "name": "Ottawa Hospital Research Institute"
    }},
    "knowsAbout": [
      {knows_about_json}
    ]
  }}
  </script>

  <style>

    body {{
      font-family: Arial, Helvetica, sans-serif;
      margin: 0;
      background: #f7f9fc;
      color: #1f2937;
      line-height: 1.65;
    }}

    .container {{
      max-width: 980px;
      margin: auto;
      padding: 60px 25px;
    }}

    h1 {{
      font-size: 42px;
      margin-bottom: 5px;
      color: #111827;
    }}

    .subtitle {{
      font-size: 19px;
      color: #4b5563;
      margin-bottom: 25px;
    }}

    .links {{
      margin-bottom: 20px;
    }}

    .links a {{
      margin-right: 18px;
      text-decoration: none;
      color: #1d4ed8;
      font-weight: 600;
    }}

    .links a:hover {{
      text-decoration: underline;
    }}

    h2 {{
      margin-top: 55px;
      padding-bottom: 8px;
      border-bottom: 2px solid #e5e7eb;
      color: #111827;
    }}

    h3 {{
      color: #1f2937;
      margin-top: 0;
      margin-bottom: 8px;
    }}

    .research,
    .publication {{
      background: white;
      padding: 22px 25px;
      border-radius: 10px;
      margin-top: 18px;
    }}

    .publication h3 a {{
      color: #1d4ed8;
      text-decoration: none;
    }}

    .publication h3 a:hover {{
      text-decoration: underline;
    }}

    .publication-link {{
      font-weight: 600;
    }}

    footer {{
      margin-top: 70px;
      color: #6b7280;
      font-size: 14px;
    }}

  </style>

</head>


<body>

<div class="container">

  <h1>Sasi Jagadeesan</h1>

  <div class="subtitle">
    Neuroscientist | Human Spinal Cord Biology | Molecular Genetics | Clinical Machine Learning
  </div>

  <div class="links">

    <a href="https://orcid.org/{ORCID}">
      ORCID
    </a>

    <a href="https://scholar.google.com/citations?user=epnSboAAAAAJ&hl=en">
      Google Scholar
    </a>

    <a href="https://www.researchgate.net/profile/Sasi-Jagadeesan">
      ResearchGate
    </a>

    <a href="https://github.com/sasijagadeesan">
      GitHub
    </a>

  </div>

{sections_str}

  <footer>

    © Sasi Kumar Jagadeesan

    <br>

    ORCID:
    <a href="https://orcid.org/{ORCID}">
      {ORCID}
    </a>

  </footer>


</div>

</body>

</html>
"""

with open(os.path.join(REPO, "index.html"), "w", encoding="utf-8") as f:
    f.write(INDEX_HTML)
print("Wrote index.html")

# ---------- sitemap.xml ----------
urls = [f"{SITE}/"] + [f"{SITE}/publications/{p['slug']}/" for p in PAPERS]
sitemap_entries = "\n\n".join(f"  <url>\n    <loc>{u}</loc>\n  </url>" for u in urls)
SITEMAP = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

{sitemap_entries}

</urlset>
"""
with open(os.path.join(REPO, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(SITEMAP)
print(f"Wrote sitemap.xml with {len(urls)} URLs")
