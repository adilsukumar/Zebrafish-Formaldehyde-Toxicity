<!-- ZEBRA_DESIGN_hero_START -->
<p><picture><source media="(max-width: 600px)" srcset="assets/readme/hero-mobile.svg"/><img src="assets/readme/hero.svg" width="100%" alt="Zebrafish Formaldehyde Toxicity. Observe carefully. Interpret with context. Concept illustration."/></picture></p>
<!-- ZEBRA_DESIGN_hero_END -->

# Zebrafish Formaldehyde Toxicity Analysis

Reproducible analysis accompanying an exploratory adult-zebrafish formaldehyde screening report. This public edition keeps transcribed group observations, a small standard-library analysis script and tests; intermediate drafts, template downloads and report-layout experiments are omitted.

<!-- ZEBRA_DESIGN_observations_START -->
<p><picture><source media="(max-width: 600px)" srcset="assets/readme/section-observations-mobile.svg"/><img src="assets/readme/section-observations.svg" width="100%" alt="THE RECORDED GROUPS. The original counts, life stage and exposure context."/></picture></p>
<!-- ZEBRA_DESIGN_observations_END -->

## Recorded observations

| Nominal concentration | Exposed | Deaths after 96 hours | Mortality |
|---|---:|---:|---:|
| Control | 10 | 1 | 10% |
| 40 ppm | 10 | 5 | 50% |
| 100 ppm | 10 | 10 | 100% |

There was one exposure vessel per group. `data/observations.csv` transcribes these recorded group counts; it is not individual-level raw tracking data. Life stage is adult, following the final report. Earlier working drafts used embryo wording and are not included here.

<!-- ZEBRA_DESIGN_reproduce_START -->
<p><picture><source media="(max-width: 600px)" srcset="assets/readme/section-reproduce-mobile.svg"/><img src="assets/readme/section-reproduce.svg" width="100%" alt="A SMALL, REPRODUCIBLE ANALYSIS. Standard-library Python, regression tests and saved outputs."/></picture></p>

<p><picture><source media="(max-width: 600px)" srcset="assets/readme/analysis-mobile.svg"/><img src="assets/readme/analysis.svg" width="100%" alt="Observations, calculation, verification and outputs."/></picture></p>
<!-- ZEBRA_DESIGN_reproduce_END -->

## Reproduce

Python 3.11 or newer; no third-party packages required:

```sh
python analyze.py
python -m unittest discover -s tests -v
```

`results/summary.json` records inputs, assumptions and outputs. `results/mortality.svg` plots the observed mortality. The [supporting OECD QSAR Toolbox reports](reports/qsar/README.md) include six original DOCX reports, searchable transcriptions and embedded tool depictions. They combine reported Toolbox profiling/database records with literature summaries. The unpublished experimental manuscript and intermediate drafts remain separate.

<!-- ZEBRA_DESIGN_method_START -->
<p><picture><source media="(max-width: 600px)" srcset="assets/readme/section-method-mobile.svg"/><img src="assets/readme/section-method.svg" width="100%" alt="METHOD, THEN INTERPRETATION. Correction, endpoint convention and explicit limitations."/></picture></p>

<p><picture><source media="(max-width: 600px)" srcset="assets/readme/context-mobile.svg"/><img src="assets/readme/context.svg" width="100%" alt="Supporting QSAR context with the original scope and limitations preserved."/></picture></p>
<!-- ZEBRA_DESIGN_method_END -->

## Method and interpretation

Abbott correction uses `(exposure mortality - control mortality) / (1 - control mortality)`, giving 44.44% at 40 nominal ppm. The report draws a straight line through two log10-concentration/probit points. Complete mortality is replaced with a finite 97.5% calculation endpoint; the resulting descriptive 50% crossing is approximately **42.51 nominal ppm**. Using 95% instead gives approximately **42.97 nominal ppm**.

This endpoint sensitivity is reported explicitly. Two nonzero concentration groups and no independent vessel replication do not establish a precise population LC50, a confidence interval, embryo sensitivity, or human-health risk. Nominal exposure concentrations were not analytically verified. QSAR structural alerts are chemical context, not confirmation of the mechanism of mortality.

<!-- ZEBRA_DESIGN_map_START -->
<p><picture><source media="(max-width: 600px)" srcset="assets/readme/section-map-mobile.svg"/><img src="assets/readme/section-map.svg" width="100%" alt="FOLLOW THE EVIDENCE. Source observations, calculations, tests and supporting reports."/></picture></p>

<p align="center"><a href="data/observations.csv"><img src="assets/readme/doc-0.svg" width="430" alt="Observations: Transcribed group counts"/></a> <a href="analyze.py"><img src="assets/readme/doc-1.svg" width="430" alt="Analysis source: Correction and descriptive calculation"/></a> <a href="results/summary.json"><img src="assets/readme/doc-2.svg" width="430" alt="Summary output: Recorded inputs, assumptions and outputs"/></a> <a href="reports/qsar/README.md"><img src="assets/readme/doc-3.svg" width="430" alt="QSAR support: Supporting reports and provenance"/></a></p>
<!-- ZEBRA_DESIGN_map_END -->

## Repository map

- `data/observations.csv`: transcribed observations.
- `analyze.py`: validation, correction and descriptive calculation.
- `tests/`: regression checks against the report and invalid inputs.
- `results/`: small, reproducible summary and figure.
- `reports/qsar/`: original supporting reports, chemical depictions, provenance and known source inconsistencies.

Project maintained by Adil Sukumar. Research authorship is as recorded in the original report. No publication, ethics-approval or independent replication claim is added by this repository.


<!-- ZEBRA_DESIGN_closing_START -->
<p><picture><source media="(max-width: 600px)" srcset="assets/readme/closing-mobile.svg"/><img src="assets/readme/closing.svg" width="100%" alt="Keep the observation. Show the reasoning. A clear path back to the evidence."/></picture></p>
<!-- ZEBRA_DESIGN_closing_END -->
