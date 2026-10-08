# Packaged 1 L electric kettle cradle-to-gate reassessment

## Status and scope

This repository preserves a second, separately identified screening run (`rerun-20261008-01`) for the functional unit **one packaged 1 L electric kettle at the factory gate**. It includes raw material production, component conversion, assembly, packaging production/packing, and inbound transport in the intended boundary; customer delivery, use, and end-of-life are excluded. The requested full inventory is **not closed**. The reported climate arithmetic is a transparent screening estimate only and is not a complete LCA or harmonized LCIA result.

## BOM and mass reconciliation

`data/bom.csv` is the user-provided BOM, transcribed as supplied. `src/calculate.py` parses all 12 entries and checks the mass totals. Kettle material = **723.00 g**; packaging = **137.80 g**; total packed mass = **860.80 g**. These are finished-product masses, not purchased feed adjusted for manufacturing loss.

## Dataset search and matching

`data/dataset_mapping.csv` records dataset name, release/catalog, UUID/version when exposed, geography, year, reference flow, source URL, access date, and match decision. The TianGong records include process candidates for 304 stainless billet, copper, PP, PVC, LDPE, and corrugated board from the previous submission's search log. A steel billet is not the kettle's sheet/formed product; copper refined metal is not confirmed for the component; PP/PVC records have year/route and boundary issues. A brass product flow is not an LCI process. No provider was selected.

The supplied `release-downloads.md` was read as a **release/download index**, not a database package. It lists USLCI 1.2026-09.0 and points to the LCA Commons repository. Public search identified a US PVC virgin-resin unit process (UUID `3dbccdda-2014-4239-ad1f-4e15c034942b`, U.S., data collection 2015, 1 kg, gate-to-gate) and possible records for stainless steel 304 flat-rolled coil. PP, PC and corrugated product exchanges were found inside unrelated scanner processes; these exchanges are product flows and do not establish independent material-production processes. The candidate mappings are not linked into a kettle product system. Search date: 2026-10-08. Sources include the [USLCI repository](https://www.lcacommons.gov/lca-collaboration/National_Renewable_Energy_Laboratory/USLCI_Database_Public/datasets), [PVC process](https://lcacommons.gov/lca-collaboration/National_Renewable_Energy_Laboratory/USLCI_Database_Public/dataset/PROCESS/3dbccdda-2014-4239-ad1f-4e15c034942b), [TianGong catalog](https://www.tiangong.earth/en/lca-database), and [TianGong data repository organization](https://github.com/tiangong-lca).

No complete JSON-LD database package was downloaded or imported. There is no verified UUID-version set of linked providers for all BOM inputs, and no verified supplier chain to the kettle factory.

## Calculation and screening results

Reproduce using Python 3 standard library from repository root:

```powershell
python src/calculate.py
```

The script reads BOM and the preserved factor table `data/screening_factors.csv`; it writes run-specific files under `runs/`. Python used for this run: bundled Python 3 runtime (exact patch build not captured). The arithmetic is mass in kg multiplied by factor in kg CO2e/kg, plus the assumed aggregate electricity scenario.

- Material-proxy subtotal: **1.9717913589 kg CO2e/unit**.
- Assumed conversion/assembly/packing electricity: **0.50 kWh/unit × 0.5366 kg CO2/kWh = 0.268300 kg CO2/unit**. This factor is China 2022 national-average operational CO2, not lifecycle GWP.
- Screening arithmetic total: **2.2400913589 kg CO2e/unit**.
- Energy scenario totals: 0 kWh → 1.971791; 0.25 kWh → 2.105941; 0.50 kWh → 2.240091; 1.0 kWh → 2.508391 kg CO2e/unit.

Per-material contributions and the energy scenario table are in the run files. Factors are heterogeneous external proxies carried forward from the actual previous commit files; geographies and boundaries vary (China, Germany, Japan, Europe, U.S.). They are not a single consistent method, database release, or year. PC factor represents solid sheet and includes conversion; it may overlap foreground conversion. Cardboard proxy excludes biogenic CO2. Resin production factors are cumulative cradle-to-gate proxies. No formal LCIA method/version, time horizon characterization set, elementary-flow matching, or characterization-factor matrix was applied. Uncharacterized flows are not zero; they are unresolved.

## Assumptions and data gaps

`data/assumptions.csv` records assumptions and open gaps. Finished mass equals purchased mass (100% yield) only as a temporary arithmetic convention; scrap is not modeled or credited. No supplier origins, transport modes/distances, injection molding/forming energy, process heat, water, packaging-line energy, assembly inventory, or factory location were provided. No grade/recycled-content details are known for nylon, plastics, metals, silicone, foil, or board. No uncertainty distributions exist; the electricity cases are deterministic sensitivity scenarios, not probabilistic uncertainty. Do not interpret any missing process as zero.

A completed LCA requires product-specific grades/forms, actual supplier locations and process routes, conversion/assembly/packing records, yield/scrap and allocation rules, transport data, provider-linked complete process inventories, and a specified LCIA method/version with elementary-flow mapping.

## Prior-submission comparison and provenance

The prior submission was checked out at immutable commit `87fda697d865538a830693baae80da810c7cd5d0` and copied under `runs/prior/`. That commit actually contains only `README.md`, `contributions.csv`, `dataset_mapping.csv`, `energy_sensitivity.csv`, `screening_factors.csv`, and `summary.txt`; it does not contain the script, BOM, or decision log described by its README. These files are preserved unchanged. Its recorded proxy total is 2.2400913589 kg CO2e/unit. This run independently transcribes the supplied BOM and reruns the arithmetic with the archived factor table; the numerical difference is **0.000000 kg CO2e/unit** because no new impact-capable, matched provider or factor was defensibly introduced. Main change: the new repository makes the calculation reproducible and expands candidate search with USLCI evidence; the unresolved gaps remain and no full LCA claim is made.

Run ID: `rerun-20261008-01`. Decision and prompt log: `logs/decision-log.md`. Previous snapshot: `runs/prior/`. No secrets, personal names, email addresses, or credentials are included.
