import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder


def handle_missing_categorical(df_copy, categorical_cols, strategy):
    """
    Handle missing values in categorical columns using the specified strategy.

    Parameters:
    df_copy(which is copy of original df) (pd.DataFrame): The input DataFrame.
    categorical_cols (list): List of categorical column names.
    strategy (str): The strategy to use ('mode', 'linear_regression', 'knn', 'delete', 'false').

    Returns:
    pd.DataFrame: The DataFrame with missing values handled.df_copy
    """
    
    def impute_mode(df_copy, col):
        mode_value = df_copy[col].mode()[0]
        df_copy[col].fillna(mode_value, inplace=True)
    
    
    def delete_rows(df_copy, col):
        df_copy.dropna(subset=[col], inplace=True)
    
    def mark_as_false(df_copy, col):
        df_copy[col].fillna('False', inplace=True)
    
    match strategy:
        case 'mode':
            for col in categorical_cols:
                impute_mode(df_copy, col)
       
        case 'delete':
            for col in categorical_cols:
                delete_rows(df_copy, col)
        case 'false':
            for col in categorical_cols:
                mark_as_false(df_copy, col)
        case _:
            raise ValueError(f"Strategy {strategy} not recognized. Choose from 'mode', 'linear_regression', 'knn', 'delete', 'false'")

    return df_copy

#This function for reading the data inputed from user and calling the main function
def data_read(df, categorical_cols, strategy):
    df_copy = df.copy()
    result = handle_missing_categorical(df_copy, categorical_cols, strategy)
    return result

