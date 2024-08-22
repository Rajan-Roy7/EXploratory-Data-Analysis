import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from collections import Counter
# %matplotlib inline

def outlier(df_copy, n, features):
    """
    z_score_method
    Takes a dataframe df of features and returns an index list corresponding to the observations 
    containing more than n outliers according to the z-score method.
    """
    outlier_list = []
    
    for column in features:
        # calculate the mean and standard deviation of the data frame
        data_mean = df_copy[column].mean()
        data_std = df_copy[column].std()
        threshold = 3
        
        z_score = abs((df_copy[column] - data_mean) / data_std)
        
        # Determining a list of indices of outliers for feature column        
        outlier_list_column = df_copy[z_score > threshold].index.tolist()
        # appending the found outlier indices for column to the list of outlier indices 
        outlier_list.extend(outlier_list_column)
        
    # selecting observations containing more than n outliers
    outlier_list = Counter(outlier_list)        
    multiple_outliers = list(k for k, v in outlier_list.items() if v > n)
    
    # Calculate the number of outlier records
    #print('Total number of outliers:', len(multiple_outliers))
    return multiple_outliers
#This function is used to take the input from user and calling the main function
def data_read(df, n, features):
    df_copy = df.copy()
    result = outlier(df_copy, 1, features)
    return result