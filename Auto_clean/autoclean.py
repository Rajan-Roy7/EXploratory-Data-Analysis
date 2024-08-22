# autoclean.py
import pandas as pd
from datacleaner import autoclean  # Ensure this import points to the correct library or function

def data_clean(df_copy):
    """
    Clean the copied dataframe.

    Parameters:
    df_copy (pd.DataFrame): The DataFrame to be cleaned.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    cleaned_df = autoclean(df_copy)
    return cleaned_df

def read_data(df):
    df_copy = df.copy()
    result = data_clean(df_copy)
    return result




