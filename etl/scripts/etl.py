# -*- coding: utf-8 -*-

from ddf_utils import chef
from ddf_utils.index import create_index_file
import os

out_dir = '../../'
recipe_file = '../recipes/recipe_main.yaml'

if __name__ == '__main__':
    # removing old files
    for f in os.listdir(out_dir):
        if f.startswith("ddf--"):
            os.remove(os.path.join(out_dir, f))

    recipe = chef.build_recipe(recipe_file)
    res = chef.run_recipe(recipe)
    chef.dish_to_csv(res, out_dir)

    create_index_file(out_dir)
