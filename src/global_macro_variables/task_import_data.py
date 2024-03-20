import pandas as pd
from pytask import task

from global_macro_variables.config import (
    BLD,
    FRED_API_KEY,
    FRED_INTEREST_RATE_SERIES,
    OECD_DATA_QUERY_LINKS,
    OECD_VARIABLE_NAMES,
)
from global_macro_variables.import_data import (
    import_10y_yields_data_series_from_fred,
    import_data_series_from_fred,
    import_quarterly_data_from_OECD,
)

for key in OECD_DATA_QUERY_LINKS:
    query_link = OECD_DATA_QUERY_LINKS[key]
    variable_name = OECD_VARIABLE_NAMES[key]

    @task(id=key)
    def task_import_quarterly_oecd_data(
        produces=BLD / key,
        query_link=query_link,
        variable_name=variable_name,
    ):
        print(variable_name)
        data = import_quarterly_data_from_OECD(query_link, variable_name)

        data.to_pickle(produces)


def task_import_vix_data_from_fred(
    series_id="VIXCLS",
    api_key=FRED_API_KEY,
    produces=BLD / "vix.pkl",
):
    data = import_data_series_from_fred(series_id, "VIX_Daily_Close", api_key)

    data.to_pickle(produces)


def task_import_3_month_US_treasuries_from_fred(
    series_id="DGS3MO",
    api_key=FRED_API_KEY,
    produces=BLD / "3_month_US_treasuries.pkl",
):
    data = import_data_series_from_fred(series_id, "3_Month_US_Treasury_Yield", api_key)

    data.to_pickle(produces)


def task_import_nasdaq_from_fred(
    series_id="NASDAQCOM",
    api_key=FRED_API_KEY,
    produces=BLD / "nasdaq.pkl",
):
    data = import_data_series_from_fred(series_id, "NASDAQ_Daily_Close", api_key)

    data.to_pickle(produces)


def task_import_fred_interest_series(
    series_id=FRED_INTEREST_RATE_SERIES,
    api_key=FRED_API_KEY,
    produces=BLD / "10_year_maturity_bond_yields.pkl",
):
    export_data = pd.DataFrame()

    for key, value in series_id.items():
        data = import_10y_yields_data_series_from_fred(value, api_key)
        data["Country"] = key
        export_data = pd.concat([export_data, data])

    export_data.to_pickle(produces)
