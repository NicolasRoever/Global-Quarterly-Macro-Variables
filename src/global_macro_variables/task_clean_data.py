import pandas as pd

from global_macro_variables.clean_data import (
    _make_missing_values_heatmap,
    check_dataframe_rows,
    generate_long_format_rating_data,
    merge_all_OECD_dataframes_for_final_output,
    merge_OECD_data_and_moody_rating_data,
    merge_OECD_data_with_fred_10y_interest_rates,
    merge_quarterly_fred_dataseries,
    resample_daily_time_series_data_for_multiple_countries_to_quarterly,
    turn_daily_time_series_into_quarterly_data,
)
from global_macro_variables.config import (
    BLD,
    COUNTRY_CODES_AND_NAMES_MAPPING,
    COUNTRY_MAPPING_RATING_DATA_VS_OECD_DATA_FOR_MERGING,
    TOP_DIR,
)


def task_resample_fred_10y_interest_rate_to_quarterly_data(
    depends_on=BLD / "10_year_maturity_bond_yields.pkl",
    produces=BLD / "10_year_maturity_bond_yields_quarterly.pkl",
):
    data = pd.read_pickle(depends_on)

    data["Date"] = pd.to_datetime(data["Date"])

    data_resampled = (
        resample_daily_time_series_data_for_multiple_countries_to_quarterly(data)
    )
    data_resampled.to_pickle(produces)


dependencies_task_generate_output_data = {
    "quarterly_gdp_USD": BLD / "quarterly_gdp_USD.pkl",
    "debt_by_gdp": BLD / "debt_by_gdp.pkl",
    "current_account": BLD / "current_account.pkl",
    "real_quarterly_gva": BLD / "real_quarterly_gva.pkl",
    "moody_ratings_data": BLD / "ratings_data_long_format.pkl",
    "cpi": BLD / "cpi.pkl",
    "vix": BLD / "vix.pkl",
    "3_month_US_treasuries": BLD / "3_month_US_treasuries.pkl",
    "nasdaq": BLD / "nasdaq.pkl",
    "10_year_maturity_bond_yields": BLD / "10_year_maturity_bond_yields_quarterly.pkl",
}


def task_generate_output_data(
    depends_on=dependencies_task_generate_output_data,
    country_mapping_codes_names=COUNTRY_CODES_AND_NAMES_MAPPING,
    country_mapping_rating_vs_oecd_data=COUNTRY_MAPPING_RATING_DATA_VS_OECD_DATA_FOR_MERGING,
    produces=[  # noqa
        BLD / "Quarterly Macroeconomic Variables.xlsx",
        TOP_DIR / "Quarterly Macroeconomic Variables.xlsx",
    ],
):
    """This function generates the output data by taking the mean of the input data."""
    # Import Data

    quarterly_gdp_USD = pd.read_pickle(depends_on["quarterly_gdp_USD"])  # noqa
    debt_by_gdp = pd.read_pickle(depends_on["debt_by_gdp"])
    current_account = pd.read_pickle(depends_on["current_account"])
    real_quarterly_gva = pd.read_pickle(depends_on["real_quarterly_gva"])
    cpi = pd.read_pickle(depends_on["cpi"])
    moody_ratings_data = pd.read_pickle(depends_on["moody_ratings_data"])
    vix = pd.read_pickle(depends_on["vix"])
    three_month_us_treasuries = pd.read_pickle(depends_on["3_month_US_treasuries"])
    nasdaq = pd.read_pickle(depends_on["nasdaq"])
    ten_year_maturity_bond_yields = pd.read_pickle(
        depends_on["10_year_maturity_bond_yields"],
    )

    # Merge OECD Data
    merged_OECD_data = merge_all_OECD_dataframes_for_final_output(
        quarterly_gdp_USD,
        cpi,
        debt_by_gdp,
        real_quarterly_gva,
        current_account,
    )

    merged_OECD_data["Country"] = merged_OECD_data["REF_AREA"].map(
        country_mapping_codes_names,
    )

    merged_OECD_data = merged_OECD_data.dropna(subset=["Country"])

    # Add Rating Data

    merged_OECD_data = merge_OECD_data_and_moody_rating_data(
        merged_OECD_data,
        moody_ratings_data,
        COUNTRY_MAPPING_RATING_DATA_VS_OECD_DATA_FOR_MERGING,
    )

    # Add Quarterly Date

    merged_OECD_data["Date_Quarterly"] = pd.to_datetime(
        merged_OECD_data["Date"],
    ).dt.to_period("Q")

    # Add 10y interest rates

    data_with_interest_rates = merge_OECD_data_with_fred_10y_interest_rates(
        merged_OECD_data,
        ten_year_maturity_bond_yields[
            ["Date_Quarterly", "Country", "10y_Maturity_Bond_Yield"]
        ],
    )

    # Merge and add FRED data

    vix_quarterly_data = turn_daily_time_series_into_quarterly_data(vix)
    nasdaq_quarterly_data = turn_daily_time_series_into_quarterly_data(nasdaq)
    three_month_us_treasuries_quarterly_data = (
        turn_daily_time_series_into_quarterly_data(three_month_us_treasuries)
    )

    fred_data = merge_quarterly_fred_dataseries(
        vix=vix_quarterly_data,
        nasdaq=nasdaq_quarterly_data,
        three_month_us_treasuries=three_month_us_treasuries_quarterly_data,
    )

    final_data = pd.merge(
        data_with_interest_rates,
        fred_data,
        on="Date_Quarterly",
        how="left",
        validate="many_to_one",
    )

    check_dataframe_rows(final_data, data_with_interest_rates.shape[0])

    _make_missing_values_heatmap(final_data, "Final Data")

    final_data = final_data.dropna(subset=["REF_AREA"])

    final_data.to_excel(produces[0], index=False)
    final_data.to_excel(produces[1], index=False)


def task_generate_long_format_rating_data(
    depends_on=BLD / "ratings_moodys.pkl",
    produces=BLD / "ratings_data_long_format.pkl",
):
    ratings_data = pd.read_pickle(depends_on)

    ratings_data_long_format = generate_long_format_rating_data(ratings_data)

    ratings_data_long_format.to_pickle(produces)
