import pandas as pd

def turn_daily_time_series_into_quarterly_data(data, method = "mean"):

    """This function turns daily data into quarterly data by taking th quartely mean."""

    # Create a dictionary of old and new column names
    rename_dict = {col: col + '_Quarterly_Mean' if col != 'Date' else col for col in data.columns}
    
    data = data.resample('Q', on = "Date").mean().rename(columns=rename_dict, inplace=True)

    return data