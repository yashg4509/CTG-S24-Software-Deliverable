import pandas as pd
import os

# initialize output dataframe
price_momentum_df = pd.DataFrame(columns=['Date', 'Stock', 'Price Momentum'])

def calculate_price_momentum(ticker):
    """
    Calculates price momentum factor for a given stock.

    :param data: DataFrame containing the stock data
    :param period: Period over which price momentum is calculated (5 days in this example)
    :return: Pandas Series containing the output data of calculated factor
    """
    try:
        # read data from CSV
        stock_data = pd.read_csv(os.path.join("../../data/", f"{ticker}.csv"))

        # calculate the difference in close prices between start and end days and
        # divide by close price at end day, then find the percent
        stock_data['Price Momentum'] = ((stock_data['Close'] - stock_data['Close'].shift(5)) / stock_data['Close'].shift(5)) * 100

        # clean for missing values
        stock_data.dropna(inplace=True)

        # indicate stock for output
        stock_data['Stock'] = ticker

        # append price momentum calculation to output df
        global price_momentum_df
        price_momentum_df = pd.concat([price_momentum_df, stock_data[['Date', 'Stock', 'Price Momentum']]], ignore_index=True)

        # print(f"Price momentum factor calculated for {ticker}")

    except Exception as e:
        print(f"Error calculating price momentum factor for {ticker}: {str(e)}")

# read and process tickers from the tickers.txt file
with open("../../task_1/tickers.txt", "r") as f:
    tickers = f.read().splitlines()

# calculate price momentum factor for each ticker
for ticker in tickers:
    calculate_price_momentum(ticker)

# save all calculations to output.csv
price_momentum_df.to_csv("price_momentum.csv", index=False)
print("Price momentum data saved to price_momentum.csv")
