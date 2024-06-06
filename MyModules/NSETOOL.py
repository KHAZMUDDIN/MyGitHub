from django.http import HttpResponse
from django.shortcuts import render
import os
import pandas as pd
import numpy as np
import json
import yfinance as yf
import warnings
from datetime import datetime, timedelta
# import yfinance as yf
#
# # Define the ticker symbols for NSE indices
# indices = {
#     'NIFTY 50': '^NSEI',
#     'NIFTY BANK': '^NSEBANK',
#     'NIFTY MIDCAP 50': '^NSEMDCP50',
#     'NIFTY NEXT 50': '^NSENEXT50'
# }
#
# # Fetch data for each index
# for index_name, ticker in indices.items():
#     index = yf.Ticker(ticker)
#
#     # Get historical market data (you can adjust the period as needed)
#     hist = index.history(period="1d")
#
#     print(f"{index_name} Data:")
#     print(hist)
#     print("\n")

import yfinance as yf

# Suppress specific FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning, message=".*TimedeltaIndex construction is deprecated.*")

periods = {
        '1Day': timedelta(days=1),
        '1Week': timedelta(weeks=1),
        '1Month': timedelta(days=30),
        '3Months': timedelta(days=90),
        '6Months': timedelta(days=180),
        '1Year': timedelta(days=365),
        '5Years': timedelta(days=5*365)
    }

# Function to calculate returns for a given stock data
def calculate_returns(stock_data):
    returns = {}

    if stock_data.empty:
        return {period: None for period in periods.keys()}

    last_trading_day = stock_data.index[-1]
    current_close = stock_data['Close'].loc[last_trading_day]

    for period, delta in periods.items():
        target_date = last_trading_day - delta
        past_data = stock_data[stock_data.index <= target_date]

        if not past_data.empty:
            past_close = past_data['Close'].iloc[-1]
            returns[period] = round(((current_close - past_close) / past_close) * 100, 2)
        else:
            returns[period] = None

    return returns

# Function to fetch and print index quotes
def fetch_index_quotes(indices):
    for index_name, ticker in indices.items():
        index = yf.Ticker(ticker)
        print(f"{index_name}: {ticker}")

        # Fetch real-time data
        info = index.info
        # print(f"\n{index_name} Real-Time Data:")
        # print(f"Current Price: {info.get('regularMarketPrice', 'N/A')}")
        # print(f"Day High: {info.get('dayHigh', 'N/A')}")
        # print(f"Day Low: {info.get('dayLow', 'N/A')}")
        # print(f"Previous Close: {info.get('regularMarketPreviousClose', 'N/A')}")
        # print(f"Open: {info.get('regularMarketOpen', 'N/A')}")
        # print(f"Volume: {info.get('regularMarketVolume', 'N/A')}")
        #
        # Fetch historical market data (e.g., for the last 5 days)
        hist = index.history(period="5d")
        print(f"\n{index_name} Historical Data (Last 5 Days):")
        # indices
        # Fetch historical market data for the last 6 years
        hist = index.history(period="6y")
        ret = calculate_returns(hist)
        print(f"returns: {ret}")
        print("============================================================")

# # Define the ticker symbols for NSE indices
# indices = {
#     'NIFTY 50': '^NSEI',
#     'NIFTY BANK': '^NSEBANK',
#     'NIFTY MIDCAP 50': '^NSEMDCP50',
#     'NIFTY NEXT 50': '^NSENEXT50'
# }

# Define the ticker symbols for NSE indices
indices = {
    'NIFTY 50': '^NSEI'
}

# Fetch and print quotes for all defined indices
fetch_index_quotes(indices)

