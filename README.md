# Cradle-to-gate screening reassessment of a packaged 1 L electric kettle

> **Result status:** screening arithmetic only. The foreground inventory is incomplete, TianGong/USLCI providers are not linked into a kettle product system, and the proxy factors do not form a harmonized LCIA method. This is **not a complete LCA** and the total below must not be described as a characterized GWP100 result.

## 1. Study identity and purpose

- **Study title:** Cradle-to-gate screening reassessment of one packaged 1 L electric kettle.
- **Public student/group alias:** Unknown; not supplied. Full name and email are intentionally omitted.
- **Repository:** [mgchoe-dotcom/kettle_LCA_2nd](https://github.com/mgchoe-dotcom/kettle_LCA_2nd).
- **Run identifier:** `rerun-20261008-01`.
- **Study date:** 2026-10-08.
- **Goal:** re-evaluate the supplied BOM, inspect available dataset matches and make the arithmetic reproducible while preserving the prior submission.
- **Intended comparison:** comparison with the preserved screening result at prior commit `87fda697d865538a830693baae80da810c7cd5d0`; no product alternatives were compared.
- **Run type/tag:** separate reassessment run; no Git tag. The final commit SHA is intentionally not embedded here; use the repository's final commit when submitting the course form.

## 2. Product, declared unit and system boundary

- **Declared unit / functional unit:** one manufactured and packaged BC1 representative 1 L plastic electric kettle at the factory gate.
- **Specifications:** nominal 1 L capacity; the BOM describes a plastic electric kettle. Detailed model, rated power, dimensions, component allocation, and manufacturer are unknown.
- **BOM source/date/path:** material quantities supplied directly in the user prompt on 2026-10-08; machine-readable transcription is [`data/bom.csv`](data/bom.csv). No external BOM source document or revision was supplied in this run.
- **Mass check:** kettle materials = **723.00 g**; packaging = **137.80 g**; packaged unit = **860.80 g**. The calculation script recomputes and asserts these values.
- **Intended included stages:** raw-material extraction and production; material conversion/component manufacturing; kettle assembly; packaging manufacture and packing; inbound transport to the factory.
- **Actually quantified:** BOM mass multiplied by preserved, heterogeneous external screening factors, plus one assumed aggregate electricity input. This does not quantify all intended stages.
- **Excluded:** customer delivery, product use, and end-of-life. No use-phase or end-of-life extension is included.
- **Cut-offs:** no formal cut-off rule; no BOM item was removed. Missing stages are unresolved, not zero.
- **Geography/reference year:** product factory and suppliers are unknown. Proxy geographies span China, Germany, Japan, Europe, and the United States, with non-uniform reference years. There is no common reference year.

## 3. Foreground inventory and quantitative assumptions

The BOM rows are finished product masses, not measured factory purchases. No yield adjustment is available; the screening arithmetic temporarily treats finished mass as purchased mass (equivalent to 100% yield). This is an assumption, not a measured production yield. Gram values are converted to kilograms by dividing by 1,000.

| Input/parameter | Value | Unit | Evidence/source and status |
|---|---:|---|---|
| Stainless steel | 186 | g/unit | User BOM; sourced quantity, grade/form unknown |
| Brass | 20.25 | g/unit | User BOM; sourced quantity, alloy unknown |
| Copper | 15 | g/unit | User BOM; sourced quantity, grade/form unknown |
| PP | 350.25 | g/unit | User BOM; sourced quantity, resin grade/recycled content unknown |
| PVC | 43.5 | g/unit | User BOM; sourced quantity, formulation/recycled content unknown |
| Nylon | 49.5 | g/unit | User BOM; sourced quantity, grade unspecified |
| POM | 9.75 | g/unit | User BOM; sourced quantity, grade/recycled content unknown |
| PC | 6.75 | g/unit | User BOM; sourced quantity, grade/additives unknown |
| ABS | 30 | g/unit | User BOM; sourced quantity, grade/recycled content unknown |
| Silicone | 12 | g/unit | User BOM; sourced quantity, cure/formulation unknown |
| LDPE packaging foil | 6.3 | g/unit | User BOM; film specification unknown |
| Cardboard packaging | 131.5 | g/unit | User BOM; board construction/recycled content unknown |
| Conversion, assembly, packing electricity | 0.50 | kWh/unit | Assumed aggregate placeholder; no factory data |
| Electricity factor | 0.5366 | kg CO2/kWh | Carried-forward China 2022 national-average operational CO2 factor; not a lifecycle LCIA factor |
| Yield/loss | 100% assumed | ratio | No measurement; feed mass treated as BOM mass; scrap omitted |
| Inbound transport | Unknown | tonne-km | Supplier locations, modes and distances unavailable; not calculated |
| Process heat, water, line energy | Unknown | per unit | No process data; not calculated |
| Scrap/recycling/credits | Unknown | kg and allocation rule | No scrap quantities or destinations; not calculated; no credits |
| Prices/monetary proxies | Not applicable | — | No monetary proxy used |

The factor basis is recorded in [`data/screening_factors.csv`](data/screening_factors.csv). Upstream resin factors are cumulative resin-production proxies, so adding their upstream energy again would double count. The PC proxy is for solid sheet and includes sheet processing; adding a separate equivalent PC sheet-conversion burden risks double counting. The aggregate electricity placeholder must be removed/replaced if selected process datasets already include the same electricity. No actual conversion-process inventory is available.

## 4. Background data and matching decisions

See [`data/dataset_mapping.csv`](data/dataset_mapping.csv) for the searchable mapping of database/release, dataset name, UUID/version where exposed, geography, year, reference flow, source URL, access date, and match decision. [`data/tiangong_candidates.csv`](data/tiangong_candidates.csv) preserves the earlier TianGong candidate log. [`data/screening_factors.csv`](data/screening_factors.csv) records the numerical external proxy factors. File hashes for remote sources were not captured.

- **TianGong:** public catalog candidates include a 304 stainless billet process, refined copper process, PP and PVC processes, an LDPE resin process, and corrugated-cardboard production. Candidate UUIDs/versions and metadata as present in the previous submission's mapping are retained in the linked table. They were not promoted to providers: billet is not the kettle's sheet/formed stock; copper component form is unconfirmed; PP/PVC route, year, and/or waste boundary need review; LDPE resin does not cover foil conversion; cardboard board type/recycled content is unverified. The brass record is a product-flow record, not a production LCI process. Search was by material names and synonyms in the public TianGong catalog; exact query exports were not retained. Search date recorded: 2026-10-08.
- **USLCI:** the supplied `release-downloads.md` was reviewed as a release/download index only, not as a database package. It lists release **1.2026-09.0**. Public LCA Commons search found the PVC virgin-resin process UUID `3dbccdda-2014-4239-ad1f-4e15c034942b` (U.S.; primary data collected in 2015; 1 kg resin; gate-to-gate). It is a candidate, not a closed cradle-to-gate provider: upstream VCM/EDC supply must be connected and the kettle PVC compound match is unresolved. A stainless 304 flat-rolled-coil record is a candidate, but reference flow and full scope require inspection. PP, PC, and corrugated-product exchanges surfaced inside scanner-manufacturing processes; those exchanges are not independent production providers. No downloaded database or complete JSON-LD package was imported, and the public search was not exhaustive.
- **External proxies used numerically:** stainless steel (China); brass CuZn20 (Germany); copper (China); PP/PVC/LDPE resins (Japan); grouped nylon/POM/ABS and RTV-1 silicone (Europe); PC solid sheet (Europe); corrugated board (U.S.). These are cumulative published factors, not unit-process inventories selected from TianGong/USLCI. Their scopes, methods, geography, and reference years differ. Source URLs and stated bases are in [`data/screening_factors.csv`](data/screening_factors.csv).
- **Supplier links/external dependencies:** none confirmed. Dataset candidates are not connected to actual kettle suppliers or to a factory location. No monetary estimate was used.

Public catalog starting points: [TianGong LCA database](https://www.tiangong.earth/en/lca-database), [TianGong repositories](https://github.com/tiangong-lca), [USLCI on LCA Commons](https://www.lcacommons.gov/lca-collaboration/National_Renewable_Energy_Laboratory/USLCI_Database_Public/datasets), and [USLCI PVC process](https://lcacommons.gov/lca-collaboration/National_Renewable_Energy_Laboratory/USLCI_Database_Public/dataset/PROCESS/3dbccdda-2014-4239-ad1f-4e15c034942b). Retrieval date: 2026-10-08.

## 5. Calculation and impact-assessment methods

- **Actual calculation:** `mass_kg[i] = BOM_g[i] / 1000`; `material_screening[i] = mass_kg[i] × external_factor[i]`; `screening_total = Σ material_screening[i] + assumed_kWh × operational_CO2_factor`. This is transparent factor multiplication, not a solved process network.
- **Matrix representation:** no technosphere matrix `A`, scaling vector `s`, elementary-flow inventory `g = B s`, or characterization `h = C g` was built. The scalar factor arithmetic is the actual equivalent used.
- **Software/solver:** Python 3.12.14 standard library; no LCA solver or database engine. No process scaling or provider-linking algorithm was applied.
- **System model/allocation:** not modeled for the kettle. No allocation or recycling credit is calculated. The brass proxy contains its source dataset's secondary-content assumptions; other source proxy contents are inherited and not harmonized.
- **Impact assessment:** no formal characterization method/version or time horizon was applied. Factors report mixed GHG, CO2-e, GWP-total or CO2-only metrics; they cannot be treated as a consistent GWP100 method. There is no characterized elementary-flow inventory or flow-mapping table.
- **Biogenic carbon:** the cardboard proxy excludes biogenic CO2; other biogenic flows are not characterized.
- **Unresolved providers/flows:** all material-provider connections, foreground manufacturing and transport processes, and elementary-flow characterizations remain unresolved. Missing suppliers and uncharacterized flows are not assigned zero.

## 6. How to reproduce the analysis

Repository file map:

- [`data/bom.csv`](data/bom.csv): supplied 12-row BOM.
- [`data/dataset_mapping.csv`](data/dataset_mapping.csv): candidate and matching decisions.
- [`data/tiangong_candidates.csv`](data/tiangong_candidates.csv): preserved TianGong mapping from prior work.
- [`data/screening_factors.csv`](data/screening_factors.csv): external factors used in the arithmetic.
- [`data/assumptions.csv`](data/assumptions.csv): parameter assumptions and gaps.
- [`src/calculate.py`](src/calculate.py): reproducible calculation and mass assertions.
- [`runs/rerun-20261008-01_summary.json`](runs/rerun-20261008-01_summary.json): machine-readable run summary.
- [`runs/rerun-20261008-01_contributions.csv`](runs/rerun-20261008-01_contributions.csv): per-material contributions.
- [`runs/rerun-20261008-01_sensitivity.csv`](runs/rerun-20261008-01_sensitivity.csv): deterministic electricity scenarios.
- [`runs/prior/`](runs/prior/): unchanged artifacts from the previous commit.
- [`logs/decision-log.md`](logs/decision-log.md): prompt and modeling decision summary.

**Runtime:** Python 3.12.14, standard library only; no third-party dependencies, seed, account, or API key. No operating system-specific data package is needed for the arithmetic. Exact command executed in the Codex workspace (from the workspace root) was:

```powershell
& 'C:\Users\DB_MSE\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' work/kettle_LCA_2nd/src/calculate.py
```

For a clone of this repository, from its root, run:

```powershell
python src/calculate.py
```

Expected generated paths are `runs/rerun-20261008-01_summary.json`, `runs/rerun-20261008-01_contributions.csv`, and `runs/rerun-20261008-01_sensitivity.csv`. The script overwrites those three files for this fixed run ID when rerun; preserve/copy them before changing factors or assumptions. No database retrieval command is supplied because no package was downloaded. Manual work remains to retrieve the selected release, inspect process datasets, verify permissions/versions, establish supplier links, and close inventory and LCIA. No report viewer/tool is applicable; results are CSV/JSON/Markdown files.

## 7. Results, checks and interpretation

**Status:** screening scenario only. The result is not a GWP100 total; it is heterogeneous proxy arithmetic with an operational CO2 electricity term.

- Material-proxy subtotal: **1.9717913589 kg CO2e per packaged kettle**.
- Assumed electricity: **0.268300 kg CO2 per kettle**.
- Screening arithmetic total: **2.2400913589 kg CO2e per packaged kettle**.

| Contribution | kg CO2e/unit | Interpretation |
|---|---:|---|
| PP | 0.657979 | external Japan resin proxy |
| Assumed aggregate electricity | 0.268300 | 0.50 kWh × 0.5366 kg operational CO2/kWh |
| Nylon | 0.368775 | grouped PA6/PA66 European proxy |
| Stainless steel | 0.327360 | Chinese production-average proxy |
| Cardboard packaging | 0.157800 | U.S. corrugated board proxy; biogenic CO2 excluded |
| ABS | 0.115200 | grouped European ABS/ASA/PS proxy |
| Copper | 0.088200 | Chinese route-mix proxy |
| PVC | 0.088168 | Japanese resin proxy |
| Silicone | 0.069480 | European virgin RTV-1 sealant proxy; kettle grade unconfirmed |
| POM | 0.030713 | grouped POM/PBT European proxy |
| Brass | 0.028654 | German CuZn20 proxy |
| PC | 0.026325 | European solid-sheet proxy; conversion may be embedded |
| LDPE foil | 0.013138 | Japanese resin only; film conversion absent |

The three largest individual terms are PP, nylon, and stainless steel. Assumed aggregate electricity ranks fourth. Their ranking is conditional on selected proxies and the assumed electricity. The full unrounded breakdown is linked in [`runs/rerun-20261008-01_contributions.csv`](runs/rerun-20261008-01_contributions.csv).

**Checks:** BOM row count 12 and mass assertions pass (723.00 g kettle, 137.80 g packaging, 860.80 g total). The material contribution sum is 1.9717913589 kg CO2e; adding 0.268300 kg operational CO2 gives 2.2400913589, subject to floating point rounding. Supplier closure fails/not available because no providers are linked. Contribution sum is internally arithmetically consistent, but it is not a closed LCA inventory. Double counting remains a risk between PC sheet conversion and any future foreground conversion, and between aggregate electricity and process datasets containing electricity. Unquantified manufacturing, transport, scrap and characterization contributions are omitted, not zero. These values do not support a product-comparison, regulatory, or complete-footprint claim.

## 8. Uncertainty and sensitivity

No probabilistic uncertainty analysis was calculated: no source-specific distributions, correlations, or complete linked model are available. Mean, median, P05/P95, a conditional central 90% interval, simulation draw count, seed, and convergence checks are therefore **not calculated**. The electricity-only scenarios are deterministic sensitivity cases, not probability intervals or method/provider scenarios:

| Assumed aggregate electricity | Screening arithmetic total (kg CO2e/unit) |
|---:|---:|
| 0 kWh | 1.971791 |
| 0.25 kWh | 2.105941 |
| 0.50 kWh (central assumption) | 2.240091 |
| 1.00 kWh | 2.508391 |

See [`runs/rerun-20261008-01_sensitivity.csv`](runs/rerun-20261008-01_sensitivity.csv). No provider/method scenario or repeated-AI-run variability was modeled. The scenario range is conditional on fixed proxy factors and the stated electricity factor.

## 9. Codex and human decisions

- **Codex model/version:** GPT-6 as displayed by the task environment; exact build unknown. Reasoning setting and full inference settings were not available.
- **Run date:** 2026-10-08; exact start/end times not recorded.
- **Prompt/decision record:** the user requested a separate new-repository cradle-to-gate reassessment, verification of the prior commit, BOM reconciliation, TianGong/USLCI dataset search, explicit unmatched candidates, process and transport gaps, contribution/sensitivity outputs, and preservation under a new run ID. A curated summary is in [`logs/decision-log.md`](logs/decision-log.md); private messages and credentials are not included.
- **Human-provided decisions:** functional unit, intended system boundary, BOM quantities, new repository URL, and prior baseline commit were provided by the user. Manufacturing region, suppliers, material grades, yields, transport, and LCIA method remain unknown; no human-confirmed dataset match was provided.
- **Modeling choices:** retain legacy screening factors only to make a transparent comparable arithmetic run; assume 0.50 kWh/unit as a placeholder and show deterministic sensitivity; do not promote process or flow candidates when product form, route, or provider linkage is unresolved.
- **Accepted/rejected matches:** no TianGong/USLCI process is accepted as a provider. Candidates and rejection reasons are recorded in `data/dataset_mapping.csv`.
- **Edits/checks:** BOM transcription, script creation, and rerun arithmetic; BOM mass assertions and contribution sum independently reviewed against CSV outputs. No independent LCA solver output exists.
- **Assistance:** public web/catalog search and local Python standard-library arithmetic. No private source files, contacts, or credentials are included.

## 10. Independent and revised runs

The prior submission is preserved under [`runs/prior/`](runs/prior/) from commit `87fda697d865538a830693baae80da810c7cd5d0`. Inspection of that commit found only README and result/mapping/factor CSV/text artifacts; its README refers to `src/calculate.py`, `data/bom.csv`, and a decision log, but those files were not present in the commit. The old tracked outputs are retained unchanged in this repository.

| Run | Basis | Recorded/computed total | Difference |
|---|---|---:|---:|
| Prior baseline at `87fda697d865538a830693baae80da810c7cd5d0` | Heterogeneous proxy arithmetic, 0.50 kWh assumed | 2.2400913589 kg CO2e/unit | — |
| `rerun-20261008-01` | BOM transcribed and recalculated with the preserved proxy factor table and same 0.50 kWh assumption | 2.2400913589 kg CO2e/unit | 0.0000000000 kg CO2e/unit; 0.00% |

No impact-factor/provider or LCIA-method decision changed, so the result is a reproducible arithmetic rerun, not a revised impact model. The new work adds an executable script, BOM, explicit run outputs, assumptions, and USLCI candidate notes; the numeric total remains unchanged because the newly researched candidates were not sufficiently matched to replace any factor. Predicted numerical effect of the added documentation/reproducibility is zero. No independent run, tag, or alternate scenario using linked process databases is available.

## Unresolved information to review

1. Confirm public student/group alias if one should be shown; full name and email remain for the course form only.
2. Supply the actual factory geography/reference year, product model/specifications, component grade/form and recycled content.
3. Provide suppliers/routes, incoming transport, conversion/assembly/packing energy and materials, yield/scrap and scrap treatment.
4. Confirm which database release(s) and LCIA method/version the course expects; download/import the appropriate USLCI/TianGong data and verify exact provider links and elementary-flow characterization.
5. Decide whether the course permits the clearly limited proxy arithmetic to be submitted as a screening exercise; it is not a complete LCA or GWP100 result.
