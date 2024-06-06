import pandas as pd
import numpy as np
import json
import yfinance as yf
import warnings
from datetime import datetime, timedelta

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
symbol = 'WIPRO.NS'
tick = yf.Ticker(symbol)
stock_data = tick.history(period = '7d')
last_trading_day = stock_data.index[-1]
print(last_trading_day)

for period, delta in periods.items():
    target_date = last_trading_day - delta
    print(target_date)