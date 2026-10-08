import csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
RUN_ID='rerun-20261008-01'
bom=list(csv.DictReader((ROOT/'data/bom.csv').open(encoding='utf-8-sig',newline='')))
factors={r['material']:r for r in csv.DictReader((ROOT/'data/screening_factors.csv').open(encoding='utf-8-sig',newline=''))}
# BOM check in integer grams; impact arithmetic uses only documented legacy proxy factors.
by_scope={}
rows=[]
for b in bom:
    mass_g=float(b['finished_mass_g']); by_scope[b['scope']]=by_scope.get(b['scope'],0)+mass_g
    f=factors[b['material']]; impact=mass_g/1000*float(f['kg_co2e_per_kg'])
    rows.append({'material':b['material'],'scope':b['scope'],'finished_mass_g':mass_g,'kg_proxy_factor_per_kg':float(f['kg_co2e_per_kg']),'factor_geography':f['geography'],'contribution_kg_co2e_screening':impact,'status':'proxy scenario; not harmonized LCIA'})
assert len(bom)==12 and abs(by_scope['Kettle']-723)<1e-9 and abs(by_scope['Packaging']-137.8)<1e-9
subtotal=sum(r['contribution_kg_co2e_screening'] for r in rows)
energy_factor=0.5366
with (ROOT/'runs'/f'{RUN_ID}_contributions.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
sens=[]
for kwh in [0,.25,.5,1]: sens.append({'energy_kwh_per_unit':kwh,'factor_kg_co2_per_kwh':energy_factor,'energy_kg_co2':kwh*energy_factor,'screening_arithmetic_total_kg_co2e':subtotal+kwh*energy_factor})
with (ROOT/'runs'/f'{RUN_ID}_sensitivity.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=sens[0].keys());w.writeheader();w.writerows(sens)
summary={'run_id':RUN_ID,'date':'2026-10-08','functional_unit':'one packaged 1 L electric kettle at factory gate','bom_scope_g':by_scope,'total_mass_g':sum(by_scope.values()),'proxy_material_subtotal_kg_co2e':subtotal,'assumed_energy_kwh_per_unit':.5,'assumed_energy_factor_kg_co2_per_kwh':energy_factor,'screening_arithmetic_total_kg_co2e':subtotal+.5*energy_factor,'result_status':'screening arithmetic only; incomplete inventory; not a complete LCA/LCIA'}
(ROOT/'runs'/f'{RUN_ID}_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
