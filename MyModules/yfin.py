import pandas as pd
import yfinance as yf
import warnings
from datetime import datetime, timedelta

# Suppress specific FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning, message=".*TimedeltaIndex construction is deprecated.*")
#
# def ret(new_df):
#     # Example new_df DataFrame
#
#     # Define periods and labels
#     periods = {
#         '1day': timedelta(days=2),
#         '1week': timedelta(days=8),
#         '1month': timedelta(days=31),
#         '3months': timedelta(days=91),
#         '6months': timedelta(days=181),
#         '1year': timedelta(days=366),
#         '5years': timedelta(days=5 * 365 + 1)
#     }
#
#     # Function to calculate returns
#     def calculate_returns(symbols):
#         end_date = datetime.today().strftime('%Y-%m-%d')
#         start_date = (datetime.today() - timedelta(days=6*365)).strftime('%Y-%m-%d')
#         stock_data = yf.download(symbols, start=start_date, end=end_date)
#
#         if stock_data.empty:
#             return {symbol: {period: None for period in periods.keys()} for symbol in symbols}
#
#         returns = {symbol: {} for symbol in symbols}
#
#         for period, delta in periods.items():
#             target_date = datetime.today() - delta
#
#             for symbol in symbols:
#                 try:
#                     current_close = stock_data['Close'][symbol].iloc[-1]
#                     past_data = stock_data['Close'][symbol][stock_data.index <= target_date]
#
#                     if not past_data.empty:
#                         past_close = past_data.iloc[-1]
#                         returns[symbol][period] = ((current_close - past_close) / past_close) * 100
#                     else:
#                         returns[symbol][period] = None
#                 except KeyError:
#                     returns[symbol][period] = None
#
#         return returns
#
#     # Fetch returns for all symbols in new_df
#     symbols = new_df['NSEID'].tolist()
#     # Add ".NS" to each element
#     symbols = [element + ".NS" for element in symbols]
#     returns = calculate_returns(symbols)
#
#     # Add return columns to new_df and fill with calculated values
#     for period in periods.keys():
#         new_df[period] = new_df['NSEID'].apply(lambda x: returns[x][period] if x in returns else None)
#
#     return new_df
#
# # Example new_df DataFrame
# new_df = pd.DataFrame({
#     'NSEID': ['ITC', 'GODFRYPHLP', 'VSTIND', 'GOLDENTOBC']  # Replace these with your actual symbols
# })
#
# df = ret(new_df)
# print(df)

# import pandas as pd
# import yfinance as yf
# import warnings
# from datetime import datetime, timedelta
#
# # Suppress specific FutureWarning
# warnings.filterwarnings("ignore", category=FutureWarning, message=".*TimedeltaIndex construction is deprecated.*")
#
# def ret(new_df):
#     # Define periods and labels
#     periods = {
#         '1day': timedelta(days=2),
#         '1week': timedelta(days=8),
#         '1month': timedelta(days=31),
#         '3months': timedelta(days=91),
#         '6months': timedelta(days=181),
#         '1year': timedelta(days=366),
#         '5years': timedelta(days=5 * 365 + 1)
#     }
#
#     # Function to calculate returns
#     def calculate_returns(symbol):
#         try:
#             end_date = datetime.today().strftime('%Y-%m-%d')
#             start_date = (datetime.today() - timedelta(days=6*365)).strftime('%Y-%m-%d')
#             stock_data = yf.download(symbol, start=start_date, end=end_date)
#
#             if stock_data.empty:
#                 return {period: None for period in periods.keys()}
#
#             returns = {}
#
#             for period, delta in periods.items():
#                 target_date = datetime.today() - delta
#                 past_data = stock_data['Close'][stock_data.index <= target_date]
#
#                 if not past_data.empty:
#                     current_close = stock_data['Close'].iloc[-1]
#                     past_close = past_data.iloc[-1]
#                     returns[period] = ((current_close - past_close) / past_close) * 100
#                 else:
#                     returns[period] = None
#
#             return returns
#         except Exception as e:
#             print(f"Error occurred for {symbol}: {e}")
#             return {period: None for period in periods.keys()}
#
#     # Fetch returns for all symbols in new_df
#     new_df['Returns'] = new_df['NSEID'].apply(calculate_returns)
#
#     # Extract returns for each period
#     for period in periods.keys():
#         new_df[period] = new_df['Returns'].apply(lambda x: x[period])
#
#     # Drop the 'Returns' column
#     new_df.drop(columns=['Returns'], inplace=True)
#
#     return new_df
#
# # Example new_df DataFrame
# new_df = pd.DataFrame({
#     'NSEID': ['ITC', 'GODFRYPHLP', 'VSTIND', 'GOLDENTOBC']  # Replace these with your actual symbols
# })
#
# df = ret(new_df)
# print(df)

all_comp = ['ITC', 'GODFRYPHLP', 'VSTIND', 'GOLDENTOBC']

end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=6*365)).strftime('%Y-%m-%d')
print(f"From {start_date} to {end_date}")

for comp in all_comp:
    stock_data = yf.download(comp+".NS", start=start_date, end=end_date)
    print(stock_data)



