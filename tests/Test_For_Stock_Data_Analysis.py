import os
import unittest
import pandas as pd
from scripts.Stock_Data_EDA import EDA  # Import the EDA class


class TestEDA(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        cls.file_path = "test_stock_data.csv"  # Replace with your test file path
        cls.eda = EDA(cls.file_path)

        # Check if the test file exists, create one if it doesn't
        if not os.path.exists(cls.file_path):
            data = {
                "Date": pd.date_range(start="2022-01-01", periods=100, freq="D"),
                "Close": pd.Series(range(100)),
                "Volume": pd.Series(range(100, 200)),
            }
            test_df = pd.DataFrame(data)
            test_df.to_csv(cls.file_path, index=False)

        cls.eda.load_data()

    def test_load_data(self):
        """Test loading of data"""
        self.assertIsNotNone(self.eda.df, "DataFrame should not be None after loading data.")
        self.assertIn("Date", self.eda.df.columns, "'Date' column should be in DataFrame.")
        self.assertIn("Close", self.eda.df.columns, "'Close' column should be in DataFrame.")
        self.assertIn("Volume", self.eda.df.columns, "'Volume' column should be in DataFrame.")

    def test_descriptive_statistics(self):
        """Test descriptive statistics output"""
        desc_stats = self.eda.df.describe()
        self.assertIsNotNone(desc_stats, "Descriptive statistics should not be None.")
        self.assertIn("Close", desc_stats.columns, "'Close' column should be in the descriptive statistics.")
        self.assertIn("Volume", desc_stats.columns, "'Volume' column should be in the descriptive statistics.")

    def test_count_data_points_per_year(self):
        """Test counting of data points per year"""
        count_per_year = self.eda.df['Date'].groupby(self.eda.df['Date'].dt.year).count()
        self.assertEqual(count_per_year[2022], 100, "There should be 100 data points for the year 2022.")

    def test_plot_date_trends(self):
        """Test plotting of date trends"""
        try:
            self.eda.plot_date_trends()
            plot_successful = True
        except Exception as e:
            plot_successful = False
            self.fail(f"plot_date_trends raised an exception: {e}")

        self.assertTrue(plot_successful, "plot_date_trends should complete without exceptions.")

    def test_plot_stock_prices(self):
        """Test plotting of stock prices"""
        try:
            self.eda.plot_stock_prices()
            plot_successful = True
        except Exception as e:
            plot_successful = False
            self.fail(f"plot_stock_prices raised an exception: {e}")

        self.assertTrue(plot_successful, "plot_stock_prices should complete without exceptions.")

    def test_plot_volume(self):
        """Test plotting of trading volume"""
        try:
            self.eda.plot_volume()
            plot_successful = True
        except Exception as e:
            plot_successful = False
            self.fail(f"plot_volume raised an exception: {e}")

        self.assertTrue(plot_successful, "plot_volume should complete without exceptions.")

    def test_plot_calculate_rsi(self):
        """Test calculation and plotting of RSI"""
        try:
            self.eda.plot_calculate_rsi()
            plot_successful = True
        except Exception as e:
            plot_successful = False
            self.fail(f"plot_calculate_rsi raised an exception: {e}")

        self.assertTrue(plot_successful, "plot_calculate_rsi should complete without exceptions.")

    def test_plot_calculate_macd(self):
        """Test calculation and plotting of MACD"""
        try:
            self.eda.plot_calculate_macd()
            plot_successful = True
        except Exception as e:
            plot_successful = False
            self.fail(f"plot_calculate_macd raised an exception: {e}")

        self.assertTrue(plot_successful, "plot_calculate_macd should complete without exceptions.")

if __name__ == "__main__":
    unittest.main()
