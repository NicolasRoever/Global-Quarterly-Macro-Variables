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



def import_quarterly_gdp_data_in_USD_from_oecd(xml_query_link):


    r = requests.get(xml_query_link)
    dictionary_data = xmltodict.parse(r.content)

    data = clean_oecd_xml_response(dictionary_data)

    data = data.rename(columns={"@value": "GDP_in_USD_Current_Prices"})

    return data


def import_real_quarterly_gdp_data_from_oecd(xml_query_link):
    """This function imports the real quarterly GDP data from the OECD API."""
    r = requests.get(xml_query_link)
    dictionary_data = xmltodict.parse(r.content)

    data = clean_oecd_xml_response(dictionary_data)

    data = data.rename(columns={"@value": "Real_Quarterly_GDP_in_Domestic_Currency"})

    return data



def import_quarterly_public_debt_as_percent_of_gdp_data_from_oecd(xml_query_link):
    
        r = requests.get(xml_query_link)
        dictionary_data = xmltodict.parse(r.content)
    
        data = clean_oecd_xml_response(dictionary_data)
    
        data = data.rename(columns={"@value": "Public_Debt_as_%_of_GDP"})
    
        return data

def import_quarterly_current_account_from_OECD(xml_query_link):
     
        r = requests.get(xml_query_link)
        dictionary_data = xmltodict.parse(r.content)
    
        data = clean_oecd_xml_response(dictionary_data)
    
        data = data.rename(columns={"@value": "Current_Account_in_USD"})
    
        return data




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




