import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class EDA:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None  # Initialize df in __init__

    def load_data(self):
        if not os.path.exists(self.file_path):
            print(f"File not found: {self.file_path}")
        else:
            self.df = pd.read_csv(self.file_path)
            self.df["Date"] = pd.to_datetime(self.df["Date"])

    def descriptive_statistics(self):
        if self.df is not None:
            print("Descriptive Statistics: \n", self.df.describe())
        else:
            print("No data loaded. please load the data first.")

    def plot_correlation_heatmap(self):
        if self.df is not None:
            plt.figure(figsize=(10, 8))
            sns.heatmap(self.df.corr(), annot=True, cmap="coolwarm")
            plt.title("Correlation Heatmap")
            plt.show()
        else:
            print("Data not loaded. Please load the data first.")

    def count_data_points_per_year(self):
        if self.df is not None:
            years = self.df["Date"].dt.year
            year_counts = years.value_counts()
            count_per_year = year_counts.sort_index()
            print(" number of Data Points per Year: \n", count_per_year)
        else:
            print("No data loaded. please load the data first.")

    def plot_date_trends(self):
        if self.df is not None:
            self.df["year"] = self.df["Date"].dt.year
            self.df.groupby("year").size().plot(kind="bar")
            plt.title("Number of Data Points per Year")
            plt.xlabel("Year")
            plt.ylabel("Count")
            plt.show()
        else:
            print("No data loaded. please load the data first.")

    def plot_stock_prices(self):
        if self.df is not None:
            plt.figure(figsize=(10, 6))
            plt.plot(self.df["Date"], self.df["Close"], label="Close Price")
            plt.title("Stock Prices Over Time")
            plt.xlabel("Date")
            plt.ylabel("Close Price")
            plt.legend()
            plt.show()
        else:
            print("No data loaded. please load the data first. \n")

    def plot_volume(self):
        if self.df is not None:
            plt.figure(figsize=(10, 6))
            plt.plot(self.df["Date"], self.df["Volume"])
            plt.title("Trading Volume Over Time")
            plt.xlabel("Date")
            plt.ylabel("Volume")
            plt.ticklabel_format(style="plain", axis="y")
            plt.legend()
            plt.show()
        else:
            print("No data loaded. Please load the data first.")

    def real_time_exchange_plot(self):
        if self.df is not None:
            plt.figure(figsize=(10, 6))
            # Plot the closing prices
            plt.plot(
                self.df["Date"], self.df["Close"], label="Close Price", color="blue"
            )
            # Add volume bars on a secondary y-axis
            ax2 = plt.gca().twinx()
            ax2.bar(
                self.df["Date"],
                self.df["Volume"],
                color="gray",
                alpha=0.3,
                label="Volume",
            )
            ax2.set_ylabel("Volume")
            plt.title("Stock Closing Price and Volume Over Time")
            plt.xlabel("Date")
            plt.ylabel("Close Price")
            plt.legend(loc="upper left")
            plt.show()
            plt.clf()  # Clear the figure after displaying
        else:
            print("No data loaded. Please load the data first.")
            
    def plot_calculate_rsi(self, period=14):
        if self.df is not None:
            delta = self.df['Close'].diff(1)
            gain = delta.where(delta > 0, 0)
            loss = -delta.where(delta < 0, 0)
            avg_gain = gain.rolling(window=period).mean()
            avg_loss = loss.rolling(window=period).mean()
            rs = avg_gain / avg_loss
            self.df['RSI'] = 100 - (100 / (1 + rs))
            plt.figure(figsize=(10, 6))
            plt.plot(self.df['Date'], self.df['RSI'], label='RSI')
            plt.axhline(y=70, color='red', linestyle='--')
            plt.axhline(y=30, color='green', linestyle='--')
            plt.title('Relative Strength Index')
            plt.xlabel('Date')
            plt.ylabel('RSI')
            plt.legend()
            plt.show()
        else:
            print("No data loaded. Please load the data first.")
            
    def calculate_moving_averages(self, window_size=50):
        if self.df is not None:
            self.df[f'SMA_{window_size}'] = self.df['Close'].rolling(window=window_size).mean()
            plt.figure(figsize=(10, 6))
            plt.plot(self.df['Date'], self.df['Close'], label='Close Price')
            plt.plot(self.df['Date'], self.df[f'SMA_{window_size}'], label=f'SMA {window_size}')
            plt.title(f'{window_size}-Day Simple Moving Average')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            plt.show()
        else:
            print("No data loaded. Please load the data first.")
            
    def plot_calculate_macd(self, short_window=12, long_window=26, signal_window=9):
        if self.df is not None:
            self.df['MACD'] = self.df['Close'].ewm(span=short_window, adjust=False).mean() - \
                            self.df['Close'].ewm(span=long_window, adjust=False).mean()
            self.df['Signal Line'] = self.df['MACD'].ewm(span=signal_window, adjust=False).mean()
            plt.figure(figsize=(10, 6))
            plt.plot(self.df['Date'], self.df['MACD'], label='MACD')
            plt.plot(self.df['Date'], self.df['Signal Line'], label='Signal Line')
            plt.title('MACD and Signal Line')
            plt.xlabel('Date')
            plt.ylabel('Value')
            plt.legend()
            plt.show()
        else:
            print("No data loaded. Please load the data first.")
