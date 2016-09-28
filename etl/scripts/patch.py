# -*- coding: utf-8 -*-

import pandas as pd
import os

out_dir = '../../'

def concepts_tag_column():
    """add tag column to measures"""
    concs = pd.read_csv(os.path.join(out_dir, 'ddf--concepts.csv'))
    graph = pd.read_excel('../source/graph_settings.xlsx', sheetname='Indicators')
    mappin = pd.read_excel('../source/Gapminder world tag tree.xlsx', skip_footer=4)

    measures = concs[concs['concept_type'] == 'measure']
    measures = measures.set_index('concept').drop(['age', 'latitude', 'longitude'])

    graph = graph.set_index('ddf_id')
    m = graph.loc[measures.index, ['Menu level1', 'Menu level 2']].copy()
    mappin = mappin.set_index(['tag_name'])

    m2 = m.copy()

    for k, v in m.iterrows():

        if v['Menu level 2'] == 'Water' and v['Menu level1'] == 'Environment':
            m2.loc[k, 'tags'] = 'environment_water'
            continue

        if v['Menu level 2'] == 'Water' and v['Menu level1'] == 'Infrastructure':
            m2.loc[k, 'tags'] = 'infrastructure_water'
            continue

        if not pd.isnull(v['Menu level 2']):
            m2.loc[k, 'tags'] = mappin.loc[v['Menu level 2'], 'tag_id']
        elif not pd.isnull(v['Menu level1']):
            m2.loc[k, 'tags'] = mappin.loc[v['Menu level1'], 'tag_id']
        else:
            continue


    m2.loc['children_per_woman_total_fertility', 'tags'] = '_root, newborn_infants'
    m2.loc['co2_emissions_tonnes_per_person', 'tags'] = '_root, emissions'
    m2.loc['income_per_person_gdppercapita_ppp_inflation_adjusted', 'tags'] = '_root, incomes_growth'
    m2.loc['child_mortality_0_5_year_olds_dying_per_1000_born', 'tags'] = '_root, mortality'
    m2.loc['life_expectancy_years', 'tags'] = '_root, life_expectancy'

    concs = concs.set_index('concept')
    concs['tags'] = m2['tags']

    concs.to_csv(os.path.join(out_dir, 'ddf--concepts.csv'))
