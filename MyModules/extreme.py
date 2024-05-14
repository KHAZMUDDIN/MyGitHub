import pandas as pd
import os
import json
import yfinance as yf
from fuzzywuzzy import process
from datetime import datetime


# The code takes the name of the publicaly listed comapny of India and print mainly the Top and Bottom made by the
# Stock price of the coapny on daily basis in the range of <TopBot_line> from <start_date> to <end_date> on <Close> price.
# The last Top or Bottom may be incomplete.

def comp_data(comp):
    folder_path = r'E:\KHAZMUDDIN\BTECH\PYTHON\py_projects\PyStock\Industries'
    all_ind = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]

    for ind in all_ind:
        path = folder_path + '/' + ind + '/' + '/all_comp_of_' + ind + '.xlsx'
        comp_data_of_ind = pd.read_excel(path)
        res = comp_data_of_ind[comp_data_of_ind['Comp_Name'] == comp]

        # Check if the DataFrame is empty
        if res.empty:
            pass
        else:
            print(f"Industry: {ind} \n company: {comp}")
            PATH_json = r'E:\KHAZMUDDIN\BTECH\PYTHON\py_projects\PyStock\Industries\\' + ind + r'\company_info\\' + comp + '.json'
            # Open the JSON file for reading
            with open(PATH_json, 'r') as file:
                # Load the JSON data from the file
                comp_data_json = json.load(file)

            if len(comp_data_json) == 0:
                print(f"No data for {comp}")
                continue
            # Now 'data' contains the contents of the JSON file
            # You can access its contents as a Python dictionary or list

            bseID = comp_data_json['details']['bseId']
            nseID = comp_data_json['details']['nseId']

            if (nseID and bseID):
                compID = nseID + '.BO'
            else:
                if (nseID):
                    compID = nseID + '.NS'
                else:
                    compID = bseID + '.BO'

            try:
                # Fetch historical stock prices for the specified ticker symbols
                stock_data = yf.download(compID, start=start_date, end=end_date)
                return stock_data

            except Exception as e:
                # Handle the exception
                print(f"Failed to download data: {e}")
            break
def nova(comp_name_to_search, TopBot_line=20, start_date='2003-01-03', end_date=datetime.now().strftime('%Y-%m-%d')):

    def search_or_suggest(search_string, list_of_strings):
        # Check if the search_string is in the list_of_strings
        if search_string in list_of_strings:
            return "Yes"  # String found
        else:
            # Find close matches using fuzzy string matching
            matches = process.extract(search_string, list_of_strings, limit=20)
            return matches

    def Top(Pbt,itr,TopBot_line):
        if (itr < total_trading_days):
            temp_list = [Pbt]
            while (itr<total_trading_days):
                maximum = max(temp_list)
                percent = (maximum-list_Prices[itr])/maximum
                if(percent>=TopBot_line):
                    index = list_Prices.index(max(temp_list))
                    local_top = max(temp_list)

                    # Locate the row where the close price matches the target close price
                    target_row = all_data[all_data['Close'] == local_top]

                    # Get the index value (date) of the target row
                    target_date = target_row.index[0]

                    TopBot.loc[len(TopBot.index)] = [target_date,'Top',round(local_top, 0)]
                    temp_list = []
                    Bot(list_Prices[itr],itr,TopBot_line)
                    return
                temp_list.append(list_Prices[itr])
                itr = itr + 1
    def Bot(Ptb,itr,TopBot_line):
        if(itr<total_trading_days):
            temp_list = [Ptb]
            while (itr<total_trading_days):
                minimum = min(temp_list)
                percent = (list_Prices[itr]-minimum)/minimum
                if(percent>=TopBot_line):
                    index = list_Prices.index(min(temp_list))
                    local_bot = min(temp_list)

                    # Locate the row where the close price matches the target close price
                    target_row = all_data[all_data['Close'] == local_bot]

                    # Get the index value (date) of the target row
                    target_date = target_row.index[0]
                    TopBot.loc[len(TopBot.index)] = [target_date, 'Bot', round(local_bot,2)]

                    temp_list = []
                    Top(list_Prices[itr],itr,TopBot_line)
                    return
                temp_list.append(list_Prices[itr])
                itr = itr + 1

    TopBot_line = TopBot_line/100
    # Directory containing Excel files
    folder_path = r'E:\KHAZMUDDIN\BTECH\PYTHON\py_projects\PyStock\Industries'

    all_data = comp_data(comp_name_to_search)

    total_trading_days = len(all_data)

    list_Percent_Change = []
    list_Prices = []

    for i in range(total_trading_days):
        list_Prices.append(all_data["Close"].iloc[i])

    TopBot = pd.DataFrame(columns=["Date",'TopBot',"Price"])

    i = 1
    while (i<total_trading_days):
        price = list_Prices[i]
        percent = (price-list_Prices[0])/list_Prices[0]
        if(percent>=TopBot_line):
            Top(price,i,TopBot_line)
            break
        elif(percent<(-TopBot_line)):
            Bot(price,i,TopBot_line)
            break
        else:
            i = i + 1

    last_row_TopBot = TopBot.iloc[-1]  # Get the last row of the DataFrame

    last_date = pd.Timestamp(last_row_TopBot['Date'])
    last_price = last_row_TopBot['Price']

    # Filter the DataFrame based on the condition
    filtered_df_TopBot = all_data[all_data.index > last_date]

    if(last_row_TopBot['TopBot']=='Top'):
        min_value = filtered_df_TopBot['Close'].min()
        percent_last = ((last_price-min_value)/last_price)
        # Locate the row where the close price matches the target close price
        target_row_last = filtered_df_TopBot[filtered_df_TopBot['Close'] == min_value]
        # Get the index value (date) of the target row
        target_date_last = target_row_last.index[0]

        if(percent_last>=TopBot_line):
            TopBot.loc[len(TopBot.index)] = [target_date_last, 'Bot', round(min_value, 0)]
            pass
        pass
    else:
        max_value = filtered_df_TopBot['Close'].max()
        percent_last = ((max_value-last_price) / last_price)
        # Locate the row where the close price matches the target close price
        target_row_last = filtered_df_TopBot[filtered_df_TopBot['Close'] == max_value]
        # Get the index value (date) of the target row
        target_date_last = target_row_last.index[0]
        if (percent_last >= TopBot_line):
            TopBot.loc[len(TopBot.index)] = [target_date_last, 'Top', round(max_value, 0)]
            pass
        pass

    CngPercent = []
    No_of_Days = []
    for item in range(len(TopBot)):
        if(item==0):
            No_of_Days.append(0)
            CngPercent.append(0)
            continue
        temp_cng = ((TopBot.iloc[item,2]-TopBot.iloc[(item-1),2])/TopBot.iloc[(item-1),2])*100
        temp_days = (TopBot.iloc[item,0]-TopBot.iloc[(item-1),0])
        No_of_Days.append(temp_days.days)
        CngPercent.append(round(temp_cng,2))

    TopBot["Cng%"] = CngPercent
    TopBot["Days"] = No_of_Days
    TopBot['day_of_week'] = TopBot['Date'].dt.strftime('%A')

    return TopBot
if __name__ == "__main__":
    # Code here will only execute when the file is run directly
    # ================================================================
    cname = 'wipro'
    line = 20  # 10 for 10% or 25 for 25%
    start_date = '2003-01-03'
    end_date = '2024-04-01'
    # =================================================================

    result = nova(cname,line,start_date,end_date)

    print(result)
