{- let lib =
      https://raw.githubusercontent.com/semio/dhall-ddf-recipe/master/package.dhall -}
let lib =
      /Users/semio/src/work/Gapminder/libs/dhall_recipe_procedures/package.dhall

let Recipe = lib.render.recipe_builder

let unpop = "open-numbers/ddf--unpop--world_population_prospects"

let age5yearinterval = [ "0_4", "10_14", "15_19", "5_9" ]

let agebroad = [ "0_14", "20_39", "40_59", "60plus", "65plus", "70plus" ]

let genders = [ "1", "2" ]

-- let global = [ "900" ]

let ingredients =
      lib.render.with_dataset
        unpop
        [ { id = "unpop-dps-agebroad-gender"
          , key = "global, time, agebroad, gender"
          , value =
              lib.render.ingredient.value_filter.list
                [ "population_percentage" ]
          }
        , { id = "unpop-dps-age5year-gender"
          , key = "global, time, age5yearinterval, gender"
          , value =
              lib.render.ingredient.value_filter.list
                [ "population_percentage" ]
          }
        , { id = "unpop-dps-agebroad"
          , key = "global, time, agebroad"
          , value =
              lib.render.ingredient.value_filter.list
                [ "population", "population_percentage" ]
          }
        , { id = "unpop-dps-age5year"
          , key = "global, time, age5yearinterval"
          , value =
              lib.render.ingredient.value_filter.list
                [ "population", "population_percentage" ]
          }
        ]

let filter = lib.render.filter

let Dict = lib.types.Dict

let filter_proc =
        λ(ingredient : Text)
      → λ(ageType : Text)
      → λ(ageValues : List Text)
      → λ(gender : Optional (List Text))
      → let t = List Text

        let row_opt =
              Optional/fold
                t
                gender
                (Dict Text t)
                (   λ(v : t)
                  → [ { mapKey = ageType, mapValue = ageValues }
                    , { mapKey = "gender", mapValue = v }
                    ]
                )
                (   [ { mapKey = ageType, mapValue = ageValues }
                    ]
                  : Dict Text t
                )

        let result = ingredient ++ "-filtered"

        in  filter.run
              { ingredients = [ ingredient ]
              , options =
                { row = filter.row.simple_dict row_opt
                , item = filter.item.no_filter {=}
                }
              , result
              }

let flatten = lib.render.flatten

let merge_ = lib.render.merge

let translate_column = lib.render.translate_column

let translate_header = lib.render.translate_header

let translate_age =
        λ(ingredient : Text)
      → translate_header.run
          { ingredients = [ ingredient ]
          , options =
                translate_header.default_options
              ⫽ { dictionary =
                    translate_header.dictionary.inline
                      (toMap { agebroad = "age", age5yearinterval = "age" })
                }
          , result = ingredient ++ "-age-translated"
          }

let datapoints =
      [ filter_proc
          "unpop-dps-agebroad-gender"
          "agebroad"
          agebroad
          (Some genders)
      , filter_proc
          "unpop-dps-age5year-gender"
          "age5yearinterval"
          age5yearinterval
          (Some genders)
      , filter_proc "unpop-dps-agebroad" "agebroad" agebroad (None (List Text))
      , filter_proc
          "unpop-dps-age5year"
          "age5yearinterval"
          age5yearinterval
          (None (List Text))
      , translate_age "unpop-dps-agebroad-gender-filtered"
      , translate_age "unpop-dps-age5year-gender-filtered"
      , translate_age "unpop-dps-agebroad-filtered"
      , translate_age "unpop-dps-age5year-filtered"
      , merge_.run
          { ingredients =
            [ "unpop-dps-agebroad-gender-filtered-age-translated"
            , "unpop-dps-age5year-gender-filtered-age-translated"
            ]
          , options.deep = True
          , result = "unpop-dps-age-gender"
          }
      , translate_column.run
          { ingredients = [ "unpop-dps-age-gender" ]
          , options =
            { column = "gender"
            , target_column = "gender"
            , dictionary =
                translate_column.dictionary.simple
                  [ { mapKey = "1", mapValue = "male" }
                  , { mapKey = "2", mapValue = "female" }
                  ]
            }
          , result = "unpop-dps-age-gender-translated"
          }
      , flatten.run
          { ingredients = [ "unpop-dps-age-gender-translated" ]
          , options =
            { flatten_dimensions = [ "gender", "age" ]
            , skip_totals_among_entities = [] : List Text
            , dictionary = toMap
                { population_percentage =
                    "population_aged_{age}_years_{gender}_percent"
                }
            }
          , result = "unpop-dps-age-gender-translated-flatten"
          }
      , merge_.run
          { ingredients =
            [ "unpop-dps-agebroad-filtered-age-translated"
            , "unpop-dps-age5year-filtered-age-translated"
            ]
          , options.deep = True
          , result = "unpop-dps-age"
          }
      , flatten.run
          { ingredients = [ "unpop-dps-age" ]
          , options =
            { flatten_dimensions = [ "age" ]
            , skip_totals_among_entities = [] : List Text
            , dictionary = toMap
                { population_percentage =
                    "population_aged_{age}_years_both_sexes_percent"
                , population = "population_aged_{age}_years_total_numbers"
                }
            }
          , result = "unpop-dps-age-flatten"
          }
      , merge_.run
          { ingredients =
            [ "unpop-dps-age-flatten"
            , "unpop-dps-age-gender-translated-flatten"
            ]
          , options.deep = False
          , result = "unpop-global-dps-final"
          }
      ]

in  Recipe.Main::{
    , ingredients = ingredients
    , cooking = Recipe.Cooking::{ datapoints = datapoints }
    }
