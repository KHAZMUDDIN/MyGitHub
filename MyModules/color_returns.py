import os
import pandas as pd
import yfinance as yf
import warnings

# Suppress specific FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning, message=".*TimedeltaIndex construction is deprecated.*")
def returns(all_comp):
    df_combined = pd.DataFrame()
    for compID in all_comp:
        # Fetch historical stock prices for the specified ticker symbols
        stock_data = yf.download(compID+'.NS', start='2000-01-03', end='2024-12-31')

        # Resample the DataFrame to monthly frequency and calculate monthly returns
        # monthly_returns = stock_data['Close'].resample('M').ffill().pct_change()
        # Resample the data monthly and calculate percentage change
        monthly_returns = stock_data['Close'].resample('ME').ffill().pct_change()

        print(f"monthly returns of {compID}: \n{monthly_returns}")
        # Add the series to the DataFrame
        df_combined = pd.concat([df_combined, monthly_returns], axis=1)
    print(f"combined dataframe: {df_combined}")

if __name__ == '__main__':
    all_comp = ['ITC', 'GODFRYPHLP', 'VSTIND', 'GOLDENTOBC']
    returns(all_comp)