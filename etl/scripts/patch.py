# -*- coding: utf-8 -*-

import shutil
import os
import pandas as pd
from ddf_utils.patch import apply_patch

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

    # manually set some tags.
    m2.loc['children_per_woman_total_fertility', 'tags'] = '_root, newborn_infants'
    m2.loc['co2_emissions_tonnes_per_person', 'tags'] = '_root, emissions'
    m2.loc['income_per_person_gdppercapita_ppp_inflation_adjusted', 'tags'] = '_root, incomes_growth'
    m2.loc['child_mortality_0_5_year_olds_dying_per_1000_born', 'tags'] = '_root, mortality'
    m2.loc['life_expectancy_years', 'tags'] = '_root, life_expectancy'

    concs = concs.set_index('concept')
    concs['tags'] = m2['tags']

    concs['tags'] = concs['tags'].fillna('_none')

    # remove concepts from dont panic poverty
    concs = concs.drop(['sg_population', 'sg_gini', 'sg_gdp_p_cap_const_ppp2011_dollar'])

    concs.to_csv(os.path.join(out_dir, 'ddf--concepts.csv'), encoding='utf8')


def remove_unneeded_dps():
    """remove some datapoints"""
    # FIXME: remove this function when chef is ready for this kind of tasks.
    os.remove(os.path.join(out_dir, 'ddf--datapoints--yearly_co2_emissions_tonnes--by--geo--time.csv'))
    os.remove(os.path.join(out_dir, 'ddf--datapoints--sg_gdp_p_cap_const_ppp2011_dollar--by--geo--time.csv'))
    os.remove(os.path.join(out_dir, 'ddf--datapoints--sg_population--by--geo--time.csv'))
    os.remove(os.path.join(out_dir, 'ddf--datapoints--sg_gini--by--geo--time.csv'))


def apply_patches():
    # list of patches to apply to files.
    # FIXME: find out which patch should apply to which file in the diff file.
    # then we can totally avoid manually setting it here and editting diff files.
    patches = {
        'ddf--concepts.csv': [
            'ddf--concepts.1.csv',
            'ddf--concepts.2.csv',
            'ddf--concepts.3.csv',
            'ddf--concepts.4.csv',
            'ddf--concepts.5.csv'
        ],
        'ddf--entities--tag.csv': [
            'ddf--entities--tag.0.csv'
        ],
        'ddf--index.csv' : [
            'ddf--inedx.0.csv'
        ]
    }
    # apply the patches
    for f, ps in patches.items():
        local_path = os.path.join(out_dir, f)
        for p in ps:
            print(p)
            patch_path = os.path.join('./patches', p)

            if os.path.exists(local_path):
                new_df = apply_patch(local_path, patch_path)
                new_df.to_csv(local_path, index=False, encoding='utf-8')
            else:
                shutil.copyfile(patch_path, local_path)


def do_all_changes():
    print("applying patches to DDF...")
    concepts_tag_column()
    remove_unneeded_dps()
    apply_patches()


if __name__ == '__main__':
    do_all_changes()
    print('Done.')
