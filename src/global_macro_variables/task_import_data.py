from global_macro_variables.config import FRED_API_KEY, FRED_INTEREST_RATE_SERIES, BLD, OECD_QUARTERLY_GDP_USD_XML_QUERY_LINK , OECD_QUARTERLY_CURRENT_ACCOUNT_QUERY_LINK, EUROSTAT_CPI_QUARTERLY_QUERY_LINK, OECD_REAL_QUARTERLY_GDP_QUERY_LINK
from global_macro_variables.import_data import import_10y_yields_data_series_from_fred, import_quarterly_gdp_data_in_USD_from_oecd, import_quarterly_current_account_from_OECD, import_real_quarterly_gdp_data_from_oecd, import_quarterly_CPI_data_from_oecd


import pandas as pd


def task_import_fred_series(series_id = FRED_INTEREST_RATE_SERIES, 
                            api_key = FRED_API_KEY, 
                            produces= BLD / 'fred_test_data.csv'):
    

    export_data = pd.DataFrame()

    for key, value in series_id.items():
        data = import_10y_yields_data_series_from_fred(value, api_key)
        data['Country'] = key
        export_data =pd.concat([export_data, data])
        

    export_data.to_csv(produces)

def task_import_quarterly_CPI_data_from_oecd(query_link = EUROSTAT_CPI_QUARTERLY_QUERY_LINK,
                                             produces = BLD / 'eurostat_cpi.csv'):
    
    data = import_quarterly_CPI_data_from_oecd(query_link)

    data.to_csv(produces)


def task_import_quarterly_gdp_data_USD_from_oecd(query_link = OECD_QUARTERLY_GDP_USD_XML_QUERY_LINK , 
                                             produces = BLD / 'oecd_gdp_USD.csv'):

    data = import_quarterly_gdp_data_in_USD_from_oecd(query_link)


    data.to_csv(produces)   



def task_import_current_account_data_from_oecd(query_link= OECD_QUARTERLY_CURRENT_ACCOUNT_QUERY_LINK, 
                                              produces = BLD / 'oecd_current_account.csv'):

    data = import_quarterly_current_account_from_OECD(query_link)

    data.to_csv(produces)





def task_import_real_quarterly_gdp_data_from_oecd(query_link = OECD_REAL_QUARTERLY_GDP_QUERY_LINK, 
                                                 produces = BLD / 'oecd_real_gdp.csv'):
    """This function imports the real quarterly GDP data from the OECD API."""
    data = import_real_quarterly_gdp_data_from_oecd(query_link)

    data.to_csv(produces)


    # I want FRED S&P 500

    # I want FRED CBOE VIX

    # I want FRED US short-term treasuries 