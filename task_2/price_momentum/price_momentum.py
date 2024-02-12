# imports
import pandas as pd
import os

# initialize output dataframe
price_momentum_df = pd.DataFrame()

def calculate_price_momentum(ticker):
    """
    Calculates price momentum factor for a given stock.

    :param ticker: Ticker symbol of the stock
    :return: price momentums for a certain stock for all dates in the range
    """
    try:
        # find and read stock data collected in task 1
        stock_data = pd.read_csv(os.path.join("../../data/", f"{ticker}.csv"))

        # calculate the difference in close prices between start and end days
        price_difference = stock_data['Close'] - stock_data['Close'].shift(5)

        # divide by close price at end day and find the percent to get momentum score
        stock_data[ticker] = (price_difference / stock_data['Close'].shift(5)) * 100

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
    ticker_price_momentum = calculate_price_momentum(ticker)
    # check if empty to see if error was given or not
    if not ticker_price_momentum.empty:
        # join the price momentum calculated for each ticker together
        price_momentum_df = price_momentum_df.join(ticker_price_momentum, how='outer')

# save all calculations to price_momentum.csv
price_momentum_df.to_csv("price_momentum.csv")
print("Price momentum data saved to price_momentum.csv")  # success
