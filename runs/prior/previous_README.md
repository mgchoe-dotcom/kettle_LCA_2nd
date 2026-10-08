# Packaged 1 L Electric Kettle: Cradle-to-Gate Screening LCA

> **Result status:** a reproducible screening estimate was calculated from BOM masses and published proxy factors. It is **not** a complete TianGong/USLCI product-system LCIA: no TianGong provider was accepted, several factors are cross-region proxies, and manufacturing/transport data are incomplete.

## 1. Study identity and purpose

- **Title:** Cradle-to-gate screening LCA of one packaged 1 L electric kettle.
- **Public student/group alias:** Unknown; not supplied.
- **Repository URL / Git remote:** Unknown. The supplied [TianGong GitHub organization](https://github.com/orgs/tiangong-lca/repositories) contains platform/database repositories, but no student analysis repository was identified. This task directory is not a Git repository.
- **Run identifier / tag:** `screening-proxy-2026-10-08`; no tag or commit exists.
- **Study date:** 2026-10-08.
- **Goal:** estimate cradle-to-gate climate impact for the class BC1 representative kettle and document data matching, assumptions and limitations.
- **Intended comparison:** none.
- **Run type:** first local screening run; no preserved independent/revised run is available.
- The classroom brief is available at the supplied [decision lab](https://tiangong-lca-decision-lab.ecodino73.chatgpt.site/). Prompt and modeling decisions are summarized in [`work/decision-log.md`](work/decision-log.md).

## 2. Product, declared unit and system boundary

- **Declared unit:** one manufactured and packaged 1 L BC1 representative plastic electric kettle at the factory gate.
- **BOM input:** quantities pasted by the user in chat. The classroom brief identifies the representative BC1 BOM with the EU Electric Kettles preparatory study (2020), Task 4, Tables 4-3, 4-4 and 4-8 (printed pages 26, 27 and 30). No source file or BOM revision was present locally. Local machine-readable copy: [`data/bom.csv`](data/bom.csv).
- **Mass check:** kettle components = **723.00 g**; packaging = **137.80 g**; packaged unit = **860.80 g**. Script recomputes these totals from all 12 lines.
- **Intended included stages:** material extraction and production; component/product conversion; assembly; packaging manufacture/packing; supplier-to-factory transport where data exist.
- **Actually quantified:** material factors for BOM entries plus an assumed aggregate electricity input for conversion/assembly. The factors have different process boundaries; see Sections 3–5.
- **Excluded:** customer use, end-of-life, outbound distribution after factory gate.
- **Cut-offs:** no formal cut-off rule; no items were removed from the BOM. Missing processes are listed as data gaps, not as zero.
- **Geography/reference year:** no product manufacturing geography or common reference year is specified. External factor geographies span China, Japan, Europe, Germany and the United States. The electricity placeholder uses China 2022 only as a stated scenario.
- **Use/end-of-life extension:** not modeled.

## 3. Foreground inventory and quantitative assumptions

| Input | Value | Evidence/status | Treatment |
|---|---:|---|---|
| Stainless steel | 186 g | Sourced from supplied BOM | Finished mass treated as purchased input |
| Brass | 20.25 g | Sourced from supplied BOM | Alloy grade/form unknown |
| Copper | 15 g | Sourced from supplied BOM | Grade/form unknown |
| PP | 350.25 g | Sourced from supplied BOM | Resin grade and recycled content unknown |
| PVC | 43.5 g | Sourced from supplied BOM | Formulation/recycled content unknown |
| Nylon | 49.5 g | Sourced from supplied BOM | Grade unknown |
| POM | 9.75 g | Sourced from supplied BOM | Grade unknown |
| PC | 6.75 g | Sourced from supplied BOM | Grade/additives unknown |
| ABS | 30 g | Sourced from supplied BOM | Grade/recycled content unknown |
| Silicone | 12 g | Sourced from supplied BOM | Cure/formulation unknown |
| LDPE packaging foil | 6.3 g | Sourced from supplied BOM | Film specification unknown |
| Cardboard packaging | 131.5 g | Sourced from supplied BOM | Board type/recycled content unknown |
| Component conversion + assembly electricity | **0.50 kWh/unit** | Assumed placeholder; no factory data | Included in screening total; sensitivity at 0, 0.25, 0.5 and 1 kWh in [`outputs/energy_sensitivity.csv`](outputs/energy_sensitivity.csv) |
| Electricity factor | **0.5366 kg CO₂/kWh** | China national-average 2022 official factor | CO₂-only factor; not full lifecycle GWP factor |
| Yield / production loss | 100% assumed | No loss data supplied | Purchased input equals BOM finished mass; scrap is omitted, not credited |
| Inbound transport | Unknown / not calculated | Supplier origins and distances unavailable | Omitted from result |
| Process heat, water, packaging-line energy | Unknown / not calculated | No factory/process records | Omitted from result |
| Scrap and recycling credits | Unknown / not calculated | No quantities/destination/allocation data | No burden or credit modeled |
| Prices / monetary proxies | Not applicable | No monetary estimation used | — |

Masses are converted from grams to kilograms by dividing by 1,000. Each contribution is `finished_mass_kg × factor_kg_CO2e_per_kg`. No yield adjustment was possible. Resin factors generally include upstream resin production, so that upstream energy is not added again. PC's proxy is a solid-sheet product factor and includes sheet processing; corrugated board's factor is for corrugated board. The electricity placeholder is an aggregate process estimate and must not be added again if replaced by molding/assembly process datasets that already include energy.

## 4. Background data and matching decisions

TianGong process candidates are listed in [`data/dataset_mapping.csv`](data/dataset_mapping.csv), including their visible UUID/version, geography/year/reference flow where exposed, source URL, retrieval date and decision. No candidate is accepted as a provider for the numeric run. The supplied [TianGong database page](https://www.tiangong.earth/en/lca-database) and [LCIA guide](https://docs.tiangong.earth/en/docs/user-guide/lcia/) distinguish complete process/flow linkage and characterization from a material flow record alone.

| BOM entries | Numeric factor used | Geography and basis | Source |
|---|---:|---|---|
| Stainless steel | 1.76 kg CO₂-e/kg | China stainless-steel production average; not kettle-grade-specific | Jing et al. 2019, [DOI](https://doi.org/10.1002/ep.13125) |
| Brass | 1.415 kg CO₂e/kg | Germany, CuZn20 alloy A1-A3 GWP-total; 90% secondary content is described in dataset | [ÖKOBAUDAT dataset](https://www.oekobaudat.de/OEKOBAU.DAT/datasetdetail/process.xhtml?uuid=3d5b565c-187b-4413-ab45-3eaa89ede35d&version=20.21.060) |
| Copper | 5.88 kg CO₂e/kg | China production route mix, cradle-to-gate | Dong et al. 2020, [DOI](https://doi.org/10.1016/j.jclepro.2020.122825) |
| PP, PVC, LDPE | 1.878598; 2.026849; 2.085433 kg GHG/kg respectively | Japan, resin cradle-to-gate factors, based on industry-weighted resin data and IDEA upstream links | [Plastic Waste Management Institute, 2025](https://www.pwmi.or.jp/column/column-2636/) |
| Nylon, POM, ABS | 7.45; 3.15; 3.84 kg CO₂e/kg respectively | European grouped EPD proxies: PA6/PA66; POM/PBT; ABS/ASA/PS | [EPD Denmark](https://www.epddanmark.dk/media/aaffkvml/md-26002-en.pdf) |
| PC | 3.9 kg CO₂e/kg | European solid PC sheet A1-A3 factor; includes sheet production | [EPD](https://epd-online.com/Epd/PdfDownload?id=23711&stat=true) |
| Silicone | 5.79 kg CO₂e/kg | Virgin RTV-1 sealant cradle-to-gate proxy; product differs from unspecified kettle silicone | [RSC article](https://pubs.rsc.org/en/content/articlehtml/2026/gc/d6gc01680d) |
| Corrugated cardboard | 1.20 kg CO₂/kg | United States corrugated board; excludes biogenic CO₂ | [Fibre Box Association 2020 LCA](https://www.fibrebox.org/assets/2024/03/2020_LCA-_Full_Report.pdf) |
| Aggregate electricity | 0.5366 kg CO₂/kWh | China national average, 2022 | [MEE/NBS announcement](https://www.mee.gov.cn/xxgk2018/xxgk/xxgk01/202412/t20241226_1099413.html) |

These are external factors rather than one common LCIA database release. Their characterization methods, geography, reference year and boundary are not harmonized; some are GWP-total, some reported GHG/CO₂-e, and the electricity factor is CO₂-only. Thus the sum is a screening indicator and should not be presented as a standards-compliant harmonized GWP100 result. No file hash is available for remote sources. The search was by material names/synonyms in the public TianGong catalog; complete query exports and TianGong datasets are not locally cached. USLCI was not downloaded or used. The user-provided `release-downloads.md` (outside this repository) documents USLCI releases, including JSON-LD through LCA Commons; it is not itself a database package. No monetary proxy or supplier link was used.

## 5. Calculation and impact-assessment methods

- **Implemented algorithm:** transparent arithmetic, equivalent to a diagonal one-process-per-material scaling model. For material `i`, `mass_i_kg = BOM_g_i / 1000`; `impact_i = mass_i_kg × factor_i`. Then sum material contributions and the aggregate electricity estimate.
- **Model form:** conceptually `A s = f`, `g = B s`, `h = C g`; the provided script does not assemble a process matrix, elementary-flow inventory, or characterization matrix. It multiplies published cumulative factors directly.
- **Software:** Python standard library only; script [`src/calculate.py`](src/calculate.py). No LCA solver/database engine was invoked.
- **Provider linking:** no automatic or manual TianGong/USLCI provider links. Proxy factors are manually curated in [`data/screening_factors.csv`](data/screening_factors.csv).
- **Allocation/recycling:** no kettle scrap allocation or avoided-burden credit. Brass proxy contains its source dataset's secondary-content assumption; packaging board proxy reflects its source study's product mix. No end-of-life recycling is included.
- **Impact indicator:** screening climate indicator reported in kg CO₂e/unit, intended to approximate GWP100 from source factors; method versions are heterogeneous and not harmonized. This is not a full GWP100 LCIA result. Other impact categories are not calculated.
- **Biogenic carbon:** cardboard factor excludes biogenic CO₂; no other biogenic flow characterization is performed.
- **Flow matching/missing providers:** no elementary-flow mapping was performed. Unknown providers and uncharacterized flows cannot be reported as zero; they remain outside the factor-based calculation.

## 6. How to reproduce the analysis

Files:

```text
data/bom.csv                    supplied BOM, machine-readable
data/screening_factors.csv      external screening factors and sources
data/dataset_mapping.csv        TianGong candidate match log
src/calculate.py                arithmetic calculation
outputs/contributions.csv       per-material result
outputs/energy_sensitivity.csv  electricity scenario table
outputs/summary.txt             run summary
work/decision-log.md            user requirements and modeling decisions
```

Run from the repository root with Python 3:

```powershell
python src/calculate.py
```

The script uses only Python standard-library modules, reads `data/` and rewrites the three files in `outputs/`. No API, account, seed, or external download is needed to reproduce the arithmetic. To update the research factors, review their source and scope, edit `data/screening_factors.csv`, then rerun. TianGong/USLCI dataset access, account permissions, exact provider matching, and LCIA characterization would be additional manual steps. The supplied USLCI release document mentions LCA Commons/API access requirements; no API key value is present or needed here.

## 7. Results, checks and interpretation

**Baseline screening scenario:** one packaged kettle, proxy material factors, and assumed 0.50 kWh aggregate conversion/assembly electricity.

- BOM material-factor subtotal: **1.971791 kg CO₂e/unit**.
- Assumed electricity contribution: **0.268300 kg CO₂/unit**.
- Arithmetic screening total: **2.240091 kg CO₂e per packaged kettle**.
- This total is not a harmonized GWP100 result and does not close the full requested cradle-to-gate inventory because transport, heat, water, scrap and some conversion processes are missing.

| Contribution | kg CO₂e/unit | Share of arithmetic total |
|---|---:|---:|
| PP | 0.657979 | 29.4% |
| Assumed conversion/assembly electricity | 0.268300 | 12.0% |
| Nylon | 0.368775 | 16.5% |
| Stainless steel | 0.327360 | 14.6% |
| Cardboard packaging | 0.157800 | 7.0% |
| ABS | 0.115200 | 5.1% |
| Copper | 0.088200 | 3.9% |
| PVC | 0.088168 | 3.9% |
| Silicone | 0.069480 | 3.1% |
| POM | 0.030713 | 1.4% |
| Brass | 0.028654 | 1.3% |
| PC | 0.026325 | 1.2% |
| LDPE resin | 0.013138 | 0.6% |

The three largest entries are PP, nylon and stainless steel (electricity is also a large foreground assumption). Together the top three materials contribute 1.354114 kg CO₂e, about 60.5% of the arithmetic screening total. The ranking is conditional on the chosen proxy factors and is not evidence of a supplier-specific hotspot.

- **Mass/unit check:** pass; 723.00 g kettle + 137.80 g packaging = 860.80 g total.
- **Provider/supplier closure:** fail/not performed; no dataset providers or suppliers are linked.
- **Contribution sum:** pass within arithmetic precision; contributions sum to 2.240091 kg CO₂e/unit.
- **Double counting:** no explicit duplicated upstream energy was added; however the aggregate conversion/assembly electricity is a placeholder that could overlap future component process datasets. PC and cardboard factors already include processing at their source-defined boundaries.
- **Sensitivity:** electricity-only variation gives totals of 1.971791 (0 kWh), 2.105941 (0.25 kWh), 2.240091 (0.5 kWh) and 2.508391 (1.0 kWh) kg CO₂e/unit. This is a scenario check, not probabilistic uncertainty. See [`outputs/energy_sensitivity.csv`](outputs/energy_sensitivity.csv), [`outputs/contributions.csv`](outputs/contributions.csv), and [`outputs/summary.txt`](outputs/summary.txt).
- **Interpretation limits:** omitted transport and unit processes, proxy region/method inconsistency, and possible factor boundary mismatches prevent a complete product footprint claim.

## 8. Uncertainty and sensitivity

No probability distributions, correlations, Monte Carlo draws, or confidence intervals were calculated because source-specific uncertainty distributions were unavailable and the inventory is incomplete. The four electricity cases are deterministic scenarios only. Parameter uncertainty, database/provider scenarios, and repeated AI-run variability are not quantified. Mean, median and P05/P95 are therefore not available; the range in Section 7 is conditional only on the selected electricity assumptions and fixed proxy factors.

## 9. Codex and human decisions

- **Codex model/version:** GPT-6 as shown in the task environment; exact build and reasoning setting unavailable.
- **Run date:** 2026-10-08; exact start/end timestamps were not preserved in the artifact.
- **Consequential prompts:** user requested the LCA plan, asked what decisions were needed, said all were unknown, clarified it was a class assignment and asked Codex to make reasonable choices, then asked for impact assessment and supplied class-lab/GitHub/USLCI references. See [`work/decision-log.md`](work/decision-log.md) for the curated decisions.
- **Student decisions:** no candidate datasets, geography, reference year, grades, or LCIA method were confirmed by the student. The assumptions in this screening run were chosen by Codex to produce an explicit estimate in response to the instruction to proceed.
- **Accepted/rejected matches:** no TianGong candidate was accepted as a numerical provider. External factors were accepted only as screening proxies and are recorded with sources in `data/screening_factors.csv`.
- **Edits/checks:** BOM data transcribed to CSV; script output checked against the mass total and contribution sum. No independent LCA model/output was available for comparison.
- **Assistance:** public web/catalog review and local Python arithmetic. No credentials, private messages, or restricted database dumps are included.

## 10. Independent and revised runs

- No independent baseline output, Git tag, or prior commit was available.
- This is the first local proxy screening run; no revised run was made and no prior/revised numerical difference applies.
- Preserve this output before comparing with classmates; do not overwrite the baseline when a later provider or method scenario is evaluated. A future revision should use a separate run ID and record the changed decision and resulting delta.
- No commit SHA is available because this directory has not been initialized as the student's Git repository. The final commit SHA belongs in the course form after the student creates/uses the correct repository and commits.

## Unresolved information for review before commit and push

1. What is the actual student/group alias and repository URL? The supplied GitHub link identifies TianGong's organization, not the student's repository.
2. Confirm whether the class accepts a proxy-based screening estimate, or requires an actual TianGong/USLCI linked model and a specified LCIA method/version.
3. Confirm manufacturing geography/reference year and supplier routes; steel/brass/resin proxies currently span several geographies.
4. Confirm nylon/POM/PC/ABS/silicone grades, recycled content, brass alloy, and actual cardboard/foil specifications.
5. Replace the assumed 0.50 kWh/unit with injection molding, metal forming, assembly and packaging-line process data; provide yield/scrap and inbound transport distances.
6. Check the factor definition/metadata for each source, especially grouped polymer EPD values and the GHG versus GWP100 method compatibility, before reporting a formal GWP100 number.
7. Confirm whether the document at `C:\Users\DB_MSE\Downloads\release-downloads.md` is only an installation/source reference (as read here) or whether a downloaded USLCI package should also be used.
