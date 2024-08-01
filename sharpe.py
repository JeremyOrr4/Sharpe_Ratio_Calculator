import yfinance as yf
import numpy as np
import pandas as pd

START_DATE = pd.to_datetime("2021-01-01")
END_DATE = pd.to_datetime("2024-01-01")
RISK_FREE_RATE_FLAG = "YEARLY" # DAILY YEARLY
STOCKS_FILE = "CAN_Stocks.txt"

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
    stock_data = yf.download(ticker)
  
    first_available_date = stock_data.index.min()

    if START_DATE < first_available_date or stock_data.empty:
       return pd.DataFrame()
    
    stock_data = yf.download(ticker, start=START_DATE, end=END_DATE)

    stock_data.index.name = 'Date'
    stock_data.reset_index(inplace=True)
    stock_data['Year'] = stock_data['Date'].dt.year

    yearly_prices = stock_data.groupby('Year')['Adj Close'].agg(['first', 'last'])
    yearly_prices['Yearly Return'] = (yearly_prices['last'] - yearly_prices['first']) / yearly_prices['first']
    
    return yearly_prices


def main():
    stocks = []
    stocks_file = open(STOCKS_FILE, 'r')
    stocks_file_lines = stocks_file.readlines()

    for line in stocks_file_lines:
        stocks.append(line.strip())
    stocks_file.close()

    sharpe = dict()
    for stock in stocks:
        returns_df = getYearlyStockReturns(stock)

        if returns_df.empty:
            continue

        risk_free_rates_df = getRiskFreeRates()

        excess_returns = []
        for index, row in returns_df.iterrows():
            
            current_year = index

            current_year_risk_free_rate = risk_free_rates_df[risk_free_rates_df['Date'].dt.year == current_year]


            excess_returns.append(row['Yearly Return'] - current_year_risk_free_rate.iloc[0]['Value'])

        
        sharpe[stock] = np.mean(excess_returns) / np.std(excess_returns)
    
    sorted_sharpe = sorted(sharpe.items(), key=lambda x: x[1], reverse=True)

    with open('sharpe_ratios.txt', 'w') as f:
        f.write(f"{START_DATE}: {END_DATE}\n")
        for stock, ratio in sorted_sharpe:
            f.write(f"{stock}: {ratio}\n")



if __name__ == "__main__":
    main()

