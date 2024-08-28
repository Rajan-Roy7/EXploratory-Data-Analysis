from sklearn.decomposition import PCA
import pandas as pd

def apply_pca(df, n_components):
    """
    Applies PCA to the given DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to apply PCA to.
    n_components (int): The number of components to keep.

    Returns:
    pd.DataFrame: A DataFrame containing the transformed data.
    """
    # Initialize PCA with the specified number of components
    pca = PCA(n_components=n_components)
    numerical_df = df.select_dtypes(include=['number'])
    # Fit the PCA model to the data and transform it
    # Converting DataFrame to NumPy array for PCA, then back to DataFrame
    df_transformed = pd.DataFrame(
        pca.fit_transform(numerical_df),
        columns=[f'PC{i+1}' for i in range(n_components)]
    )
    
    return df_transformed
def data_read(df, n_components):
    df_copy = df.copy()
    result =apply_pca(df_copy, n_components)
    return result