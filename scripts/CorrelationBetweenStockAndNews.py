import os
import pandas as pd
from textblob import TextBlob
import seaborn as sns

class CombinedAnalysis:
    def __init__(self, news_file, stock_file):
        self.news_file = news_file
        self.stock_file = stock_file
        self.news_df = pd.read_csv(news_file)
        self.stock_df = pd.read_csv(stock_file)
        
        # Print columns for debugging
        print("News DataFrame columns:", self.news_df.columns)
        print("Stock DataFrame columns:", self.stock_df.columns)

    def normalize_dates(self):
        # Print available columns for debugging
        print("Available columns in news_df:", self.news_df.columns)
        print("Available columns in stock_df:", self.stock_df.columns)
        
        try:
            # Try parsing with the format that includes seconds and timezone offset
            self.news_df['Date'] = pd.to_datetime(
                self.news_df['Date'], format='%Y-%m-%d %H:%M:%S%z', errors='coerce'
            )

            # Handle the format with only hour and minute
            self.news_df['Date'] = self.news_df['Date'].fillna(
                pd.to_datetime(self.news_df['Date'], format='%m/%d/%Y %H:%M', errors='coerce')
            )

            # Handle any remaining formats using a generalized datetime parser
            self.news_df['Date'] = self.news_df['Date'].fillna(
                pd.to_datetime(self.news_df['Date'], errors='coerce')
            )

            # Convert to just the date part
            self.news_df['Date'] = self.news_df['Date'].dt.date

        except ValueError as e:
            print(f"Error parsing date in news_df: {e}")
            raise
        
        try:
            # Parse the dates in the stock_df using mixed format
            self.stock_df['Date'] = pd.to_datetime(self.stock_df['Date'], format='mixed').dt.date

        except ValueError as e:
            print(f"Error parsing date in stock_df: {e}")
            raise

        # Print to verify that dates have been normalized correctly
        print("Normalized News Dates:\n", self.news_df['Date'].head())
        print("Normalized Stock Dates:\n", self.stock_df['Date'].head())


    