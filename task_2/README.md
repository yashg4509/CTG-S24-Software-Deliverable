# Task 2: Calculate a Factor

### Summary of Implementation Details for Factor 1 & 2

The implementation of the first factor, Price Momentum, involved calculating the momentum score for each stock over a 5-day period by comparing the difference in close prices between the current day and 5 days ago. This score was then multiplied by 100 and stored in a DataFrame. Similarly, for the second factor, Volume Adjusted Momentum, the process included calculating price momentum as in Factor 1 and dividing it by the previous day’s volume, providing insights into momentum adjusted for trading volume over a 15-day period. Despite the need for slight adjustments in data manipulation and formatting, both factors were implemented smoothly without encountering significant challenges. The resulting scores were accurately computed and saved, ready for further analysis and evaluation.

### Custom Factor: Volatility Factor

#### Implementation:

For the custom factor, we decided to implement a Volatility Ratio over 20 days.
Volatility ratio is calculated as the ratio of the standard deviation of daily returns to the average daily returns over a 20-day period.

#### Motivations:

Volatility ratio provides insights into the volatility of a stock's returns relative to its average returns over a certain period.
It can be used as a measure of risk or stability of a stock's performance.

### Issues Encountered
- One major issue encountered was related to the formatting of the output CSV file.
- Initially, the factor for each stock was being calculated and saved separately, leading to difficulty in merging and analyzing the data.
- The final solution involved assigning the factor for each stock in a resultant DataFrame and joining all the DataFrames using the Date column as an index.