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


# df= pd.read_csv("original.csv")
# cleaned_credit_df = read_data(df)
# # df.shape
# # cleaned_credit_df.shape
# print(df.isna().sum())
# print("/n -----------------------------------------")
# print(cleaned_credit_df.isna().sum())

import datacleaner
print(datacleaner.__version__)
