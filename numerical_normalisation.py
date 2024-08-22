import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def normalize(df_copy, numerical_cols, strategy):
    """
    Perform normalization on the specified numerical columns of a DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame to be normalized.
    numerical_cols (list): A list of the numerical column names to be normalized.
    method (str, optional): The normalization method to use, either 'z-score' or 'min-max'. Default is 'z-score'.

    Returns:
    pandas.DataFrame: The normalized DataFrame.
    """
    
    match strategy:
        case 'z-score':
            scaler = StandardScaler()
            df_copy[numerical_cols] = scaler.fit_transform(df_copy[numerical_cols])
        case 'min-max':
            for col in numerical_cols:
                min_value = df_copy[col].min()
                max_value = df_copy[col].max()
                df_copy[col] = (df_copy[col] - min_value) / (max_value - min_value)
        case _:
            raise ValueError("Invalid normalization method. Choose 'z-score' or 'min-max'.")

    return df_copy
#This function is used to call the main function and taking input from user 
def data_read(df, numerical_cols, strategy):
    df_copy = df.copy()
    result = normalize(df_copy, numerical_cols, strategy)
    return result