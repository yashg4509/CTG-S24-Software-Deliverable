# imports
import pandas as pd
import os

# initialize output dataframe
vol_adj_df = pd.DataFrame()

def calculate_vol_adj(ticker):
    """
    Calculates volume adjusted momentum factor for a given stock

    :param ticker: Ticker symbol of the stock
    :return: volume adjusted momentum scores for a certain stock for all dates in the range
    """
    try:
        # find and read stock data collected in task 1
        stock_data = pd.read_csv(os.path.join("../../data/", f"{ticker}.csv"))

        # calculate price momentum
        price_momentum = ((stock_data['Close'] - stock_data['Close'].shift(5)) / stock_data['Close'].shift(5)) * 100

        # divide by previous day volume
        stock_data[ticker] = price_momentum / stock_data['Volume'].shift(1)

        # set Date column as index as all stocks read against Date
        stock_data.set_index('Date', inplace=True)

        # return the ticker price momentums only as we join them later on
        return stock_data[[ticker]]

    except Exception as e:
        print(f"Error calculating price momentum factor for {ticker}: {str(e)}")
        return pd.DataFrame()

# read in stocks for column names and calculations
with open("../../task_1/tickers.txt", "r") as f:
    tickers = f.read().splitlines()

# go through all stocks
for ticker in tickers:
    # calculate price momentums for each stock
    ticker_vol_adj = calculate_vol_adj(ticker)
    # check if empty to see if error was given or not
    if not ticker_vol_adj.empty:
        # join the price momentum calculated for each ticker together
        vol_adj_df = vol_adj_df.join(ticker_vol_adj, how='outer')

# save all calculations to price_momentum.csv
vol_adj_df.to_csv("vol_adj.csv")
print("Volume adjusted momentum data saved to vol_adj.csv")  # success
