#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared publication data for scripts/generate_pages.py and scripts/generate_homepage.py.

This is the single source of truth used to (re)generate papers.csv, every
publications/<slug>/index.html page, index.html, and sitemap.xml. To add a
new publication: verify it against a primary source (see CLAUDE.md), add a
new dict to PAPERS below, then run both generator scripts from the repo
root:

    python3 scripts/generate_pages.py
    python3 scripts/generate_homepage.py
"""

SITE = "https://sasijagadeesan.github.io"
ORCID = "0000-0003-3977-5367"


PAPERS = [
    # 1
    dict(
        slug="adult-human-spinal-cord-nspcs",
        title="Transcriptomic and Functional Landscape of Adult Human Spinal Cord NSPCs Compared to iPSC-Derived Neural Progenitor Cells",
        authors_full=["Sasi Kumar Jagadeesan", "Ahmad Galuta", "Ryan Vimukthie Sandarage", "Eve Chung Tsai"],
        authors_citation="Jagadeesan SK, Galuta A, Sandarage RV, Tsai EC",
        role_note="First author",
        journal="Cells", year="2025", volume="14", issue="2", pages="64",
        pub_date="2025-01-07",
        doi="10.3390/cells14020064", pmid="39851491", pmcid="PMC11763936",
        publisher_url="https://www.mdpi.com/2073-4409/14/2/64",
        oa="Yes (MDPI, open access)", pub_type="Original research",
        primary_category="Human Spinal Cord Biology & Regenerative Neuroscience",
        secondary_categories=["Neurosurgery & Clinical / Translational Research"],
        overview=[
            "This study directly compared bona fide neural stem/progenitor cells isolated from the adult human spinal cord with syngeneic induced pluripotent stem cell-derived neural progenitor populations regionalized toward either spinal cord or forebrain identities.",
            "RNA sequencing and functional differentiation assays were used to determine how closely engineered iPSC-derived neural progenitors reproduce the transcriptomic and neurogenic properties of primary adult human spinal cord NSPCs.",
        ],
        findings=[
            "iPSC-derived neural progenitor populations were molecularly distinct from bona fide adult human spinal cord NSPCs.",
            "Forebrain-patterned iPSC-derived NSPCs showed greater similarity to bona fide spinal cord NSPCs in pathways related to neurogenesis, axon guidance, synaptic signaling, and neuronal differentiation.",
            "Spinal cord-patterned iPSC-derived NSPCs showed greater heterogeneity, suboptimal regional specification, and enrichment of neural crest- and immune-associated transcriptional programs.",
            "Functional differentiation assays supported the transcriptomic findings, with stronger neurogenic potential observed in the forebrain-patterned iPSC-derived population.",
            "Donor-specific biological variation influenced how closely iPSC-derived NSPCs aligned with primary spinal cord NSPCs.",
        ],
        why_matters="The study provides a direct human benchmark for evaluating whether iPSC-derived neural progenitors faithfully reproduce the biology of primary adult human spinal cord progenitor populations. The findings are relevant to spinal cord injury, regenerative medicine, autologous cell therapy, neural progenitor engineering, and the interpretation of donor-specific variability in human neural cell models.",
        questions=[
            "How similar are iPSC-derived neural progenitor cells to bona fide adult human spinal cord NSPCs?",
            "Do spinal cord-patterned iPSC-derived progenitors accurately reproduce primary adult spinal cord progenitor biology?",
            "How does donor variability influence neural progenitor transcriptomic identity and differentiation?",
            "What transcriptomic pathways distinguish primary spinal cord NSPCs from engineered iPSC-derived neural progenitors?",
            "Which human cell populations provide the most biologically relevant benchmark for regenerative spinal cord research?",
        ],
        topics=["Adult human spinal cord", "Neural stem/progenitor cells", "NSPCs", "iPSC", "Neural progenitor cells",
                "Spinal cord injury", "Regenerative medicine", "Transcriptomics", "RNA sequencing", "Neurogenesis",
                "Axon guidance", "Neural differentiation", "Donor variability", "Patient-specific variability",
                "Autologous cell therapy", "Syngeneic comparison"],
    ),
    # 2
    dict(
        slug="personalized-stem-cell-regeneration-spinal-cord-injury",
        title="Personalized Stem Cell-Based Regeneration in Spinal Cord Injury Care",
        authors_full=["Sasi Kumar Jagadeesan", "Ryan Vimukthie Sandarage", "Sathya Mathiyalagan", "Eve Chung Tsai"],
        authors_citation="Jagadeesan SK, Sandarage RV, Mathiyalagan S, Tsai EC",
        role_note="First author",
        journal="International Journal of Molecular Sciences", year="2025", volume="26", issue="8", pages="3874",
        pub_date="2025-04-19",
        doi="10.3390/ijms26083874", pmid="40332538", pmcid="PMC12028285",
        publisher_url="https://www.mdpi.com/1422-0067/26/8/3874",
        oa="Yes (MDPI, open access)", pub_type="Review article",
        primary_category="Human Spinal Cord Biology & Regenerative Neuroscience",
        secondary_categories=["Neurosurgery & Clinical / Translational Research"],
        overview=[
            "This review examines advances in stem cell engineering and regenerative approaches for spinal cord injury (SCI), focusing on transplantation of neural stem/progenitor cells (NSPCs), induced pluripotent stem cells (iPSCs), and mesenchymal stem cells (MSCs)."
        ],
        findings_heading="Key Points Covered",
        findings=[
            "Patient-specific factors, including cellular senescence, genetic and epigenetic variability, injury microenvironment, and comorbidities, influence the efficacy of stem cell therapies by affecting graft survival and differentiation.",
            "The review synthesizes literature on NSPC-, iPSC-, and MSC-based approaches to spinal cord repair.",
            "Translational and clinical challenges facing personalized, stem cell-based regeneration for SCI are discussed.",
        ],
        why_matters="Understanding patient-specific variability is relevant to designing more individualized stem cell therapies for spinal cord injury, and to interpreting why therapeutic efficacy varies across patients.",
        questions=[
            "What patient-specific factors most influence stem cell graft survival after spinal cord injury?",
            "How can personalized approaches improve regenerative outcomes for spinal cord injury patients?",
        ],
        topics=["Spinal cord injury", "Stem cell therapy", "Neural stem/progenitor cells", "iPSC-derived neural progenitors",
                "Mesenchymal stem cells", "Personalized regenerative medicine", "Graft survival"],
    ),
    # 3
    dict(
        slug="patient-specific-interneuron-precision-model",
        title="Rebuilding spinal circuit function after spinal cord injury through a patient-specific interneuron precision model",
        authors_full=["Sasi Kumar Jagadeesan", "Ryan Vimukthie Sandarage", "Eve Chung Tsai"],
        authors_citation="Jagadeesan SK, Sandarage RV, Tsai EC",
        role_note="First author",
        journal="Frontiers in Neuroscience", year="2026", volume="20", issue="", pages="1745993",
        pub_date="2026-06-03",
        doi="10.3389/fnins.2026.1745993", pmid="42318198", pmcid="PMC13272048",
        publisher_url="https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2026.1745993/full",
        oa="Yes, CC BY", pub_type="Hypothesis and Theory",
        primary_category="Human Spinal Cord Biology & Regenerative Neuroscience",
        secondary_categories=["Neurosurgery & Clinical / Translational Research"],
        overview=[
            "This paper reframes spinal cord repair after injury as restoration of interneuron-mediated circuit organization, rather than cellular replacement alone, synthesizing insight into how embryonic patterning programs (Sonic Hedgehog, Wnt, and bone morphogenetic protein gradients) establish interneuron diversity, connectivity, and network symmetry."
        ],
        findings_heading="Key Points Covered",
        findings=[
            "Spinal interneurons are framed as central determinants of functional recovery after spinal cord injury, integrating excitatory and inhibitory inputs that drive locomotor, postural, and autonomic control.",
            "The paper synthesizes how developmental patterning programs establish interneuron diversity and network organization.",
            "The authors propose the Patient-Specific Interneuron Precision Model (PIPM), a feedback-informed conceptual framework linking patient-specific biological states — such as progenitor competence and morphogen sensitivity — to circuit-level recovery strategies.",
        ],
        why_matters="Offers a conceptual framework for thinking about spinal circuit restoration beyond cell replacement alone, relevant to designing future interneuron-targeted regenerative strategies.",
        questions=[
            "How do developmental patterning programs inform strategies for restoring spinal interneuron circuitry after injury?",
            "Can patient-specific biological states be used to guide precision regenerative approaches for spinal cord injury?",
        ],
        topics=["Spinal interneurons", "Spinal cord injury", "Circuit reconstruction", "Sonic Hedgehog signaling",
                "Wnt signaling", "BMP signaling", "Regenerative neuroscience", "Precision medicine framework"],
    ),
    # 4
    dict(
        slug="spinal-cord-donor-procurement-heterogeneity",
        title="Acquisition-Related Heterogeneity in Human Spinal Cord Donors: A 10-Year Organ Donation–Integrated Procurement Cohort for Translational Spinal Cord Injury Research",
        authors_full=["Sasi Kumar Jagadeesan", "Ryan Vimukthie Sandarage", "Eve Chung Tsai"],
        authors_citation="Jagadeesan SK, Sandarage RV, Tsai EC",
        role_note="First author",
        journal="Neurotrauma Reports", year="2026", volume="7", issue="", pages="2689288X261475797",
        pub_date="2026-08-17",
        doi="10.1177/2689288X261475797", pmid="42614516", pmcid="PMC13482055",
        publisher_url="https://journals.sagepub.com/doi/10.1177/2689288X261475797",
        oa="Yes",
        pub_type="Research article / original research",
        primary_category="Neurosurgery & Clinical / Translational Research",
        secondary_categories=["Human Spinal Cord Biology & Regenerative Neuroscience"],
        overview=[
            "This cohort study characterizes an organ donation–integrated adult human spinal cord donor cohort accrued over a decade (2016–2025, N=67 donors) to define acquisition-related variables relevant to interpreting and comparing human neurotrauma datasets."
        ],
        findings=[
            "Longitudinal accrual, donation pathway, cause-of-death distribution, anatomical procurement patterns, and preservation solution usage were characterized across the 67-donor cohort.",
            "An ischemic interval proxy (cross-clamp interval band) was defined and reported.",
            "Clinical and operative documentation was harmonized using predefined, standardized categories with explicit decision rules.",
        ],
        why_matters="Documenting acquisition-related heterogeneity supports more rigorous interpretation and cross-study comparability of human spinal cord tissue research.",
        questions=[
            "How does donor-acquisition heterogeneity affect interpretation of human spinal cord tissue datasets?",
            "What standardized documentation practices improve comparability across procurement cohorts?",
        ],
        topics=["Human spinal cord tissue procurement", "Organ donation", "Donor heterogeneity",
                "Translational spinal cord injury research", "Ischemic interval", "Tissue banking"],
    ),
    # 5
    dict(
        slug="spinal-cord-tissue-procurement-governance",
        title="Governance and Prioritization of Human Spinal Cord Tissue Procurement for Research in an Organ Donation Setting",
        authors_full=["Sasi Kumar Jagadeesan", "Ryan Vimukthie Sandarage", "Eve Chung Tsai"],
        authors_citation="Jagadeesan SK, Sandarage RV, Tsai EC",
        role_note="First author",
        journal="Biopreservation and Biobanking", year="2026", volume="", issue="", pages="",
        pub_date="2026-04-21",
        doi="10.1177/19475535261443118", pmid="42011116", pmcid="",
        publisher_url="https://doi.org/10.1177/19475535261443118",
        oa="Unconfirmed", pub_type="Review",
        primary_category="Neurosurgery & Clinical / Translational Research",
        secondary_categories=["Human Spinal Cord Biology & Regenerative Neuroscience"],
        overview=[
            "This paper describes institutionally implemented governance and prioritization practices for donation-integrated procurement and research banking of human spinal cord tissue within a tertiary academic hospital setting."
        ],
        findings_heading="Key Points Covered",
        findings=[
            "The described approach emphasizes conservative prioritization of clinical donation needs over research procurement.",
            "It maintains strict separation of clinical and research roles, a tiered informed-consent structure, and explicit stopping rules.",
            "Defined governance structures for procurement decision-making are outlined for institutional adoption.",
        ],
        why_matters="Provides a transferable governance model to support ethically and operationally sound human spinal cord tissue procurement for research.",
        questions=[
            "What governance structures best balance clinical donation priorities with research tissue procurement needs?",
            "How can informed-consent and stopping-rule frameworks be structured for donation-integrated tissue research?",
        ],
        topics=["Human tissue procurement governance", "Organ donation ethics", "Research tissue banking",
                "Informed consent", "Spinal cord tissue"],
    ),
    # 6
    dict(
        slug="cervical-spine-pathology-intimate-partner-violence",
        title="Cervical Spine Pathology in the Context of Intimate Partner and Interpersonal Violence: A Case Series and Focused Narrative Review",
        authors_full=["Ryan Vimukthie Sandarage", "Emam Khan", "Sasi Kumar Jagadeesan", "Eve Chung Tsai"],
        authors_citation="Sandarage RV, Khan E, Jagadeesan SK, Tsai EC",
        role_note="Contributing author (3rd of 4 authors); this case series and review was led by Sandarage RV et al.",
        journal="Neurotrauma Reports", year="2026", volume="7", issue="", pages="",
        pub_date="2026-08-21",
        doi="10.1177/2689288x261475301", pmid="42634724", pmcid="PMC13499929",
        publisher_url="https://doi.org/10.1177/2689288x261475301",
        oa="Likely yes (Neurotrauma Reports is an open-access journal); unconfirmed for this article",
        pub_type="Case report / case series (hybrid case series and narrative review)",
        primary_category="Neurosurgery & Clinical / Translational Research",
        secondary_categories=[],
        overview=[
            "This case series and focused narrative review examines cervical spine pathology encountered in the context of intimate partner and interpersonal violence (IPV), noting that IPV-associated spinal injury is less well characterized than traumatic brain injury or hypoxic/anoxic injury after nonfatal strangulation, and that existing spine literature has emphasized thoracolumbar compression-type fractures rather than cervical spine injuries."
        ],
        findings_heading="Key Points Covered",
        findings=[
            "Presents a case series alongside a focused narrative review of cervical spine injury in the context of IPV and interpersonal violence.",
            "Highlights neurosurgical encounters as clinical touchpoints for identifying and documenting safety concerns.",
            "Proposes that a brief, structured screening-and-referral pathway may help neurosurgical teams recognize IPV-associated neurotrauma.",
        ],
        why_matters="Raises awareness of an under-recognized pattern of neurotrauma and proposes a practical screening pathway for neurosurgical practice.",
        questions=[
            "How can neurosurgical teams better recognize IPV-associated cervical spine injury?",
            "What screening and referral pathways are feasible in neurosurgical practice for IPV-related neurotrauma?",
        ],
        topics=["Intimate partner violence", "Cervical spine injury", "Neurotrauma", "Case series",
                "Screening and referral", "Neurosurgery"],
    ),
    # 7
    dict(
        slug="ehr-machine-learning-icu-clinical-deterioration",
        title="Development and internal validation of an EHR machine learning model for clinical deterioration in ICU linked inpatients",
        authors_full=["Sasi Jagadeesan", "Pritam Kumar Panda", "Ryan Vimukthie Sandarage", "Eve C. Tsai"],
        authors_citation="Jagadeesan S, Panda PK, Sandarage RV, Tsai EC",
        role_note="First author",
        journal="Scientific Reports", year="2026", volume="", issue="", pages="",
        pub_date="2026-09-17",
        doi="10.1038/s41598-026-71682-0", pmid="", pmcid="",
        publisher_url="https://www.nature.com/articles/s41598-026-71682-0",
        oa="Yes, CC BY 4.0", pub_type="Original research",
        primary_category="Clinical Machine Learning & Predictive Medicine",
        secondary_categories=[],
        overview=[
            "Early warning scores for inpatient deterioration rely predominantly on contemporaneous vital signs and may not incorporate broader electronic health record (EHR) information. This study developed and internally validated a multi-domain EHR machine-learning model using MIMIC-IV v3.1, generating 1,334,773 monitoring windows from 80,442 ICU-linked admissions via a 6-hour sliding-window framework.",
            "The composite outcome was ICU transfer, invasive mechanical ventilation, or in-hospital mortality within 24 hours, with a prevalence of 1.96%.",
        ],
        findings=[
            "XGBoost achieved AUROC 0.758 for the composite 24-hour deterioration outcome.",
            "Comparator early warning scores performed substantially lower: modified NEWS2 AUROC 0.568, qSOFA 0.549, Shock Index 0.539, and MEWS 0.533.",
            "Vital signs were the dominant predictive domain; multi-domain EHR integration improved AUROC by 0.041 over a vitals-only model.",
            "At 90% sensitivity, the model generated 2.51 alerts per monitored patient-day with a positive predictive value of 2.8%.",
            "After collapsing contiguous alerts into episodes, the model produced 0.52 alert episodes per patient-day, with 96.9% event-level sensitivity and episode-level precision of 5.1%.",
            "The authors state that external validation and prospective operational evaluation are required before clinical use.",
        ],
        why_matters="Demonstrates that a multi-domain EHR machine-learning model can substantially outperform conventional bedside early warning scores (NEWS2, qSOFA, Shock Index, MEWS) for predicting short-term clinical deterioration in ICU-linked inpatients, while also quantifying the alert burden such a model would generate in practice.",
        questions=[
            "How much does incorporating multi-domain EHR data, beyond vital signs alone, improve prediction of clinical deterioration?",
            "How does a machine-learning model's AUROC translate into practical alert burden (alerts per patient-day, precision) at clinically relevant sensitivity thresholds?",
            "What external validation and prospective evaluation steps are needed before such a model could be used clinically?",
        ],
        topics=["Clinical machine learning", "Electronic health records", "MIMIC-IV", "XGBoost",
                "Clinical deterioration", "Early warning scores", "NEWS2", "qSOFA", "Shock Index", "MEWS"],
        extra_note="External validation and prospective operational evaluation are required before clinical use; this model has not been validated outside the MIMIC-IV internal validation described in the paper.",
    ),
    # 8
    dict(
        slug="pex11-rim20-lithium-chloride-pgm2-translation",
        title="Lithium Chloride Sensitivity Connects the Activity of PEX11 and RIM20 to the Translation of PGM2 and Other mRNAs with Structured 5′-UTRs",
        authors_full=["Sasi Kumar Jagadeesan", "Mustafa Al-Gafari", "Maryam Hajikarimlou", "Sarah Takallou",
                      "Houman Moteshareie", "Azam Tayabali", "Bahram Samanfar", "Myron Smith", "Ashkan Golshani"],
        authors_citation="Jagadeesan SK, Al-Gafari M, Hajikarimlou M, Takallou S, Moteshareie H, Tayabali A, Samanfar B, Smith M, Golshani A",
        role_note="First author",
        journal="Molecular and Cellular Biochemistry", year="2022", volume="477", issue="11", pages="2643–2656",
        pub_date="2022",
        doi="10.1007/s11010-022-04466-5", pmid="35598219", pmcid="",
        publisher_url="https://link.springer.com/article/10.1007/s11010-022-04466-5",
        oa="Unconfirmed", pub_type="Original research",
        primary_category="Yeast Genetics & Cellular Stress Biology",
        secondary_categories=["Molecular Genetics & Functional Genomics"],
        overview=[
            "This study investigated genes involved in yeast sensitivity to lithium chloride (LiCl), focusing on PEX11 and RIM20 and their role in regulating translation of PGM2 and other mRNAs with structured 5′-untranslated regions (UTRs)."
        ],
        findings=[
            "Deletion of PEX11 or RIM20 increases yeast LiCl sensitivity.",
            "PEX11 and RIM20 regulate PGM2 mRNA expression at the level of translation.",
            "The observed effect on translation appears to target the structured 5′-UTR of PGM2 mRNA.",
        ],
        why_matters="Contributes to understanding of translational control mechanisms and gene functions relevant to cellular stress responses in yeast.",
        questions=[
            "How do PEX11 and RIM20 influence translation of structured mRNAs?",
            "What role does the PGM2 5′-UTR play in LiCl-sensitivity phenotypes?",
        ],
        topics=["Saccharomyces cerevisiae", "Lithium chloride sensitivity", "PGM2", "Structured 5′-UTRs",
                "Translational regulation", "Functional genomics"],
        pmcid_note="PMCID not independently verified; a candidate ID surfaced in search was confirmed to belong to a different paper and is deliberately omitted.",
    ),
    # 9
    dict(
        slug="dbp7-yrf1-6-licl-pgm2-translation",
        title="DBP7 and YRF1-6 Are Involved in Cell Sensitivity to LiCl by Regulating the Translation of PGM2 mRNA",
        authors_full=["Sasi Kumar Jagadeesan", "Mustafa Al-gafari", "Jiashu Wang", "Sarah Takallou", "Danielle Allard",
                      "Maryam Hajikarimlou", "Thomas David Daniel Kazmirchuk", "Houman Moteshareie", "Kamaledin B. Said",
                      "Reza Nokhbeh", "Myron Smith", "Bahram Samanfar", "Ashkan Golshani"],
        authors_citation="Jagadeesan SK, Al-gafari M, Wang J, Takallou S, Allard D, Hajikarimlou M, Kazmirchuk TDD, Moteshareie H, Said KB, Nokhbeh R, Smith M, Samanfar B, Golshani A",
        role_note="First author",
        journal="International Journal of Molecular Sciences", year="2023", volume="24", issue="2", pages="1785",
        pub_date="2023-01-16",
        doi="10.3390/ijms24021785", pmid="36675300", pmcid="PMC9864399",
        publisher_url="https://www.mdpi.com/1422-0067/24/2/1785",
        oa="Yes (MDPI, open access)", pub_type="Original research",
        primary_category="Yeast Genetics & Cellular Stress Biology",
        secondary_categories=[],
        overview=[
            "This study identified DBP7 and YRF1-6 as genes involved in yeast cell sensitivity to lithium chloride (LiCl) via regulation of PGM2 mRNA translation."
        ],
        findings=[
            "dbp7Δ and yrf1-6Δ null mutants show increased LiCl sensitivity on galactose-containing media.",
            "DBP7 and YRF1-6 modulate the translational level of PGM2 mRNA.",
            "The effect on translation appears associated with the structured 5′-UTR of PGM2 mRNA.",
        ],
        why_matters="Expands the set of known genes involved in translational regulation of stress-response genes in yeast.",
        questions=[
            "How do DBP7 and YRF1-6 affect PGM2 mRNA translation?",
            "What is the broader role of these genes in the LiCl stress response?",
        ],
        topics=["Saccharomyces cerevisiae", "DBP7", "YRF1-6", "PGM2", "Lithium chloride sensitivity", "mRNA translation"],
    ),
    # 10
    dict(
        slug="dna-damage-repair-genes-yeast",
        title="Discovery and Identification of Genes Involved in DNA Damage Repair in Yeast",
        authors_full=["Sasi Kumar Jagadeesan", "Taylor Potter", "Mustafa Al-Gafari", "Mohsen Hooshyar",
                      "Chamath Minuka Hewapathirana", "Sarah Takallou", "Maryam Hajikarimlou", "Daniel Burnside",
                      "Bahram Samanfar", "Houman Moteshareie", "Myron Smith", "Ashkan Golshani"],
        authors_citation="Jagadeesan SK, Potter T, Al-Gafari M, Hooshyar M, Hewapathirana CM, Takallou S, Hajikarimlou M, Burnside D, Samanfar B, Moteshareie H, Smith M, Golshani A",
        role_note="Co-first author (with Taylor Potter)",
        journal="Gene", year="2022", volume="831", issue="", pages="146549",
        pub_date="2022-07-15",
        doi="10.1016/j.gene.2022.146549", pmid="35569766", pmcid="",
        publisher_url="https://www.sciencedirect.com/science/article/abs/pii/S0378111922003687",
        oa="Unconfirmed", pub_type="Original research",
        primary_category="Molecular Genetics & Functional Genomics",
        secondary_categories=["Yeast Genetics & Cellular Stress Biology"],
        overview=[
            "This study used a computational approach to identify novel yeast gene functions involved in DNA damage repair, focusing on double-strand break (DSB) repair in Saccharomyces cerevisiae."
        ],
        findings=[
            "A computational tool was developed to leverage large-scale yeast interaction data to predict new gene functions.",
            "GAL7, YMR130W, and YHI9 were computationally predicted and experimentally supported as playing a role in DSB repair, despite not having been previously linked to DNA repair pathways.",
        ],
        why_matters="Demonstrates the utility of computational gene-function prediction approaches for expanding knowledge of DNA damage repair networks.",
        questions=[
            "Can computational interaction-network approaches reliably predict novel DNA repair gene functions?",
            "What roles do GAL7, YMR130W, and YHI9 play in double-strand break repair?",
        ],
        topics=["DNA damage repair", "Double-strand breaks", "Saccharomyces cerevisiae", "Functional genomics",
                "Computational gene-function prediction"],
    ),
    # 11
    dict(
        slug="yap1-cox5a-npr3-oxidative-stress-yeast",
        title="Hydrogen peroxide sensitivity connects the activity of COX5A and NPR3 to the regulation of YAP1 expression",
        authors_full=["Sarah Takallou", "Maryam Hajikarimlou", "Mustafa Al-Gafari", "Jiashu Wang", "Sasi Kumar Jagadeesan",
                      "Thomas David Daniel Kazmirchuk", "Houman Moteshareie", "Alex Mulet Indrayanti", "Taha Azad",
                      "Martin Holcik", "Bahram Samanfar", "Myron Smith", "Ashkan Golshani"],
        authors_citation="Takallou S, Hajikarimlou M, Al-Gafari M, Wang J, Jagadeesan SK, Kazmirchuk TDD, Moteshareie H, Indrayanti AM, Azad T, Holcik M, Samanfar B, Smith M, Golshani A",
        role_note="Contributing author (5th of 13 authors); this study was led by Takallou S et al.",
        journal="The FASEB Journal", year="2024", volume="38", issue="5", pages="e23439",
        pub_date="2024",
        doi="10.1096/fj.202300978RR", pmid="38416461", pmcid="",
        publisher_url="https://faseb.onlinelibrary.wiley.com/doi/full/10.1096/fj.202300978RR",
        oa="Unconfirmed (FASEB Journal is generally open access)", pub_type="Original research",
        primary_category="Yeast Genetics & Cellular Stress Biology",
        secondary_categories=[],
        overview=[
            "This study examined regulation of YAP1 expression under oxidative stress, focusing on the roles of COX5A and NPR3 in the yeast hydrogen peroxide stress response."
        ],
        findings=[
            "YAP1 mRNA undergoes IRES-mediated translation in the presence of hydrogen peroxide (H₂O₂).",
            "COX5A and NPR3 facilitate YAP1 translation via the YAP1 IRES, directly or indirectly.",
        ],
        why_matters="Adds to understanding of alternative translation-initiation mechanisms activated during oxidative stress in yeast.",
        questions=[
            "How do COX5A and NPR3 influence IRES-mediated translation of YAP1 under oxidative stress?",
            "What broader role does IRES-mediated translation play in yeast stress responses?",
        ],
        topics=["Oxidative stress", "YAP1", "IRES-mediated translation", "Saccharomyces cerevisiae", "COX5A", "NPR3"],
    ),
    # 12
    dict(
        slug="yap1-nce102-cda2-bcs1-oxidative-stress-yeast",
        title="Oxidative stress-induced YAP1 expression is regulated by NCE102, CDA2, and BCS1",
        authors_full=["Sarah Takallou", "Maryam Hajikarimlou", "Mustafa Al-gafari", "Jiashu Wang", "Sasi Kumar Jagadeesan",
                      "Thomas David Daniel Kazmirchuk", "Christina Arnoczki", "Houman Moteshareie", "Kamaledin B. Said",
                      "Taha Azad", "Martin Holcik", "Bahram Samanfar", "Myron Smith", "Ashkan Golshani"],
        authors_citation="Takallou S, Hajikarimlou M, Al-gafari M, Wang J, Jagadeesan SK, Kazmirchuk TDD, Arnoczki C, Moteshareie H, Said KB, Azad T, Holcik M, Samanfar B, Smith M, Golshani A",
        role_note="Contributing author (5th of 14 authors); this study was led by Takallou S et al.",
        journal="The FEBS Journal", year="2024", volume="291", issue="20", pages="4602–4618",
        pub_date="2024",
        doi="10.1111/febs.17243", pmid="39102301", pmcid="",
        publisher_url="https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.17243",
        oa="Unconfirmed", pub_type="Original research",
        primary_category="Yeast Genetics & Cellular Stress Biology",
        secondary_categories=[],
        overview=[
            "This study investigated regulation of YAP1 expression under oxidative stress, identifying roles for NCE102, CDA2, and BCS1 in the yeast hydrogen peroxide stress response."
        ],
        findings=[
            "Deletion of NCE102, CDA2, or BCS1 increases yeast sensitivity to hydrogen peroxide (H₂O₂).",
            "These genes affect YAP1 expression at the level of translation.",
        ],
        why_matters="Identifies previously undescribed regulators of the oxidative stress response pathway in yeast.",
        questions=[
            "How do NCE102, CDA2, and BCS1 regulate YAP1 translation?",
            "What is their broader role in oxidative-stress tolerance?",
        ],
        topics=["Oxidative stress", "YAP1", "Saccharomyces cerevisiae", "Translational regulation", "NCE102", "CDA2", "BCS1"],
    ),
    # 13
    dict(
        slug="lithium-chloride-sensitivity-yeast-translation-2020",
        title="Lithium Chloride Sensitivity in Yeast and Regulation of Translation",
        authors_full=["Maryam Hajikarimlou", "Kathryn Hunt", "Grace Kirby", "Sarah Takallou", "Sasi Kumar Jagadeesan",
                      "Katayoun Omidi", "Mohsen Hooshyar", "Daniel Burnside", "Houman Moteshareie", "Mohan Babu",
                      "Myron Smith", "Martin Holcik", "Bahram Samanfar", "Ashkan Golshani"],
        authors_citation="Hajikarimlou M, Hunt K, Kirby G, Takallou S, Jagadeesan SK, Omidi K, Hooshyar M, Burnside D, Moteshareie H, Babu M, Smith M, Holcik M, Samanfar B, Golshani A",
        role_note="Contributing author (5th of 14 authors); this study was led by Hajikarimlou M et al.",
        journal="International Journal of Molecular Sciences", year="2020", volume="21", issue="16", pages="5730",
        pub_date="2020-08-10",
        doi="10.3390/ijms21165730", pmid="", pmcid="PMC7461102",
        publisher_url="https://www.mdpi.com/1422-0067/21/16/5730",
        oa="Yes (MDPI, open access)", pub_type="Original research",
        primary_category="Yeast Genetics & Cellular Stress Biology",
        secondary_categories=[],
        overview=[
            "This study examined lithium chloride (LiCl) sensitivity in yeast, identifying NAM7, PUS2, and RPL27B as genes that increase LiCl sensitivity when deleted."
        ],
        findings=[
            "NAM7, PUS2, and RPL27B influence translation and act through the 5′-UTR of PGM2 mRNA to affect LiCl sensitivity.",
        ],
        why_matters="Further characterizes translational control mechanisms underlying LiCl sensitivity in yeast.",
        questions=[
            "How do NAM7, PUS2, and RPL27B affect PGM2 mRNA translation?",
            "What is the collective role of 5′-UTR-mediated translational control in the LiCl stress response?",
        ],
        topics=["Lithium chloride sensitivity", "PGM2", "Saccharomyces cerevisiae", "Translational regulation", "Structured 5′-UTRs"],
    ),
    # 14
    dict(
        slug="yta6-ypr096c-lithium-chloride-translation",
        title="Sensitivity of Yeast to Lithium Chloride Connects the Activity of YTA6 and YPR096C to Translation of Structured mRNAs",
        authors_full=["Maryam Hajikarimlou", "Houman Moteshareie", "Katayoun Omidi", "Mohsen Hooshyar", "Sarah Shaikho",
                      "Thomas Kazmirchuk", "Daniel Burnside", "Sarah Takallou", "Narges Zare", "Sasi Kumar Jagadeesan",
                      "Nathalie Puchacz", "Mohan Babu", "Myron Smith", "Martin Holcik", "Bahram Samanfar", "Ashkan Golshani"],
        authors_citation="Hajikarimlou M, Moteshareie H, Omidi K, Hooshyar M, Shaikho S, Kazmirchuk T, Burnside D, Takallou S, Zare N, Jagadeesan SK, Puchacz N, Babu M, Smith M, Holcik M, Samanfar B, Golshani A",
        role_note="Contributing author (10th of 16 authors); this study was led by Hajikarimlou M et al.",
        journal="PLOS ONE", year="2020", volume="15", issue="7", pages="e0235033",
        pub_date="2020",
        doi="10.1371/journal.pone.0235033", pmid="32639961", pmcid="PMC7343135",
        publisher_url="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0235033",
        oa="Yes (PLOS ONE, open access)", pub_type="Original research",
        primary_category="Yeast Genetics & Cellular Stress Biology",
        secondary_categories=[],
        overview=[
            "This study identified the previously understudied genes YTA6 and YPR096C as involved in yeast sensitivity to lithium chloride (LiCl) when galactose is used as a carbon source."
        ],
        findings=[
            "Deletion of YTA6 or YPR096C increases LiCl sensitivity.",
            "YTA6 encodes a putative ATPase of the CDC48/PAS1/SEC18 (AAA) family; YPR096C encodes a protein of unknown function.",
            "Both genes influence translation of PGM2 mRNA.",
        ],
        why_matters="Expands the known gene network involved in translational regulation of PGM2 and the LiCl stress response.",
        questions=[
            "What are the specific molecular roles of YTA6 and YPR096C in translational regulation?",
            "How does carbon source (galactose vs. glucose) modulate LiCl-sensitivity phenotypes?",
        ],
        topics=["Lithium chloride sensitivity", "YTA6", "YPR096C", "PGM2", "Structured mRNA translation", "Saccharomyces cerevisiae"],
    ),
    # 15
    dict(
        slug="cymoxanil-dihydrofolate-reductase-rna-synthesis",
        title="Cymoxanil Disrupts RNA Synthesis Through Inhibiting the Activity of Dihydrofolate Reductase",
        authors_full=["Thomas David Daniel Kazmirchuk", "Daniel J. Burnside", "Jiashu Wang", "Sasi Kumar Jagadeesan",
                      "Mustafa Al-gafari", "Eshan Silva", "Taylor Potter", "Calvin Bradbury-Jost", "Nishka Beersing Ramessur",
                      "Brittany Ellis", "Sarah Takallou", "Maryam Hajikarimlou", "Houman Moteshareie", "Kamaledin B. Said",
                      "Bahram Samanfar", "Eugene Fletcher", "Ashkan Golshani"],
        authors_citation="Kazmirchuk TDD, Burnside DJ, Wang J, Jagadeesan SK, Al-gafari M, Silva E, Potter T, Bradbury-Jost C, Beersing Ramessur N, Ellis B, Takallou S, Hajikarimlou M, Moteshareie H, Said KB, Samanfar B, Fletcher E, Golshani A",
        role_note="Contributing author (4th of 17 authors); this study was led by Kazmirchuk TDD et al.",
        journal="Scientific Reports", year="2024", volume="14", issue="", pages="11695",
        pub_date="2024-05-22",
        doi="10.1038/s41598-024-62563-5", pmid="38778133", pmcid="PMC11111663",
        publisher_url="https://www.nature.com/articles/s41598-024-62563-5",
        oa="Yes (Scientific Reports, open access)", pub_type="Original research",
        primary_category="Molecular Genetics & Functional Genomics",
        secondary_categories=["Yeast Genetics & Cellular Stress Biology"],
        overview=[
            "This study investigated the mechanism of action of the agricultural fungicide cymoxanil (CMX), used against plant pathogens such as Phytophthora infestans but whose biocidal mechanism was previously unclear."
        ],
        findings=[
            "Using qRT-PCR and expression assays in yeast, the study found that cymoxanil disrupts RNA synthesis.",
            "This effect appears to occur through inhibition of the yeast dihydrofolate reductase (DHFR) enzyme Dfr1, preventing conversion of dihydrofolate to tetrahydrofolate and indirectly inhibiting purine biosynthesis.",
        ],
        why_matters="Clarifies the mode of action of a widely used agricultural fungicide, relevant to understanding its biological effects.",
        questions=[
            "How does cymoxanil inhibit DHFR activity?",
            "What are the downstream consequences of DHFR inhibition for RNA and purine biosynthesis?",
        ],
        topics=["Cymoxanil", "Dihydrofolate reductase", "RNA synthesis", "Saccharomyces cerevisiae", "Fungicide mechanism of action"],
    ),
    # 16
    dict(
        slug="caf20-ecm32-pgm2-translation",
        title="Investigating the Activities of CAF20 and ECM32 in the Regulation of PGM2 mRNA Translation",
        authors_full=["Mustafa Al-Gafari", "Sasi Kumar Jagadeesan", "Thomas David Daniel Kazmirchuk", "Sarah Takallou",
                      "Jiashu Wang", "Maryam Hajikarimlou", "Nishka Beersing Ramessur", "Waleed Darwish",
                      "Calvin Bradbury-Jost", "Houman Moteshareie", "Kamaledin B. Said", "Bahram Samanfar", "Ashkan Golshani"],
        authors_citation="Al-Gafari M, Jagadeesan SK, Kazmirchuk TDD, Takallou S, Wang J, Hajikarimlou M, Beersing Ramessur N, Darwish W, Bradbury-Jost C, Moteshareie H, Said KB, Samanfar B, Golshani A",
        role_note="Contributing author (2nd of 13 authors); this study was led by Al-Gafari M et al.",
        journal="Biology", year="2024", volume="13", issue="11", pages="884",
        pub_date="2024-10-30",
        doi="10.3390/biology13110884", pmid="39596839", pmcid="PMC11592143",
        publisher_url="https://www.mdpi.com/2079-7737/13/11/884",
        oa="Yes (MDPI, open access)", pub_type="Original research",
        primary_category="Yeast Genetics & Cellular Stress Biology",
        secondary_categories=[],
        overview=[
            "This study used computational methods to identify yeast genes influencing translation of structured mRNAs, focusing on CAF20 and ECM32 and their role in regulating PGM2 mRNA translation."
        ],
        findings=[
            "Deletion of CAF20 or ECM32 affects translation of PGM2 and synthetic mRNAs containing structured 5′-untranslated regions.",
        ],
        why_matters="Expands understanding of mechanisms influencing translation of structured mRNAs and their role in gene regulation.",
        questions=[
            "How do CAF20 and ECM32 regulate translation of structured mRNAs?",
            "What is their relationship to other genes implicated in PGM2 translational control?",
        ],
        topics=["CAF20", "ECM32", "PGM2", "Structured mRNA translation", "Saccharomyces cerevisiae", "Functional genomics"],
    ),
    # 17
    dict(
        slug="sars-cov-2-peptide-design-computational",
        title="A Computational Approach to Rapidly Design Peptides That Detect SARS-CoV-2 Surface Protein S",
        authors_full=["Maryam Hajikarimlou", "Mohsen Hooshyar", "Mohamed Taha Moutaoufik", "Khaled A. Aly", "Taha Azad",
                      "Sarah Takallou", "Sasi Kumar Jagadeesan", "Sadhna Phanse", "Kamaledin B. Said", "Bahram Samanfar",
                      "John C. Bell", "Frank Dehne", "Mohan Babu", "Ashkan Golshani"],
        authors_citation="Hajikarimlou M, Hooshyar M, Moutaoufik MT, Aly KA, Azad T, Takallou S, Jagadeesan S, Phanse S, Said KB, Samanfar B, Bell JC, Dehne F, Babu M, Golshani A",
        role_note="Contributing author (7th of 14 authors); this study was led by Hajikarimlou M et al.",
        journal="NAR Genomics and Bioinformatics", year="2022", volume="4", issue="3", pages="lqac058",
        pub_date="2022",
        doi="10.1093/nargab/lqac058", pmid="36004308", pmcid="PMC9394169",
        publisher_url="https://academic.oup.com/nargab/article/4/3/lqac058/6673080",
        oa="Yes (Oxford Academic, open access)", pub_type="Original research",
        primary_category="Molecular Genetics & Functional Genomics",
        secondary_categories=[],
        overview=[
            "This study developed and applied a computational algorithm (InSiPS) to rapidly design peptides that bind and detect the SARS-CoV-2 spike (S) surface protein."
        ],
        findings=[
            "Two sets of peptides designed via the InSiPS method were shown to detect purified SARS-CoV-2 S protein using ELISA and Surface Plasmon Resonance (SPR) approaches.",
        ],
        why_matters="Demonstrates a computational approach for rapid peptide design with potential utility in real-time diagnostic applications for COVID-19.",
        questions=[
            "Can computational peptide-design algorithms like InSiPS be generalized to other viral surface proteins?",
            "How well do computationally designed peptides perform in real-world diagnostic settings?",
        ],
        topics=["SARS-CoV-2", "Computational peptide design", "Spike protein", "ELISA", "Surface plasmon resonance", "Diagnostics"],
    ),
]

def defaulted(p):
    p.setdefault("pmid", "")
    p.setdefault("pmcid", "")
    p.setdefault("volume", "")
    p.setdefault("issue", "")
    p.setdefault("pages", "")
    p.setdefault("secondary_categories", [])
    p.setdefault("overview", [])
    p.setdefault("findings", [])
    p.setdefault("findings_heading", "Key Findings")
    p.setdefault("why_matters", "")
    p.setdefault("questions", [])
    p.setdefault("topics", [])
    p.setdefault("pmcid_note", "")
    p.setdefault("extra_note", "")
    return p

for p in PAPERS:
    defaulted(p)


for p in PAPERS:
    defaulted(p)
