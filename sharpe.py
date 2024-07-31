import yfinance as yf
import numpy as np
import pandas as pd

startDate = '2023-07-29'
endDate = '2024-07-29'

startDate = pd.to_datetime(startDate)
endDate = pd.to_datetime(endDate)

df = pd.read_csv('CAN_Risk_Free_Rates_Daily.csv')
rates = df.set_index('Date')['Rate'].to_dict()
df = pd.DataFrame(list(rates.items()), columns=['Date', 'Value'])

df['Date'] = pd.to_datetime(df['Date'])

filtered_df = df[(df['Date'] >= startDate) & (df['Date'] <= endDate)]

filtered_dict = filtered_df.set_index('Date')['Value'].to_dict()

print(filtered_dict)

ticker = 'DOL.TO'  

# Download historical stock data
stock_data = yf.download(ticker, start=startDate, end=endDate)

# Ensure 'Date' is a column in the DataFrame and convert it to datetime if necessary
stock_data.index.name = 'Date'
stock_data.reset_index(inplace=True)

# Create a dictionary with dates as keys and closing values as values
stock_dict = stock_data.set_index('Date')['Close'].to_dict()

excessReturns = []
sorted_dates = sorted(stock_dict.keys())

for i in range(len(sorted_dates) - 1):
    current_date = sorted_dates[i]
    next_date = sorted_dates[i + 1]
    
    if next_date in stock_dict :
        current_price = stock_dict[current_date]
        next_price = stock_dict[next_date]
        excess_return = (next_price - current_price) / current_price
        print(excess_return)
        excessReturns.append(excess_return - pow(filtered_dict.get(current_date),365))
        print(pow(filtered_dict.get(current_date),12))

sharpe = np.mean(excessReturns) / np.std(excessReturns)
print(sharpe)





