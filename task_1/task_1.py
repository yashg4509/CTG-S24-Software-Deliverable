import yfinance as yf
import pandas as pd
import os

def fetch_data(ticker):
    """
    Function to get the data based on stock ticker. Downloads data using stock ticker and saves to CSV
    and conducts any necessary error handling.

    :param ticker: stock ticker to retrieve data
    :return: N/A
    """

    try:
        # use Yahoo Finance API to get data
        data = yf.download(ticker, start="2021-01-01", end="2023-12-31")

        # save to csv
        data.to_csv(f"../data/{ticker}.csv")

        print("successfully saved")  # success

    except Exception as e:
        print(f"error fetching data for {ticker} - {str(e)}")


# create data directory
if not os.path.exists("../data"):
    os.makedirs("../data")

# read and collect tickers from text file
with open("tickers.txt", "r") as f:
    tickers = f.read().splitlines()

# fetch data for each ticker
for t in tickers:
    fetch_data(t)
