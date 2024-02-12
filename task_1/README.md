## Task 1 : Data Collection and Preparation

#### Overview
In this task, we looked at data from the S&P 500 over the last 2 years. More specifically, we examined the top 25 weighted stocks using stock tickers and the Yahoo Finance API. We organized the data into different CSVs for each stock ticker.

#### Accessing the Data
1. **Data Retrieval**: All historical stock data collected can be accessed in the `data` directory with each CSV file labeled with the appropriate stock ticker.
2. **Interpreting the Data**: Each CSV file contains historical data for a specific stock, including Date, Open, High, Low, Close, Volume, and Adjusted Close.
   1. **Date**: date of the stock record
   2. **Open**: opening price of the stock at the beginning of the trading day
   3. **High**: the peak price of the stock in the trading day 
   4. **Low**: the lowest price of the stock in the trading day
   5. **Volume**: total number of shares traded during trading day
   6. **Adjusted Close (Adj Close)**: closing price adjusted for corporate actions, such as dividends, mergers, etc.

#### Handling the Errors

1. **Issues with Data Retrieval**: At the beginning, I was getting a lot of errors, whether it be formatting of extracting or other issues when accessing the data in a way to manipulate in Python. However, adding a general exception makes it so that any break in the program, even if not volatile, will allow someone to more effectively seem when there are errors and how to solve each error.
2. **Data Integrity and Missing Values**: The script uses `yfinance` library, which draws directly from Yahoo Finance and is therefore reliable for stock data. Moreover, much of these issues of missing data are all handled internally within the download function of `yfinance`, ensuring consistency in solution.

