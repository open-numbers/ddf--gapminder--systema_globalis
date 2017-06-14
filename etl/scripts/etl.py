# -*- coding: utf-8 -*-

from ddf_utils import chef
from ddf_utils.datapackage import get_datapackage, dump_json
import patch
import os
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s -%(levelname)s- %(message)s',
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
    res = chef.run_recipe(recipe, serve=True, outpath=out_dir)

    patch.do_all_changes()

    dump_json(os.path.join(out_dir, 'datapackage.json'), get_datapackage(out_dir))

    print('Done.')
