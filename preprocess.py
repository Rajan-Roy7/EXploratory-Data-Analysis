import pandas as pd

class DataPreprocessor:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        
    def remove_duplicates(self):
        from duplicate_remove import data_read
        self.data = data_read(self.data)
        return self
        
    def encode(self, categorical_cols, encoding_type):
        from encoding import data_read
        self.data = data_read(self.data, categorical_cols, encoding_type)
        return self
        
    def handle_missing_values(self, numerical_cols, strategy):
        from missing_values import data_read
        self.data = data_read(self.data, numerical_cols, strategy)
        return self
        
    def handle_missing_categorical(self, categorical_cols, strategy):
        from missing_categorical import data_read
        self.data = data_read(self.data, categorical_cols, strategy)
        return self
        
    def normalize(self, numerical_cols, strategy):
        from numerical_normalisation import data_read
        self.data = data_read(self.data, numerical_cols, strategy)
        return self
        
    def detect_outliers(self, n, features):
        from outliers import data_read
        outliers_indices = data_read(self.data, n, features)
        self.data.drop(index=outliers_indices, inplace=True)
        return self
        
    def get_data(self) -> pd.DataFrame:
        return self.data
