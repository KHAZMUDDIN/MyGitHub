import yfinance as yf
# ticker = yf.Ticker("RELIANCE.NS")
ticker = yf.Ticker("reliance.ns")

info = ticker.info
# print(info)
print(info['marketCap'])
print(info['longBusinessSummary'])



# data = ticker.history(period="1mo")
# data = ticker.history(start="2023-01-01", end="2023-05-24")

# financials = ticker.financials
# balance_sheet = ticker.balance_sheet
# cashflow = ticker.cashflow
#
# # print(financials)
#
# earnings = ticker.earnings
# quarterly_earnings = ticker.quarterly_earnings
#
# dividends = ticker.dividends
# print(dividends)
#
# splits = ticker.splits
# print(splits)
#
# sustainability = ticker.sustainability
# print(sustainability)
#
# recommendations = ticker.recommendations
# print(recommendations)
#
# calendar = ticker.calendar
# print(calendar)
#
# actions = ticker.actions
# print(actions)
#
# major_holders = ticker.major_holders
# print(major_holders)
#
# institutional_holders = ticker.institutional_holders
# print(institutional_holders)
#
# mutualfund_holders = ticker.mutualfund_holders
# print(mutualfund_holders)




