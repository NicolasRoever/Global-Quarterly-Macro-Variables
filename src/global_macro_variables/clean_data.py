from functools import reduce

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def turn_daily_time_series_into_quarterly_data(data):
    """This function turns daily data into quarterly data by taking the quarterly
    mean.
    """
    # Create a dictionary of old and new column names
    rename_dict = {
        col: col + "_Quarterly_Mean" if col != "Date" else col for col in data.columns
    }

    output_data = (
        data.dropna().resample("Q", on="Date").mean().rename(columns=rename_dict)
    )

    # Convert the index to a 'Date_Quarterly' column
    output_data["Date_Quarterly"] = output_data.index.to_period("Q")

    # Reset the index
    return output_data.reset_index(drop=True)


def resample_daily_time_series_data_for_multiple_countries_to_quarterly(
    data,
    method="mean",
):
    """Resample the data on a quarterly basis for each country."""
    # Group by 'Country' and resample on a quarterly basis

    data_resampled = (
        data.groupby("Country").resample("Q", on="Date").mean().reset_index()
    )

    data_resampled["Date_Quarterly"] = data_resampled["Date"].dt.to_period("Q")

    return data_resampled


def left_join_dataframes(*dfs, on="Date_Quarter"):
    """Left join all dataframes based on the 'Date' column."""
    # Use reduce to left join all dataframes
    return reduce(
        lambda left, right: pd.merge(
            left,
            right,
            on=on,
            how="left",
            validate="many_to_one",
        ),
        dfs,
    )


def _make_missing_values_heatmap(data, data_name, index=None):
    """Generates a heatmap indicating the presence of 0 values in the DataFrame.

    Parameters:
        data (DataFrame): The pandas DataFrame to analyze.
        data_name (str): The name of the DataFrame.

    Returns:
        None

    """
    if index:
        data = data.set_index(index)

    # Create a DataFrame indicating 0 and infinity values
    data = data.isnull()

    # Create the heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(data, cbar=False, cmap="viridis")
    plt.title("Missing Values in Dataset " + data_name)
    plt.show()


def check_dataframe_rows(df: pd.DataFrame, num_rows: int):
    """Raises an error if DataFrame does not have a certain number of rows."""
    if len(df) != num_rows:
        msg = f"DataFrame should have {num_rows} rows, but it has {len(df)} rows."
        raise ValueError(
            msg,
        )


def merge_all_OECD_dataframes_for_final_output(
    quarterly_gdp_usd,
    cpi,
    debt_by_gdp,
    real_quarterly_gva,
    current_account,
):
    """This function merges all the dataframes for the final output."""
    merged_data_1 = pd.merge(
        quarterly_gdp_usd,
        cpi,
        on=["REF_AREA", "Date"],
        how="left",
        validate="one_to_one",
    )

    check_dataframe_rows(merged_data_1, quarterly_gdp_usd.shape[0])

    merged_data_2 = pd.merge(
        merged_data_1,
        debt_by_gdp,
        on=["REF_AREA", "Date"],
        how="left",
        validate="one_to_one",
    )

    check_dataframe_rows(merged_data_2, merged_data_1.shape[0])

    merged_data_3 = pd.merge(
        merged_data_2,
        real_quarterly_gva,
        on=["REF_AREA", "Date"],
        how="left",
        validate="one_to_one",
    )

    check_dataframe_rows(merged_data_3, merged_data_2.shape[0])

    merged_data_4 = pd.merge(
        merged_data_3,
        current_account,
        on=["REF_AREA", "Date"],
        how="left",
        validate="one_to_one",
    )

    check_dataframe_rows(merged_data_4, merged_data_3.shape[0])

    return merged_data_4


def merge_OECD_data_with_fred_10y_interest_rates(oecd_data, fred_interest_rates):
    """This function merges the OECD data with the FRED 10y interest rates."""
    merged_data = pd.merge(
        oecd_data,
        fred_interest_rates,
        on=["Date_Quarterly", "Country"],
        how="left",
        validate="one_to_one",
    )

    check_dataframe_rows(merged_data, oecd_data.shape[0])

    return merged_data


def merge_quarterly_fred_dataseries(vix, nasdaq, three_month_us_treasuries):
    """This function merges the quarterly FRED dataseries."""
    check_column_exists(vix, "Date_Quarterly")
    check_column_exists(nasdaq, "Date_Quarterly")
    check_column_exists(three_month_us_treasuries, "Date_Quarterly")

    merged_data_1 = pd.merge(
        nasdaq,
        vix,
        on=["Date_Quarterly"],
        how="left",
        validate="one_to_one",
    )

    check_dataframe_rows(merged_data_1, nasdaq.shape[0])

    merged_data_2 = pd.merge(
        merged_data_1,
        three_month_us_treasuries,
        on=["Date_Quarterly"],
        how="left",
        validate="one_to_one",
    )

    check_dataframe_rows(merged_data_2, merged_data_1.shape[0])

    _make_missing_values_heatmap(
        merged_data_2,
        "Merged Quarterly FRED Data",
        index="Date_Quarterly",
    )

    return merged_data_2


def check_column_exists(df: pd.DataFrame, column: str = "Quarterly_Date"):
    """Raises an error if DataFrame does not have a column named 'quarterly_date'."""
    if column not in df.columns:
        msg = f"DataFrame should have a column named '{column}', but it was not found."
        raise ValueError(
            msg,
        )
