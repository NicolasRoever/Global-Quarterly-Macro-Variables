from functools import reduce

import matplotlib.pyplot as plt
import numpy as np
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


def generate_long_format_rating_data(
    imported_data,
    start_time="1950-01-01",
    end_time="2024-01-01",
):
    """This function takes in the dataframe generated by the get_all_ratings_from_countryeconomy.
    It returns a dataframe in long format with an entry for every day between the start_time and end_time,
    whit the rating for that day.

    Args: imported_data (pandas.DataFrame): The dataframe generated by the get_all_ratings_from_countryeconomy function
            start_time (str): The start date for the long format dataframe
            end_time (str): The end date for the long format dataframe

    Returns: cleaned_data (pandas.DataFrame): A dataframe
        columns: Date (datetime): the date of the rating
                    Rating_Letter_Moody (str): the rating
                    Country (str): The Country of the rating

    """
    dates = pd.date_range(start=start_time, end=end_time)

    countries = imported_data["Country"].unique()

    result = pd.DataFrame()

    for country in countries:
        # Filter the imported data for the current country
        country_data = imported_data[imported_data["Country"] == country].sort_values(
            by="Date",
        )

        # Create a DataFrame for the current country with the date range
        long_rating_country = pd.DataFrame(dates, columns=["Date"])
        long_rating_country["Country"] = country

        # Initialize the rating column with np.nan
        long_rating_country["Rating_Letter_Moody"] = np.nan

        # Update the rating columns based on the imported data
        for _index, row in country_data.iterrows():
            long_rating_country.loc[
                long_rating_country["Date"] >= row["Date"],
                "Rating_Letter_Moody",
            ] = row["Rating"]
        check_duplicates(long_rating_country[["Date", "Country"]])

        # Append the DataFrame for the current country to the result DataFrame
        result = pd.concat([result, long_rating_country], ignore_index=True)

    return result


def merge_OECD_data_and_moody_rating_data(
    oecd_data,
    moody_rating_data,
    country_mapping_moody_names_to_oecd,
):
    """This function merges the OECD data with the Moody rating data."""
    moody_rating_data["Country"] = moody_rating_data["Country"].map(
        country_mapping_moody_names_to_oecd,
    )

    merged_data = pd.merge(
        oecd_data,
        moody_rating_data,
        on=[
            "Country",
            "Date",
        ],
        how="left",
        validate="one_to_one",
    ).rename(columns={"Rating_Letter_Moody": "Rating_Moody_Last_Quarter_Day"})

    check_dataframe_rows(merged_data, oecd_data.shape[0])

    return merged_data


def check_na_values(column):
    """Check if there are NA values in the specified column of the DataFrame."""
    if column.isna().any():
        msg = "Column contains NA values."
        raise ValueError(msg)


def check_duplicates(df):
    """Check if there are duplicate rows in the DataFrame."""
    duplicates = df[df.duplicated(keep=False)]
    if not duplicates.empty:
        print("Duplicate rows:")
        print(duplicates)
        msg = "DataFrame contains duplicate rows."
        raise ValueError(msg)
