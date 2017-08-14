"""custom procedures"""

import logging
import pandas as pd
from ddf_utils.chef.helpers import debuggable
from ddf_utils.chef.ingredient import Ingredient, ProcedureResult

logger = logging.getLogger('Chef')


@debuggable
def add_tag_column(chef, ingredients, result, **options):
    """add tag column to concepts"""
    ingredient = chef.dag.get_node(ingredients[0]).evaluate()
    logger.info("adding tag column to {}".format(ingredients[0]))

    concs = ingredient.get_data()['concept']
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

    concs = concs.set_index('concept')
    concs['tags'] = m2['tags']

    concs['tags'] = concs['tags'].fillna('_none')

    concs = concs.reset_index()

    return ProcedureResult(chef, result, 'concept', data={'concepts': concs})
    