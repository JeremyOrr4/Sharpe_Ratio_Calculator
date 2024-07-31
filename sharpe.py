import yfinance as yf
import numpy as np
import pandas as pd


start_date = '2019-01-01'
end_date = '2024-01-01'

df = pd.read_csv('CAN_Risk_Free_Rates.csv')

rates = df.set_index('Date')['Rate'].to_dict()

df = pd.DataFrame(list(rates.items()), columns=['Date', 'Value'])

df['Date'] = pd.to_datetime(df['Date'])

date1 = '2024-07-20'
date2 = '2024-07-30'

date1 = pd.to_datetime(date1)
date2 = pd.to_datetime(date2)

filtered_df = df[(df['Date'] >= date1) & (df['Date'] <= date2)]

filtered_dict = filtered_df.set_index('Date')['Value'].to_dict()

print(filtered_dict)


# data = yf.download("AAPL", start=start_date, end=end_date)

# closing_prices = data['Close']

# excessReturns = []
# for i in range(len(closing_prices) - 1):

#     excessReturns.append(((closing_prices[i + 1] - closing_prices[i])/closing_prices[i]) - riskFreeRate)

# sharpe_ratios["AAPL"] = np.mean(excessReturns) / np.std(excessReturns)

# print(sharpe_ratios)





