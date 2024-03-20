from global_macro_variables.config import FRED_API_KEY

from fredapi import Fred
import pandas as pd
import requests
import xmltodict



def import_10y_yields_data_series_from_fred(series_id, api_key=FRED_API_KEY):
    """Import a data series from FRED."""

    # Import the data series

    fred = Fred(api_key=api_key)
    data = fred.get_series(series_id)

    # Convert the series to a DataFrame and reset the index
    data = data.reset_index()

    # Rename the columns
    data.columns = ['Date', '10y_Bond_Yield']

    # Ensure 'date' is of type datetime and 'value' is of type float
    data['Date'] = pd.to_datetime(data['Date'])
    data['10y_Maturity_Bond_Yield'] = data['10y_Bond_Yield'].astype(float)

    return data



def import_data_series_from_fred(series_id, column_name, api_key=FRED_API_KEY):
    """Import a data series from FRED.

    Args: 
    series_id: str THis is the ID for the series in FRED
    column_name: str This is the name of the column in the dataframe that includes the value received 
    api_key: str This is the API key for the FRED API

    Returns:
    data: pd.DataFrame This is the dataframe with the data series
        columns: Date (pd.datetime), 
                column_name (float)
    """

    # Import the data series

    fred = Fred(api_key=api_key)
    data = fred.get_series(series_id, start_date = pd.to_datetime("1945-01-01"))

    # Convert the series to a DataFrame and reset the index
    data = data.reset_index()

    # Rename the columns
    data.columns = ['Date', column_name]

    # Ensure 'date' is of type datetime and 'value' is of type float
    data['Date'] = pd.to_datetime(data['Date'])
    data[column_name] = data[column_name].astype(float)

    return data[['Date', column_name]]


def import_quarterly_data_from_OECD(xml_query_link, variable_name):
    """This function imports quarterly data from the OECD API."""
    r = requests.get(xml_query_link)
    dictionary_data = xmltodict.parse(r.content)

    data = clean_oecd_xml_response(dictionary_data)

    data = data.rename(columns={"@value": variable_name})

    #Correct datatypes
    data["Date"] = pd.to_datetime(data["TIME_PERIOD"])
    data[variable_name] = data[variable_name].astype(float)

    return data[["Date", variable_name]]



def import_quarterly_gdp_data_in_USD_from_oecd(xml_query_link):


    r = requests.get(xml_query_link)
    dictionary_data = xmltodict.parse(r.content)

    data = clean_oecd_xml_response(dictionary_data)

    data = data.rename(columns={"@value": "GDP_in_USD_Current_Prices"})

    #Make correct datatypes
    data["Data"] = pd.to_datetime(data["TIME_PERIOD"])
    data["GDP_in_USD_Current_Prices"] = data["GDP_in_USD_Current_Prices"].astype(float)

    return data[["Date", "GDP_in_USD_Current_Prices"]]


def import_quarterly_CPI_data_from_oecd(xml_query_link):
     
        r = requests.get(xml_query_link)
        dictionary_data = xmltodict.parse(r.content)
    
        data = clean_oecd_xml_response(dictionary_data)
    
        data = data.rename(columns={"@value": "Eurostat_CPI_Annualised Growth_Rate"})

        #Correct datatypes
        data["Date"] = pd.to_datetime(data["TIME_PERIOD"])
        data["Eurostat_CPI_Annualised Growth_Rate"] = data["Eurostat_CPI_Annualised Growth_Rate"].astype(float)
    
        return data[["Date", "Eurostat_CPI_Annualised Growth_Rate"]]


def import_real_quarterly_gdp_data_from_oecd(xml_query_link):
    """This function imports the real quarterly GDP data from the OECD API."""
    r = requests.get(xml_query_link)
    dictionary_data = xmltodict.parse(r.content)

    data = clean_oecd_xml_response(dictionary_data)

    data = data.rename(columns={"@value": "Real_Quarterly_GVA_in_Domestic_Currency"})

    #Correct datatypes
    data["Date"] = pd.to_datetime(data["TIME_PERIOD"])
    data["Real_Quarterly_GVA_in_Domestic_Currency"] = data["Real_Quarterly_GVA_in_Domestic_Currency"].astype(float)

    return data[["Date", "Real_Quarterly_GVA_in_Domestic_Currency"]]


def import_quarterly_public_debt_as_percent_of_gdp_data_from_oecd(xml_query_link):
    
        r = requests.get(xml_query_link)
        dictionary_data = xmltodict.parse(r.content)
    
        data = clean_oecd_xml_response(dictionary_data)
    
        data = data.rename(columns={"@value": "Public_Debt_as_%_of_GDP"})

        #Correct datatypes
        data["Date"] = pd.to_datetime(data["TIME_PERIOD"])
        data["Public_Debt_as_%_of_GDP"] = data["Public_Debt_as_%_of_GDP"].astype(float)
    
        return data[["Date", "Public_Debt_as_%_of_GDP"]]


def import_quarterly_current_account_from_OECD(xml_query_link):
     
        r = requests.get(xml_query_link)
        dictionary_data = xmltodict.parse(r.content)
    
        data = clean_oecd_xml_response(dictionary_data)
    
        data = data.rename(columns={"@value": "Current_Account_in_USD"})

        #Correct datatypes
        data["Date"] = pd.to_datetime(data["TIME_PERIOD"])
        data["Current_Account_in_USD"] = data["Current_Account_in_USD"].astype(float)

        return data[["Date", "Current_Account_in_USD"]]




def clean_oecd_xml_response(data_as_dictionary):
    """This function returns a dataframe from the data received from OECD's API, which has to previously be converted into a dictionary."""


    full_data = pd.DataFrame()
    

    for i in range(len(data_as_dictionary['message:GenericData']['message:DataSet']['generic:Obs'])):
        observation_dictionary = data_as_dictionary['message:GenericData']['message:DataSet']['generic:Obs'][i]

        #1. obskey
        obs_key_data = observation_dictionary['generic:ObsKey']['generic:Value']
        obs_key_dict = {d['@id']: d['@value'] for d in obs_key_data}
        #Obs value
        obs_value_dict = observation_dictionary['generic:ObsValue']
        #ObsAttributes
        obs_attributes_data = observation_dictionary['generic:Attributes']['generic:Value']
        obs_attributes_dict = {d['@id']: d['@value'] for d in obs_attributes_data}  

        full_observation = {**obs_key_dict , **obs_value_dict, **obs_attributes_dict}
        full_data = pd.concat([full_data, pd.DataFrame(full_observation, index=[0])])

    return full_data





