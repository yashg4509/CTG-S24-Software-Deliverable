# Task 3: Evaluate your factors

## Explanation of the Change
I changed the `calculate_returns` function. In the updated approach, instead of iterating through each row (date) in the factors DataFrame using iterrows(), we iterate through each row index using range(len(self.factors) - 1). This allows us to access the factors for each date and the next date separately.

We then use the factors for the current date to make decisions and select top 5 tickers. However, we calculate returns based on the data available for the next date (next_date), ensuring that we're not using future data to make decisions.

There are 2 reasons why this works against look ahead bias.

1. Instead of iterating through each row (date) in the factors DataFrame, we iterate through each row index to ensure that we're using only today's factors for making decisions, not tomorrow's.

2. We calculate returns for each date using the factors for that date, and we calculate the returns based on the data available for the next date (not the current date). This ensures that we're not using future data to make decisions.