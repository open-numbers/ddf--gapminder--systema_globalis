# Systema Globalis (SG)
The name is inspired by [Systema Naturae](https://en.wikipedia.org/wiki/Systema_Naturae); the first systematic compilation of all living things from year 1735, by the Swedish Scientist Carl von Linné. The goal of Systema Globalis is to compile all public statistics; Social, Economic and Environmental; into a comparable total dataset.

## Data
This is the main dataset used in tools on the official Gapminder website. It contains local &amp; global statistics combined from hundreds of sources.

## How to update
Currently the dataset is maintained by manually copying data from multiple other datasets.
The plan is to automate the process by using a file called ddf--imports.csv
Described [here](https://github.com/open-numbers/Data-Description-Format-DDF/wiki/File:-ddf-imports)

##Dependencies
If you added more dataset dependencies, add them manually to the excel file in data_process, and save as csv to the dataset folder. All GS-dependencies must be of type ddf and public as an Open Numbers github repo.
Files:
* ddf--dependencies is manually edited

## License
Gapminder created this dataset and provides it under [Creative Common Attribution 4.0 International][CC].

[CC]: https://creativecommons.org/licenses/by/4.0/
