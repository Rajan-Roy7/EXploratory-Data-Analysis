import pandas as pd

def remove_duplicates(df_copy):
    """
    Removes duplicate rows from a DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame from which to remove duplicates.

    Returns:
    pd.DataFrame: A DataFrame with duplicates removed.
    """
    # Remove duplicates
    df_no_duplicates = df_copy.drop_duplicates()

    return df_no_duplicates

#This function is used to read the data inputed from user and calling the main function
def data_read(df):
    df_copy = df.copy()
    result = remove_duplicates(df_copy)
    return result