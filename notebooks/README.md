# News Analysis Exploratory Data Analysis (EDA)

## Overview

This notebook performs exploratory data analysis (EDA) on financial news articles, focusing on sentiment analysis and publication trends. The main objectives are to analyze headline lengths, article contributions by publishers, and sentiment distributions.

## Contents

1. **Setup**
   - Setting the working directory and importing necessary libraries.

2. **Data Loading**
   - Loading the dataset `raw_analyst_ratings.csv`.
   - Checking for file existence.

3. **Descriptive Statistics**
   - **Headline Length Calculation**: Computes the length of each headline and adds it as a new column.
   - **Articles per Publisher**: Counts the number of articles contributed by each publisher to identify the most active publishers.
   - **Publication Trends**: Analyzes and counts articles by year and month to observe trends over time.

4. **Text Analysis**
   - **Sentiment Analysis**: Analyzes the sentiment of each headline and classifies them into positive, neutral, or negative sentiments. Visualizes sentiment distribution.

## Requirements

To run this notebook, ensure you have the following libraries installed:

- pandas
- matplotlib
- seaborn
- Any additional libraries used in `scripts/Sentiment_Analysis.py`

## Usage

1. Clone the repository or download the notebook.
2. Navigate to the directory containing the notebook.
3. Run the notebook in Jupyter Notebook or any compatible environment.

## Conclusion

This EDA provides insights into financial news articles, helping to understand publication trends and the sentiment of the headlines, which can be useful for further analysis and decision-making.