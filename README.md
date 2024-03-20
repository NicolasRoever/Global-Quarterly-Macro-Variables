# Quarterly Macroeconomic Variables

This is the code to produce dataset *Quarterly Macroeconomic Variables*. I merged and
cleaned macroeconomic data from multiple public sources. The dataset contains many of
the most important macroeconomic indicators such as GDP, inflation, etc. for 39
countries. See Table \\ref{tab:data_variables} for all available variables. All
variables are available from about the year 2000 onwards, but some time-series go as far
back as 1960. The data is in a format perfect for time-series regressions

## Usage

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
