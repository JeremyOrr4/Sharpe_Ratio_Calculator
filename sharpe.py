import yfinance as yf
import numpy as np
import pandas as pd

START_DATE = pd.to_datetime("2022-01-01")
END_DATE = pd.to_datetime("2023-01-01")
RISK_FREE_RATE_FLAG = "YEARLY" # DAILY YEARLY

def getRiskFreeRates():
    if RISK_FREE_RATE_FLAG == "YEARLY":
        df = pd.read_csv('Excel/CAN_Risk_Free_Rates_2000To2024_Yearly.csv')
    elif RISK_FREE_RATE_FLAG == "DAILY":
        df = pd.read_csv('Excel/CAN_Risk_Free_Rates_2000To2024_Daily.csv')

    rates = df.set_index('Date')['Rate'].to_dict()
    df = pd.DataFrame(list(rates.items()), columns=['Date', 'Value'])
    df['Date'] = pd.to_datetime(df['Date'])
    filtered_df = df[(df['Date'] >= START_DATE) & (df['Date'] <= END_DATE)]
    # filtered_dict = filtered_df.set_index('Date')['Value'].to_dict()

    return filtered_df


def getYearlyStockReturns(ticker):
    stock_data = yf.download(ticker, start=START_DATE, end=END_DATE)

    stock_data.index.name = 'Date'
    stock_data.reset_index(inplace=True)
    stock_data['Year'] = stock_data['Date'].dt.year

    yearly_prices = stock_data.groupby('Year')['Adj Close'].agg(['first', 'last'])
    yearly_prices['Yearly Return'] = (yearly_prices['last'] - yearly_prices['first']) / yearly_prices['first']
    
    return yearly_prices


def main():
    stocks = []
    stocks_file = open('Stocks.txt', 'r')
    stocks_file_lines = stocks_file.readlines()

    for line in stocks_file_lines:
        stocks.append(line.strip())
    stocks_file.close()
    
    returns_df = getYearlyStockReturns(stocks[0])
    risk_free_rates_df = getRiskFreeRates()

    excess_returns = []
    for index, row in returns_df.iterrows():
        
        current_year = index

        current_year_risk_free_rate = risk_free_rates_df[risk_free_rates_df['Date'].dt.year == current_year]


        excess_returns.append(row['Yearly Return'] - current_year_risk_free_rate.iloc[0]['Value'])


    print(excess_returns)



if __name__ == "__main__":
    main()

# Download historical stock data

# Ensure 'Date' is a column in the DataFrame and convert it to datetime if necessary
# stock_data.index.name = 'Date'
# stock_data.reset_index(inplace=True)

# # Create a dictionary with dates as keys and closing values as values
# stock_dict = stock_data.set_index('Date')['Close'].to_dict()

# excessReturns = []
# sorted_dates = sorted(stock_dict.keys())

# for i in range(len(sorted_dates) - 1):
#     current_date = sorted_dates[i]
#     next_date = sorted_dates[i + 1]
    
#     if next_date in stock_dict :
#         current_price = stock_dict[current_date]
#         next_price = stock_dict[next_date]
#         excess_return = (next_price - current_price) / current_price
#         print(excess_return)
#         excessReturns.append(excess_return - pow(filtered_dict.get(current_date),365))
#         print(pow(filtered_dict.get(current_date),12))

# sharpe = np.mean(excessReturns) / np.std(excessReturns)
# print(sharpe)





