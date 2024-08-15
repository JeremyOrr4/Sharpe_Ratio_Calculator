# Stock Sharpe Ratio Calculation Application

This Python application calculates the Sharpe ratios for a list of Canadian stocks over a specified date range. The Sharpe ratio measures the risk-adjusted return of an investment.

## Features

- **Historical Data Download**: Uses the Yahoo Finance API to download historical stock data.
- **Yearly Returns Calculation**: Computes yearly returns based on adjusted closing prices.
- **Risk-Free Rate Adjustment**: Adjusts returns using historical risk-free rates from a CSV file.
- **Sharpe Ratio Calculation**: Calculates the Sharpe ratio for each stock, which is then sorted and saved to a text file.

## Files Included

- **CAN_Stocks.txt**: A file containing a list of stock tickers (one per line).
- **CAN_Risk_Free_Rates_2000To2024_Yearly.csv**: A CSV file containing yearly risk-free rates for Canada from 2000 to 2024.
- **sharpe_ratios.txt**: The output file where the calculated Sharpe ratios are stored.

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required Python libraries using pip:
   ```
   pip install yfinance pandas numpy
   ```

## Usage

1. Populate `CAN_Stocks.txt` with the stock tickers you want to analyze.
2. Make sure `CAN_Risk_Free_Rates_2000To2024_Yearly.csv` is placed in the `Excel` directory.
3. Set the `START_DATE` and `END_DATE` in the script to define your desired date range.
4. Run the script:
   ```
   python sharpe.py
   ```
5. The Sharpe ratios will be saved in `sharpe_ratios.txt`.

## Output

The output file `sharpe_ratios.txt` will contain the Sharpe ratios for each stock, sorted in descending order. The file format will look like this:

## License

This project is licensed under the MIT License.
