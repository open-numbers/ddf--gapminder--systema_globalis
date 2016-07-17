# Recipe Standard (draft)

In this document:

1. define what is recipe and what can we do with it
2. define what are keywords in recipe and the structure of a recipe
3. from recipe to dataset

## What is recipe

recipe is an instruction about how to construct a new dataset from existing one.
by reading and running the recipe executor, one can generate a new dataset for 
any propose.

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

- `recipes_dir`: the directory contians all recipes.
- `dictionary_dir`: the directory contains all translation files. (translation 
will be discussed later)

### include

TODO

### cooking procedures

TODO
