from global_macro_variables.config import FRED_API_KEY, FRED_INTEREST_RATE_SERIES, BLD, OECD_DATA_QUERY_LINKS, OECD_VARIABLE_NAMES
from global_macro_variables.import_data import import_10y_yields_data_series_from_fred, import_quarterly_gdp_data_in_USD_from_oecd, import_quarterly_current_account_from_OECD, import_real_quarterly_gdp_data_from_oecd, import_quarterly_CPI_data_from_oecd, import_data_series_from_fred, import_quarterly_data_from_OECD


import pandas as pd
from pytask import task


def task_import_fred_series(series_id = FRED_INTEREST_RATE_SERIES, 
                            api_key = FRED_API_KEY, 
                            produces= BLD / 'fred_test_data.pickle'):
    

    export_data = pd.DataFrame()

    for key, value in series_id.items():
        data = import_10y_yields_data_series_from_fred(value, api_key)
        data['Country'] = key
        export_data =pd.concat([export_data, data])
        

    export_data.to_pieckle(produces)


for key in OECD_DATA_QUERY_LINKS.keys():

    @task(id=key)
    def task_import_quarterly_oecd_data(produces = BLD / key, 
                                        query_link_dictionary = OECD_DATA_QUERY_LINKS, 
                                    variable_name_dictionary = OECD_VARIABLE_NAMES):
        
        query_link = query_link_dictionary[key]
        variable_name = variable_name_dictionary[key]
        data = import_quarterly_data_from_OECD(query_link, variable_name)

        data.to_pkl(produces)




def task_import_quarterly_CPI_data_from_oecd(query_link = EUROSTAT_CPI_QUARTERLY_QUERY_LINK,
                                             produces = BLD / f'{output_file_name}'):
    
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


def task_import_s_and_p_500_data_from_fred(series_id = "SP500", 
                                          api_key = FRED_API_KEY, 
                                          produces = BLD / 's_and_p_500.pkl'):
    
    data = import_data_series_from_fred(series_id, "S&P_500_Daily_Close", api_key)

    data.to_pickle(produces)



def task_import_vix_data_from_fred(series_id = "VIXCLS", 
                              api_key = FRED_API_KEY, 
                              produces = BLD / 'vix.pkl'):
    
    data = import_data_series_from_fred(series_id, "VIX_Daily_Close", api_key)

    data.to_pickle(produces)


    
def task_import_3_month_US_treasuries_from_fred(series_id = "DGS3MO", 
                                           api_key = FRED_API_KEY, 
                                           produces = BLD / '3_month_US_treasuries.pkl'):
    
    data = import_data_series_from_fred(series_id, "3_Month_US_Treasury_Yield", api_key)

    data.to_pickle(produces)


def task_import_nasdaq_from_fred(series_id = "NASDAQCOM", 
                                 api_key = FRED_API_KEY, 
                                 produces = BLD / 'nasdaq.pkl'):
    
    data = import_data_series_from_fred(series_id, "NASDAQ_Daily_Close", api_key)

    data.to_pickle(produces)


