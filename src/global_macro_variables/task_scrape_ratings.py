from global_macro_variables.config import (
    BLD,
    COUNTRY_TABLE_ID_FOR_MOODY_RATING,
    COUNTRY_URL_FOR_RATINGS_DICTIONARY,
)
from global_macro_variables.scrape_ratings import get_all_ratings_from_countryeconomy


def task_scrape_ratings_for_all_countries(
    countries=COUNTRY_TABLE_ID_FOR_MOODY_RATING.keys(),
    country_url_dictionary=COUNTRY_URL_FOR_RATINGS_DICTIONARY,
    country_table_id_dictionary=COUNTRY_TABLE_ID_FOR_MOODY_RATING,
    rating_provider="Moodys",
    produces=BLD / "ratings_moodys.pkl",
):
    data = get_all_ratings_from_countryeconomy(
        countries,
        rating_provider,
        country_url_dictionary,
        country_table_id_dictionary,
    )

    data.to_pickle(produces)
