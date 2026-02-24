# ETL

This dataset is built from recipes under `etl/recipes`, with the main entrypoint:

- `etl/recipes/etl.yaml`

You can run `etl/scripts/etl.py` or use the `ddf` command to run the recipes.

## How to update

This dataset relys on following datasets. In order to update this dataset, one should update the source datasets and run the etl script.

### Source datasets

The datasets below are all `dataset:` sources referenced by recipes included by
`etl/recipes/etl.yaml` (including nested includes).

| Dataset ID | Recipe(s) | Repo |
| --- | --- | --- |
| `open-numbers/ddf--gapminder--billionaires` | `countries/recipe_billionaire.yaml` | https://github.com/open-numbers/ddf--gapminder--billionaires |
| `open-numbers/ddf--gapminder--bp_energy` | `countries/recipe_bp.yaml` | https://github.com/open-numbers/ddf--gapminder--bp_energy |
| `open-numbers/ddf--gapminder--fao_fra` | `countries/recipe_fao_fra.yaml` | https://github.com/open-numbers/ddf--gapminder--fao_fra |
| `open-numbers/ddf--gapminder--fasttrack` | `countries/recipe_oecd.yaml` | https://github.com/open-numbers/ddf--gapminder--fasttrack |
| `open-numbers/ddf--gapminder--gapminder_world` | `countries.yaml`, `multidimensional.yaml` | https://github.com/open-numbers/ddf--gapminder--gapminder_world |
| `open-numbers/ddf--gapminder--gbd_indicators` | `countries/recipe_gbd.yaml` | https://github.com/open-numbers/ddf--gapminder--gbd_indicators |
| `open-numbers/ddf--gapminder--ihme_edu_attainment` | `countries/recipe_ihme_edu_attainment.yaml` | https://github.com/open-numbers/ddf--gapminder--ihme_edu_attainment |
| `open-numbers/ddf--gapminder--ilostat` | `countries/recipe_ilostat.yaml` | https://github.com/open-numbers/ddf--gapminder--ilostat |
| `open-numbers/ddf--gapminder--ontology` | `countries.yaml`, `countries/recipe_gw_geo.yaml` | https://github.com/open-numbers/ddf--gapminder--ontology |
| `open-numbers/ddf--gapminder--static_assets` | `countries.yaml` | https://github.com/open-numbers/ddf--gapminder--static_assets |
| `open-numbers/ddf--gapminder--unfao_faostat` | `countries/recipe_fao_faostat.yaml` | https://github.com/open-numbers/ddf--gapminder--unfao_faostat |
| `open-numbers/ddf--gapminder--unpop_wpp` | `countries/recipe_unpop.yaml` | https://github.com/open-numbers/ddf--gapminder--unpop_wpp |
| `open-numbers/ddf--gapminder--who_gho` | `countries/recipe_who_gho.yaml` | https://github.com/open-numbers/ddf--gapminder--who_gho |
| `open-numbers/ddf--igme--cme` | `countries/recipe_igme_cme.yaml` | https://github.com/open-numbers/ddf--igme--cme |
| `open-numbers/ddf--imf--mfs_ir` | `countries/recipe_imf_mfs.yaml` | https://github.com/open-numbers/ddf--imf--mfs_ir |
| `open-numbers/ddf--inscr--polity5` | `countries/recipe_polity5.yaml` | https://github.com/open-numbers/ddf--inscr--polity5 |
| `open-numbers/ddf--ncdrisc--indicators` | `countries/recipe_ncdrisc.yaml` | https://github.com/open-numbers/ddf--ncdrisc--indicators |
| `open-numbers/ddf--oecd--dac` | `countries/recipe_oecd.yaml` | https://github.com/open-numbers/ddf--oecd--dac |
| `open-numbers/ddf--open_numbers` | `countries/recipe_gw_geo.yaml` | https://github.com/open-numbers/ddf--open_numbers |
| `open-numbers/ddf--open_numbers--em_dat_indicators` | `countries/recipe_em_dat.yaml` | https://github.com/open-numbers/ddf--open_numbers--em_dat_indicators |
| `open-numbers/ddf--open_numbers--world_development_indicators` | `countries/recipe_wdi.yaml` | https://github.com/open-numbers/ddf--open_numbers--world_development_indicators |
| `open-numbers/ddf--pwt--penn_world_table` | `countries/recipe_pwt.yaml` | https://github.com/open-numbers/ddf--pwt--penn_world_table |
| `open-numbers/ddf--undp--hdi` | `countries/recipe_hdi.yaml` | https://github.com/open-numbers/ddf--undp--hdi |
| `open-numbers/ddf--unesco--education` | `countries/recipe_unesco_edu.yaml`, `global-regions/unesco_edu_global.yaml`, `global-regions/unesco_edu_income_groups.yaml` | https://github.com/open-numbers/ddf--unesco--education |
| `open-numbers/ddf--unfao--aquastat` | `countries/recipe_fao_aqua.yaml` | https://github.com/open-numbers/ddf--unfao--aquastat |
| `open-numbers/ddf--unicef--stillbirth` | `countries/recipe_unicef_stillbirth.yaml` | https://github.com/open-numbers/ddf--unicef--stillbirth |
| `open-numbers/ddf--who--tb_burden_estimates` | `countries/recipe_whotb.yaml` | https://github.com/open-numbers/ddf--who--tb_burden_estimates |
| `open-numbers/ddf--wipo--patent_indicators` | `countries/recipe_wipo.yaml` | https://github.com/open-numbers/ddf--wipo--patent_indicators |
| `open-numbers/ddf--world_bank--world_development_indicators` | `global-regions/wdi_global.yaml` | https://github.com/open-numbers/ddf--world_bank--world_development_indicators |
| `open-numbers/ddf--worldbank--education_statistics` | `countries/recipe_wb_edstats.yaml` | https://github.com/open-numbers/ddf--worldbank--education_statistics |
| `open-numbers/ddf--worldbank--povcalnet` | `countries/recipe_wb_pip.yaml` | https://github.com/open-numbers/ddf--worldbank--povcalnet |

Note: WDI is currently sourced from two differently named dataset IDs:
`open-numbers/ddf--open_numbers--world_development_indicators` (countries)
and `open-numbers/ddf--world_bank--world_development_indicators`
(global-regions).
