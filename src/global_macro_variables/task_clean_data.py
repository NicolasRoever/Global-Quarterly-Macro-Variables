

def generate_output_data(data, method = "mean"):
    """This function generates the output data by taking the mean of the input data."""
    # Create a dictionary of old and new column names
    rename_dict = {col: col + '_Quarterly_Mean' if col != 'Date' else col for col in data.columns}
    
    data = data.resample('Q', on = "Date").mean().rename(columns=rename_dict, inplace=True)

    return data