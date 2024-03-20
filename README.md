# Quarterly Macroeconomic Variables

This is the code to produce dataset *Quarterly Macroeconomic Variables*. I merge and
cleaned macroeconomic data from multiple public sources. The final dataset contains many
of the most important macroeconomic indicators such as GDP, inflation, etc. for 39
countries.

You find the produced dataset in this directory (the Excel file *Quarterly Macroeconomic
Variables.xlsx*)

The dataset is also published via the Harvard Data Universe
[here](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2F9CPKBB&version=DRAFT)

## How to Produce the Dataset Yourself

To get started, create and activate the environment with

```console
$ conda/mamba env create
$ conda activate global_macro_variables
```

To build the project, type

```console
$ pytask
```

## Credits

This project was created with [cookiecutter](https://github.com/audreyr/cookiecutter)
and the
[econ-project-templates](https://github.com/OpenSourceEconomics/econ-project-templates).
