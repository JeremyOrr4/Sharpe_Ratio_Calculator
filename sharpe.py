import yfinance as yf
import numpy as np
import pandas as pd

riskFreeRate = 0.02
start_date = '2018-01-01'
end_date = '2023-01-01'
sharpe_ratios = {}


data = yf.download("AAPL", start=start_date, end=end_date)

closing_prices = data['Close']

excessReturns = []
for i in range(len(closing_prices) - 1):

    excessReturns.append(((closing_prices[i + 1] - closing_prices[i])/closing_prices[i]) - riskFreeRate)

sharpe_ratios["AAPL"] = np.mean(excessReturns) / np.std(excessReturns)

print(sharpe_ratios)





