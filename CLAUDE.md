# CLAUDE.md — Repository Instructions for sasijagadeesan.github.io

## Purpose

This repository is Sasi Kumar Jagadeesan's academic publication hub: a
discoverability surface for his real, peer-reviewed research, built so
scholarly search engines and AI retrieval systems can find and correctly
cite it.

**Non-goals:** this is not a citation-manipulation project. No exaggerated
claims, no keyword stuffing, no fabricated findings, no encouragement of
inappropriate citation. Every factual claim on this site must trace to a
verifiable source.

## Source of truth

`papers.csv` is the single source of truth for the publication list. To add
a new publication:

1. Verify it (see "Verification hierarchy" below).
2. Add one row to `papers.csv` with every column filled in, or explicitly
   left blank with a note if a field cannot be verified.
3. Generate/update the corresponding page under `publications/<slug>/index.html`.
4. Add the new page's URL to `sitemap.xml`.
5. Add a card for it to the relevant category section of `index.html`.

Do not hand-edit a publication page's bibliographic data without updating
`papers.csv` to match — the two must never drift apart.

## Verification hierarchy

When verifying a publication, prefer sources in this order:

1. Publisher page
2. Crossref / DOI record
3. PubMed
4. PubMed Central
5. Journal site

Google Scholar and ResearchGate are useful for **discovery** only — never
treat them as the authoritative source for bibliographic or scientific
metadata.

## Hard rules — never guess

Never fabricate or guess: DOI, PMID, PMCID, publication date, author list,
author order, volume, issue, article number/pages, abstract text, or
findings. If a field cannot be verified, leave it blank in `papers.csv` and
omit it from the page (do not print an empty "PMID:" line). Note the gap in
the `notes` column instead.

If two sources disagree (e.g., a search snippet returns a PMCID that
belongs to a different paper), do not pick one — leave the field blank and
flag the conflict in `notes` until it's resolved against a primary source.

## Scientific-accuracy rules

- Never infer a scientific conclusion from the title alone.
- "Study Overview," "Key Findings," "Why This Study Matters," and
  "Scientific Questions" sections must be written only from the abstract or
  full text (or, when neither is accessible, from an explicit
  publisher-supplied summary the author has provided directly — see the
  Scientific Reports EHR-ML page for an example of this exception, marked
  as such).
- If no abstract or full text is available, write no scientific summary at
  all — a bibliographic-only entry is fine until it can be verified.
- Do not exaggerate novelty, clinical relevance, translational impact, or
  causality beyond what the source states.

## Author-position policy

Every peer-reviewed paper the author co-authored gets a dedicated page —
**author position is never a reason to exclude a paper.** Author position
must instead be recorded accurately:

- `papers.csv` → `author_position` column: `first`, `co-first`, or `middle`.
- Every page's meta/bibliographic box includes a `role-note` line stating
  Sasi Kumar Jagadeesan's actual role (e.g., "First author," "Co-first
  author (with X)," or "Contributing author (Nth of M authors); this study
  was led by [first author] et al.").
- Narrative sections (Overview, Key Findings, Why It Matters) are always
  written in neutral third person about "the study" / "the research team,"
  never "I discovered" or "we led," when the author was a contributing
  (non-first) author.

## Research category taxonomy

Each paper gets exactly one `primary_category` and zero or more
`secondary_categories`, from this fixed list:

1. **Human Spinal Cord Biology & Regenerative Neuroscience** — adult human
   spinal cord biology, NSPCs, iPSC-derived neural progenitors, spinal
   interneurons, regenerative neuroscience.
2. **Neurosurgery & Clinical / Translational Research** — human tissue
   procurement, donor cohorts, procurement governance, clinical
   neurosurgical case research.
3. **Clinical Machine Learning & Predictive Medicine** — EHR-based ML,
   MIMIC-IV, early warning scores, clinical deterioration prediction.
4. **Molecular Genetics & Functional Genomics** — gene-function discovery,
   DNA damage repair, computational genomics, RNA/translation biology not
   specific to yeast stress phenotypes.
5. **Yeast Genetics & Cellular Stress Biology** — *Saccharomyces
   cerevisiae* genetics, lithium chloride sensitivity, oxidative stress,
   translational regulation of structured mRNAs.

Do not invent new categories without updating this list and the homepage
section order to match.

## Keyword and topic usage

Each page's `<meta name="keywords">` and "Relevant Research Topics" tags
should use only terms genuinely supported by that paper's content — 5–10
terms per page is typical. Do not paste the sitewide master keyword list
onto every page; that is keyword stuffing and is explicitly against this
project's objective.

## Page template contract

Every dedicated publication page must include:

- Exact, verified title and author order
- `Sasi Kumar Jagadeesan's role: ...` line
- Journal, year, volume/issue/pages or article number
- DOI (always), PMID and PMCID only when verified
- Links to publisher, DOI, PubMed, and PMC (only for identifiers that exist)
- Study Overview, Key Findings (or "Key Points Covered" for reviews), Why
  This Study Matters, Scientific Questions, Relevant Research Topics tags
- Formatted citation (Vancouver style)
- `<link rel="canonical">` pointing at `https://sasijagadeesan.github.io/publications/<slug>/`
- `<meta name="robots" content="index, follow">`
- Google Scholar–compatible `citation_*` meta tags
- `Schema.org` `ScholarlyArticle` JSON-LD (author list, identifiers,
  `isPartOf` periodical, keywords, `sameAs` links)

## Sitemap rule

Every dedicated publication page must appear in `sitemap.xml`. When adding
a page, add its URL to the sitemap in the same change. Do not add any
`robots.txt` directive that blocks legitimate search or retrieval crawlers
— keep crawling open (`Allow: /`) unless there is a specific, stated
technical reason not to.

## Regeneration

The pages in this repository were originally produced by a small
data-driven generator (a Python script driven by the same fields as
`papers.csv`) rather than hand-written one at a time, to keep all 17+ pages
structurally consistent. When adding several publications at once, prefer
regenerating from a data source over hand-editing HTML directly, to avoid
drift between pages.
