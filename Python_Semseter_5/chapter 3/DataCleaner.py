import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

class DataCleaner:
    def __init__(self,numeric_fill='mean',categorical_fill='mode',date_columns=None,z_score_threshold=3):
        self.numeric_fill = numeric_fill
        self.categorical_fill = categorical_fill
        self.date_columns = date_columns or []
        self.z_score_threshold = z_score_threshold

    def clean(self, df:pd.DataFrame)->pd.DataFrame:
        # df = self.numeric_fill(df)
        df = self.handle_missing_values(df)
        df = self.convert_dates(df)
        df = self.remove_outliers(df)
        return df

    def handle_missing_values(self, df:pd.DataFrame) -> pd.DataFrame:
        for col in df.select_dtypes(include=np.number).columns:
            if self.numeric_fill == 'mean':
                df[col] = df[col].fillna(df[col].mean())
            elif self.numeric_fill == 'median':
                df[col] = df[col].fillna(df[col].median())
            elif isinstance(self.numeric_fill, (int,float)):
                df[col] = df[col].fillna(self.numeric_fill)
            
        for col in df.select_dtypes(include=object).columns:
            if self.categorical_fill == 'mode':
                df[col] = df[col].fillna(df[col].mode())
            elif isinstance(self.categorical_fill, str):
                df[col] = df[col].fillna(self.categorical_fill)
        return df
    
    def convert_dates(self, df:pd.DataFrame) -> pd.DataFrame:
        for col in self.date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col],errors='coerce')
        return df

    def remove_outliers(self, df:pd.DataFrame) ->pd.DataFrame:
        numeric_cols = df.select_dtypes(include = np.number).columns
        for col in numeric_cols:
            mean, std = df[col].mean(),df[col].std()
            z_scores = (df[col] - mean) / std
            df = df[z_scores.abs() <= self.z_score_threshold] 
        return df
    
if __name__ == "__main__":
    try:
        df=pd.read_csv('sample_data.csv')
        cleaner = DataCleaner(date_columns='join_date')
        cleaned_df = cleaner.clean(df)
        cleaned_df.to_csv('cleaned_data.csv',index=False)
        print("Data cleaning completed")
    except Exception as e:
        print(f"An error occurred: {e}")
