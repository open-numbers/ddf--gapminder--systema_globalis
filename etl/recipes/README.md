# Recipe Standard (draft)

## What is recipe

recipe is an instruction about how to construct a new dataset from existing one.
by reading and running the recipe executor, one can generate a new dataset based
on the `ingredients` and `procedures` described in the recipe.

## structure of for a recipe

A recipe is mainly construct with 4 parts:

- basic info
- configurations
- include of other files
- cooking procedures

A recipe file can be in either json or yaml format. Please check the yaml file in
this folder to see examples of recipes.

### basic info

all basic info are stored in `info` section of the recipe. an `id` field is
required inside this section. Any other information about the new dataset can be
store inside this section, such as `name`, `provider`, `description` and so on.

### config

inside configuration section. we define the configuration of dirs. currently we
can set below path:

- `recipes_dir`: the directory contains all recipes to include.
- `dictionary_dir`: the directory contains all translation files. (translation
will be discussed later)

### include

one recipe can include other recipes inside itself. to include a recipe, simply
append the filename to the `include` section. note that it should be a absolute
path or a filename inside the `recipes_dir`.

### cooking procedures

supported procedures currently:

- translate_header
- translate_column
- identity
- merge
- align
    discussion: https://github.com/semio/ddf_utils/issues/3
- groupby
    discussion: https://github.com/semio/ddf_utils/issues/4
- filter_col
    discussion: https://github.com/semio/ddf_utils/issues/2
- filter_item
- run_op
    discussion: https://github.com/semio/ddf_utils/issues/7
