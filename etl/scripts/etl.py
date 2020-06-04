# -*- coding: utf-8 -*-

import os
from ddf_utils.chef.api import Chef


out_dir = '../../'
recipe_file = '../recipes/etl.yaml'

try:
    datasets_dir = os.environ['DATASETS_DIR']
except KeyError:
    datasets_dir = '../../../'


if __name__ == '__main__':
    chef = Chef.from_recipe(recipe_file, ddf_dir=datasets_dir)
    chef.run(serve=True, outpath=out_dir)
