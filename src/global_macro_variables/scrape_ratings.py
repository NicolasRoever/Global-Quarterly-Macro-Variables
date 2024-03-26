"""Scrape Sovereign Bond Ratings from https://countryeconomy.com/ratings."""


import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_all_ratings_from_countryeconomy(
    country_name_list,
    rating_provider,
    country_name_url_dicionary,
    country_table_id_for_rating_provider_dictionary,
):
    result = pd.DataFrame()

    for country in country_name_list:
        print(country)
        data = get_ratings_from_countryeconomy(
            country,
            rating_provider,
            country_name_url_dicionary[country],
            country_table_id_for_rating_provider_dictionary[country],
        )
        result = pd.concat([result, data])

        result = pd.concat([result, data])

    return result


def get_raw_data_from_countryeconomy(country, table_id):
    """This function gets the raw data from countryeconomy.com
    Args:
    country: str: the country to get the data from, this has to be in the format as in the URL!
    table_id: str: the id of the table to get the data from.

    """
    country_url = f"https://countryeconomy.com/ratings/{country}"

    page = requests.get(country_url)

    # Check if the request was successful
    if page.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(page.text, "html.parser")

        # Find the table with the specified id
        table = soup.find("table", {"id": table_id})

        # Read the table into a pandas DataFrame
        return pd.read_html(str(table))[0]

    else:
        print("Failed to retrieve the webpage.")
        return None


def clean_scraped_table(raw_data, country, rating_provider="Moodys"):
    """This function cleans the raw data retrieved by the function get_raw_data_from_countryeconomy.

    Args: country: the name of the country, it is appended as a separate column
    rating_provider: the rating provider, it is appended as a separate column
    raw_data: the raw data retrieved by the function get_raw_data_from_countryeconomy

    Returns: pd.DataFrame: the cleaned data
        columns: "Date" (pd.Datetime): the date of the rating
                    "Rating" (str): the rating


    """
    # Joining Column Names from Multiindex
    raw_data.columns = [" ".join(col).strip() for col in raw_data.columns.values]

    # Create a dataframe only selecting the Long term foreign currency rating and the date
    raw_data_renamed = raw_data[
        [
            "Long term Rating Foreign currency Date",
            "Long term Rating Foreign currency Rating(Outlook)",
        ]
    ].rename(
        columns={
            "Long term Rating Foreign currency Date": "Date",
            "Long term Rating Foreign currency Rating(Outlook)": "Rating",
        },
    )

    # Add 'Country' and 'Rating Provider' columns

    df_clean = pd.DataFrame()
    df_clean["Date"] = pd.to_datetime(raw_data_renamed["Date"])
    df_clean["Rating"] = raw_data_renamed["Rating"].replace(
        r"\s*\([^)]*\)",
        "",
        regex=True,
    )
    df_clean["Country"] = country
    df_clean["Rating Provider"] = rating_provider

    return df_clean


def get_ratings_from_countryeconomy(
    country,
    rating_provider,
    country_name_for_url,
    country_table_id_for_rating_provider,
):
    """This function gets the ratings from countryeconomy.com and cleans the data.

    Args: country: the name of the country to be appended as a dataframe column
        rating_provider: the rating provider to be appended as a dataframe column
        country_name_for_url: the name of the country to be used in the URL
        country_table_id_for_rating_provider: the table id for the rating provider
    """
    raw_data = get_raw_data_from_countryeconomy(
        country_name_for_url,
        country_table_id_for_rating_provider,
    )
    return clean_scraped_table(raw_data, country, rating_provider)
