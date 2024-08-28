import matplotlib.pyplot as plt
import pandas as pd
from textblob import TextBlob  # type: ignore
import re


class NewsAnalysis:
    def __init__(self, file_path):
        try:
            self.df = pd.read_csv(file_path)  # Use read_csv for CSV files

            # First attempt to parse dates with the first format
            self.df["date"] = pd.to_datetime(
                self.df["date"], format="%Y-%m-%d %H:%M:%S%z", errors="coerce"
            )

            # For rows where the date parsing failed, try the second format
            self.df["date"] = self.df["date"].fillna(
                pd.to_datetime(
                    self.df["date"], format="%m/%d/%Y %H:%M", errors="coerce"
                )
            )

        except Exception as e:
            print(f"Error reading the file: {e}")

    def calculate_headline_length(self):
        self.df["headline_length"] = self.df["headline"].apply(len)

    def articles_per_publisher(self):
        return self.df["publisher"].value_counts()

    def publication_trends(self):
        self.df["year_month"] = self.df["date"].dt.to_period("M")
        return self.df["year_month"].value_counts().sort_index()

    # def sentiment_analysis(self):
    #     self.df["sentiment"] = self.df["headline"].apply(
    #         lambda x: TextBlob(x).sentiment.polarity
    #     )

    def publication_frequency(self):
        self.df.set_index("date", inplace=True)
        return self.df.resample("D").size()

    def top_publishers(self):
        return self.df["publisher"].value_counts().head(10)

    def domain_counts(self):
        self.df["domain"] = self.df["publisher"].apply(
            lambda x: x.split("@")[-1] if "@" in x else x
        )
        return self.df["domain"].value_counts()

    def save_results(self, output_path):
        self.df.to_excel(output_path, index=False)

    def plot_top_publishers(self, top_n=20):
        """Plot the top N publishers by the number of articles."""
        top_publishers = self.articles_per_publisher().head(top_n)
        top_publishers.plot(
            kind="bar",
            figsize=(12, 6),
            title=f"Top {top_n} Publishers by Number of Articles",
        )
        plt.xlabel("Publisher")
        plt.ylabel("Number of Articles")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    def plot_publication_trends(self):
        """Plot the publication trends over time."""
        # Ensure 'year_month' column is created if not already present
        if "year_month" not in self.df.columns:
            self.df["year_month"] = self.df["date"].dt.to_period("M")
        
        # Compute publication trends
        publication_trends = self.df["year_month"].value_counts().sort_index()
        
        # Plotting the trends
        publication_trends.plot(
            kind="line", figsize=(12, 6), title="Publication Trends Over Time"
        )
        plt.xlabel("Year-Month")
        plt.ylabel("Number of Articles")
        plt.tight_layout()
        plt.show()

    def display_top_publishers(self, top_n=20):
        """Display the top N publishers in tabular format."""
        top_publishers = self.articles_per_publisher().head(top_n)
        print(f"Top {top_n} Publishers in Tabular Format:")
        print(top_publishers)

    def display_publication_trends(self, top_n=10):
        """Display the first N publication trends in tabular format."""
        # Ensure 'year_month' column is created if not already present
        if "year_month" not in self.df.columns:
            self.df["year_month"] = self.df["date"].dt.to_period("M")
        
        # Compute publication trends
        publication_trends = self.df["year_month"].value_counts().sort_index().head(top_n)
        
        # Displaying the trends
        print(f"First {top_n} Publication Trends in Tabular Format:")
        print(publication_trends)

    # Text Analysis(Sentiment analysis & Topic Modeling):
    def sentiment_analysis(self):
        def get_sentiment(headline):
            analysis = TextBlob(headline)
            if analysis.sentiment.polarity > 0:
                return "Positive"
            elif analysis.sentiment.polarity == 0:
                return "Neutral"
            else:
                return "Negative"

        self.df["sentiment"] = self.df["headline"].apply(get_sentiment)
        
        # Visualize the sentiment data
        sentiment_counts = self.df["sentiment"].value_counts()
        sentiment_counts.plot(kind='bar', color=['green', 'blue', 'red'])
        plt.xlabel('Sentiment')
        plt.ylabel('Number of Headlines')
        plt.title('Sentiment Analysis of Headlines')
        plt.show()
    
        return self.df[["headline", "sentiment"]]
    
    def extract_domain(self, email):
        """Extract domain from email address."""
        match = re.search(r'@([\w.]+)', email)
        return match.group(1) if match else None
    
    def analyze_publisher_domains(self):
        """Identify unique domains and their frequencies."""
        # Extract domains
        self.df['domain'] = self.df['publisher'].apply(self.extract_domain)
        
        # Count frequencies of each domain
        domain_counts = self.df['domain'].value_counts()
        
        return domain_counts
    
    def display_domain_distribution(self):
        """Plot the distribution of domains."""
        domain_counts = self.analyze_publisher_domains()
        plt.figure(figsize=(12, 6))
        domain_counts.plot(kind='bar')
        plt.xlabel('Domain')
        plt.ylabel('Frequency')
        plt.title('Frequency of Publishers by Domain')
        plt.xticks(rotation=45)
        plt.show()
