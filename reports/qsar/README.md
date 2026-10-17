# OECD QSAR Toolbox supporting reports

The supplied project reports identify **OECD QSAR Toolbox**; two mention version **4.9**. Six original DOCX reports are preserved byte-for-byte, including their embedded chemical depiction screenshots. UTF-8 transcriptions make the contents searchable on GitHub; the extracted PNGs show the original tool depictions. `source-manifest.json` records original filenames and SHA-256 hashes.

These are project-prepared summaries combining Toolbox records/profilers and cited literature. They are not native Toolbox project/database exports, fresh model runs, or a newly trained QSAR model. No native Toolbox workspace or profiler export was found in the supplied report set. The screenshots show chemical depictions, not complete endpoint or profiler audit trails.

## Scope and provenance

| Report | Role in this repository |
|---|---|
| [Formaldehyde](Formaldehyde.docx) | Main chemical; reported Toolbox aquatic-toxicity record and mechanistic profiler context |
| [Ethanol](Ethanol.docx) | Supplementary chemical comparison; reported Toolbox record/profilers |
| [Sodium benzoate](Sodium-Benzoate.docx) | Supplementary comparison; reported Toolbox record/profilers |
| [Monosodium glutamate](Monosodium-Glutamate.docx) | Supplementary comparison; literature-derived endpoints |
| [Erythrosine B](Erythrosine-B.docx) | Supplementary comparison; literature context without a verified numerical LC50 in the supplied report |
| [Sunset Yellow](Sunset-Yellow.docx) | Supplementary comparison; literature-derived endpoints |

Only the formaldehyde adult-fish observations are analyzed by `analyze.py`. The other reports do not establish that this project performed experiments on those chemicals. Exposure durations, life stages and units differ; reported endpoints must not be ranked as a controlled comparative experiment.

## Known source inconsistencies

- The formaldehyde report identification section and embedded depiction use CAS **50-00-0**, but its toxicity table prints **67-47-0**. Treat the latter as an unresolved transcription error; recheck the original Toolbox record before reusing the table.
- The sodium benzoate report prints a SMILES beginning `CC1=...`, while its embedded depiction shows an unsubstituted benzoate ring. The identifier should be rechecked against the original chemical record before any computational reuse.
- The MSG report combines CAS 142-47-2 with hydrated formula/mass/SMILES fields. Salt/hydration conventions should be reconciled before descriptor calculations.
- The formaldehyde report's selected profilers say “No alert found.” This records those particular profiler outputs only; it is not evidence of absence of carcinogenicity or genotoxicity.

The source documents remain unchanged so their provenance can be inspected. Their cited database/literature values have not all been independently revalidated for this release. There is no claim that the reported 41 mg/L database endpoint was predicted by this repository's Python code.

## Computational contribution

This repository connects documented chemical identity and mechanistic profiling context with a reproducible Python analysis of transcribed mortality counts: input validation, Abbott correction, log-concentration/probit interpolation, endpoint sensitivity, machine-readable JSON and an SVG plot. Tool-assisted profiling and numerical analysis are distinct parts of the work.
