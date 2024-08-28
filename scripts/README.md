# Financial News Sentiment Analysis Project

## Overview
This project focuses on analyzing financial news headlines to assess their sentiment and correlating these sentiments with stock price movements. The analysis aims to uncover insights that can enhance financial forecasting and support investment strategies.

## Project Structure
The project consists of two main scripts:

### 1. Sentiment Analysis (`Sentiment_Analysis.py`)
This script performs sentiment analysis on financial news headlines. The key features include:
- **Headline Length Calculation:** Measures the length of each news headline.
- **Article Count per Publisher:** Counts the number of articles published by each news source.
- **Publication Trends:** Analyzes the publication trends over time.
- **Sentiment Analysis:** Evaluates the sentiment of each headline (e.g., positive, negative, or neutral).
- **Publisher Domain Analysis:** Analyzes the distribution of publishers based on their domain.

### 2. Stock Data EDA (`Stock_Data_EDA.py`)
This script conducts Exploratory Data Analysis (EDA) on stock data. The key features include:
- **Data Visualization:** Generates various plots to visualize stock data trends.
- **Correlation Analysis:** Assesses the relationship between stock price movements and other financial metrics.
- **Stock Performance Analysis:** Evaluates stock performance based on the collected data.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Ermi23/Financial-News-Sentiment-Analysis.git

### 2. Setup Virtual Enviroment
python3 -m venv venv
# On Windows: .\venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate

### 3. install dependencies

pip install -r requirements.txt

## Usage
To use this project:

Ensure Python and the required libraries are installed.
Clone the repository to your local machine.
Navigate to the project directory.
Run the scripts as needed for sentiment analysis or stock data exploration.