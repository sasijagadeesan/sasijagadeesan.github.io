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
is recorded accurately, but never displayed as a public label:

- `papers.csv` → `author_position` column: `first`, `co-first`, or `middle`.
  This is internal metadata for future automation (e.g., sorting or
  filtering by role) — it is not rendered on any page.
- Public pages show only the complete, correctly ordered published author
  list. Do **not** add a "First author" / "Contributing author (Nth of M)"
  / "co-first author" / "led by X et al." label anywhere on a page or on
  the homepage. The author order itself is the only signal shown.
- Narrative sections (Overview, Key Findings, Why It Matters) are always
  written in neutral third person about "the study" / "the research team"
  — never "I discovered" or "we led" — regardless of author position, and
  without adding explanatory authorship commentary either. Describe the
  study, not who did how much of it.

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

- Exact, verified title and complete author order (no role/position label)
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

The pages in this repository are produced by a small data-driven generator
under `scripts/`, not hand-written one at a time, so all pages stay
structurally consistent and `papers.csv` never drifts from the HTML:

- `scripts/papers_data.py` — the single source of truth: one Python dict
  per publication (title, authors, journal, identifiers, category,
  overview/findings/why-it-matters/questions/topics, etc.). This is what
  you edit to add, correct, or remove a publication.
- `scripts/generate_pages.py` — reads `papers_data.py` and writes
  `papers.csv` plus every `publications/<slug>/index.html` page.
- `scripts/generate_homepage.py` — reads `papers_data.py` and writes
  `index.html` and `sitemap.xml`.

To add or correct a publication:

1. Verify it (see "Verification hierarchy" above).
2. Edit the `PAPERS` list in `scripts/papers_data.py` — add a new dict or
   fix an existing one. Leave any unverified field as `""` and note the
   gap in that paper's data rather than guessing.
3. From the repository root, run:

   ```
   python3 scripts/generate_pages.py
   python3 scripts/generate_homepage.py
   ```

4. Review the diff (`git diff`) before committing — the generators
   overwrite `papers.csv`, `index.html`, `sitemap.xml`, and every
   generated publication page on each run.

The one exception is `publications/adult-human-spinal-cord-nspcs/index.html`
(the original, hand-written page), which the generator does not touch —
its `PAPERS` entry is marked `existing=True` and exists only so it's
included in `papers.csv`. Keep its bibliographic data in sync with
`papers_data.py` by hand if it ever changes.
