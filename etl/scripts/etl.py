# -*- coding: utf-8 -*-

from ddf_utils import chef
from ddf_utils.index import get_datapackage
import patch
import os
import json
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -%(levelname)s- %(message)s',
                    datefmt="%H:%M:%S"
                    )

out_dir = '../../'
recipe_file = '../recipes/recipe_main.yaml'

if __name__ == '__main__':
    # removing old files
    for f in os.listdir(out_dir):
        if f.startswith("ddf--"):
            os.remove(os.path.join(out_dir, f))

    recipe = chef.build_recipe(recipe_file)
    res = chef.run_recipe(recipe)
    print('saving result to disk...')
    chef.dish_to_csv(res, out_dir)

    patch.do_all_changes()

    # TODO: keep older datapacakge's basic info(author etc)
    datapackage = get_datapackage(out_dir)
    with open(os.path.join(out_dir, 'datapackage.json'), 'w', encoding='utf8') as f:
        json.dump(datapackage, f, indent=4, ensure_ascii=False)

    print('Done.')
