import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import category_encoders as ce

def encode_columns(df_copy, categorical_cols, encoding_type):
    """
    Encode the categorical columns of a DataFrame using the specified encoding type.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame containing both categorical and non-categorical columns.
    categorical_cols (list): A list of column names to be encoded.
    encoding_type (str): The type of encoding to apply ('one_hot' or 'binary').
    
    Returns:
    pd.DataFrame: The DataFrame with encoded features and original non-categorical columns.
    """
    
    
    # Perform encoding based on the specified type
    match encoding_type:
        case 'one_hot':
            # Create an instance of the OneHotEncoder
            ohe = OneHotEncoder()
            
            # Fit and transform the categorical columns
            encoded_cols = ohe.fit_transform(df_copy[categorical_cols])
            
            # Convert the sparse matrix to a dense DataFrame
            encoded_df = pd.DataFrame(encoded_cols.toarray(), columns=ohe.get_feature_names_out(categorical_cols))
        
        case 'binary':
            # Create an instance of the BinaryEncoder
            binary_encoder = ce.BinaryEncoder(cols=categorical_cols)
            
            # Fit and transform the categorical columns
            encoded_df = binary_encoder.fit_transform(df_copy[categorical_cols])
        
        case _:
            raise ValueError(f"Unsupported encoding type: {encoding_type}")

    # Concatenate the encoded features to the original DataFrame
    df_encoded = pd.concat([df_copy, encoded_df], axis=1)
    
    # Drop the original categorical columns
    df_copy = df_encoded.drop(categorical_cols, axis=1)
    
    # Return the final DataFrame
    return df_copy

#This function is for reading the inputed data from user and calling the main function
def data_read(df, categorical_cols, encoding_type):
    df_copy = df.copy()
    result = encode_columns(df_copy, categorical_cols, encoding_type)
    return result