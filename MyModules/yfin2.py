import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

#
# # Function to calculate returns for a given stock data
# def calculate_returns(stock_data, periods):
#     returns = {}
#
#     if stock_data.empty:
#         return {period: None for period in periods.keys()}
#
#     for period, delta in periods.items():
#         target_date = datetime.today() - delta
#         try:
#             current_close = stock_data['Close'].iloc[-1]
#             past_data = stock_data[stock_data.index <= target_date]
#
#             if not past_data.empty:
#                 past_close = past_data['Close'].iloc[-1]
#                 returns[period] = ((current_close - past_close) / past_close) * 100
#             else:
#                 returns[period] = None
#         except KeyError:
#             returns[period] = None
#
#     return returns
#
#
# # Main function to fetch data and calculate returns for all companies in the DataFrame
# def fetch_all_company_data(df):
#     # Define periods and labels
#     periods = {
#         '1Day': timedelta(days=1),
#         '1Week': timedelta(weeks=1),
#         '1Month': timedelta(days=30),
#         '3Months': timedelta(days=90),
#         '6Months': timedelta(days=180),
#         '1Year': timedelta(days=365),
#         '5Years': timedelta(days=5 * 365)
#     }
#
#     # Iterate through each row of the DataFrame
#     for index, row in df.iterrows():
#         symbol = row['NSEID'] + ".NS"  # Append ".NS" to the symbol
#
#         # Fetch data for the company using yfinance
#         end_date = datetime.today().strftime('%Y-%m-%d')
#         start_date = (datetime.today() - timedelta(days=6 * 365)).strftime('%Y-%m-%d')
#         stock_data = yf.download(symbol, start=start_date, end=end_date)
#
#         # Calculate returns for the company
#         returns = calculate_returns(stock_data, periods)
#
#         # Update DataFrame with the fetched data
#         for period, value in returns.items():
#             df.at[index, period] = value
#
#     return df
#
#
# # Example DataFrame
# new_df = pd.DataFrame({
#     'NSEID': ['ITC', 'GODFRYPHLP', 'VSTIND', 'GOLDENTOBC']  # Replace these with your actual symbols
# })
#
# # Fetch data for all companies in the DataFrame and print the result
# result_df = fetch_all_company_data(new_df)
# print(result_df)


import yfinance as yf

# Replace 'AAPL' with the ticker symbol of the stock you're interested in
stock_symbol = 'WIPRO.NS'
# stock_data = yf.download(stock_symbol, start="2024-01-01", end="2024-06-03")
stock_data = yf.download(stock_symbol, start="2024-01-01", end="2024-06-03")
print(stock_data)

stock_data = yf.Ticker(stock_symbol)
print(stock_data.history(period='5y')['Close'])

# Fetch real-time data


# Print real-time price
print("Real-time price of", stock_symbol, ":", stock_data.history(period='1d')['Close'].iloc[-1])

symbol = "WIPRO.NS"  # Append ".NS" to the symbol

# Fetch data for the company using yfinance
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=6*365)).strftime('%Y-%m-%d')
df = stock_data.history(period='6y')
print(f"wipro data: {df['Close']}")
