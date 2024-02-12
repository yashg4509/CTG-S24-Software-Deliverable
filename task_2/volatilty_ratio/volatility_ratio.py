# imports
import pandas as pd
import os

# initialize output dataframe
vol_ratio_df = pd.DataFrame()

def calculate_vol_ratio(ticker):
    """
    Calculates volatility ratio over 20 days for a given stock

    :param ticker: ticker symbol for each stock
    :return: volatility ratios for a certain stock for all dates in the date range
    """

    try:
        # find and read stock data collected in task 1
        stock_data = pd.read_csv(os.path.join("../../data/", f"{ticker}.csv"))

        # calculate daily returns from row before
        daily_returns = stock_data['Close'].pct_change()

        # calculate standard deviation of daily returns
        std_dr = daily_returns.rolling(window=20).std()

        # calculate average daily returns
        avg_returns = daily_returns.rolling(window=20).mean()

        # calculate volatility ratio
        stock_data[ticker] = std_dr / avg_returns

        # set Date column as index as all stocks read against Date
        stock_data.set_index('Date', inplace=True)

        # return the stock volatility ratio only as we join them later on
        return stock_data[[ticker]]

    except Exception as e:
        print(f"Error calculating price momentum factor for {ticker}: {str(e)}")
        return pd.DataFrame()

# read in stocks for column names and calculations
with open("../../task_1/tickers.txt", "r") as f:
    tickers = f.read().splitlines()

# go through all stocks
for ticker in tickers:
    # calculate volatility ratio for each stock
    ticker_vol_ratio = calculate_vol_ratio(ticker)
    # check if empty to see if error was given or not
    if not ticker_vol_ratio.empty:
        # join the price momentum calculated for each ticker together
        vol_ratio_df = vol_ratio_df.join(ticker_vol_ratio, how='outer')

# save all calculations to price_momentum.csv
vol_ratio_df.to_csv("vol_ratio.csv")
print("Volatility ratio momentum data saved to vol_ratio.csv")  # success