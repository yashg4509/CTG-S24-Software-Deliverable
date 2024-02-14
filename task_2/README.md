# Task 2: Calculate a Factor

### Summary of Implementation Details for Factor 1 & 2

The implementation of the first factor, Price Momentum, involved calculating the momentum score for each stock over a 5-day period by comparing the difference in close prices between the current day and 5 days ago. This score was then multiplied by 100 and stored in a DataFrame. 

Similarly, for the second factor, Volume Adjusted Momentum, the process included calculating price momentum as in Factor 1 and dividing it by the previous day’s volume, providing insights into momentum adjusted for trading volume over a 15-day period. Despite the need for slight adjustments in data manipulation and formatting, both factors were implemented smoothly without encountering significant challenges. The resulting scores were accurately computed and saved, ready for further analysis and evaluation.

### Custom Factor: Volatility Factor

#### Implementation:

For the custom factor, we decided to implement a Volatility Ratio over 20 days. Volatility ratio is calculated as the ratio of the standard deviation of daily returns to the average daily returns over a 20-day period.

For calculation, I used the [rolling](https://www.geeksforgeeks.org/python-pandas-dataframe-rolling/) function to do the same percent change calculation -- where I used the pct_change function -- for the 20 day period (ie 20 rows). I coupled that with the standard deviation and mean calculations via the std() and mean() methods respectively.

#### Motivations:

Volatility ratio provides insights into the volatility of a stock's returns relative to its average returns over a certain period.
It can be used as a measure of risk or stability of a stock's performance.

### Issues Encountered
- One major issue encountered was related to the formatting of the output CSV file.
- Initially, the factor for each stock was being calculated and saved separately, leading to difficulty in merging and analyzing the data.
  - This looked something like creating a DataFrame with 2 columns, Date and the result of the factor, for each stock and then saving those to individual CSVs.
- The final solution involved assigning the factor for each stock in a resultant DataFrame and joining all the DataFrames using the Date column as an index.
  - Much of the debugging work was fixing the join statement properly as I kept encountering different issues, such as duplicated date columns, duplicated factor columns, etc.
  - In terms of implementation, what I do now is I conduct all the calculations in the method, save it to a ticker column within the original Dataframe that we are accessing, return that column from the calculating method, call the method for all tickers, and join all the resultant columns together. All factors essentially follow this same structure.
- All general bugs are handled by the general exception thrown in the `try-except` within the calculate methods.
