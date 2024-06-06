# import pandas as pd
# import yfinance as yf
# # Download the all companies of nse website(https://www.nseindia.com/regulations/listing-compliance/nse-market-capitalisation-all-companies)
# # Format the file as it contains only two columns name (Symbol, Company Name) remove all the companies rows which are
# # currently not listed and other utt pattang texts. and name the file as <NSE_AllComp_28MAR2024.xlsx> change the date part from the file.
# # all the fills which will be read and write by this <NSE_ALL_Companies.py> file will be done within the folder
# # <E:\KHAZMUDDIN\BTECH\PYTHON\Django Projects\DonFin\static\> of this PC
# # paste the file path in the below 'path' variable and run the code and will generate an .xlsx file in the same folder (/static)
# # name <Name_Ind_NSEID.xlsx>
# # also create an excel file name <All_YInd.xlsx> whithin the same folder(/static) which has only one column name(Ind) which contains
# # all the unique <industry> name of the <Ind> column of the generated <Name_Ind_NSEID.xlsx> file.

# # ===============================================================================================================
# path = r'E:\KHAZMUDDIN\BTECH\PYTHON\Django Projects\DonFin\static\NSE_AllComp_28MAR2024.xlsx'
# # ===============================================================================================================

# all_comp = pd.read_excel(path)
# # print(all_comp)
#
# # Define the data for the DataFrame
# data = {
#     "Symbol": [],
#     "Company Name": [],
#     "industry": [],
#     "industryKey": [],
#     "industryDisp": [],
#     "sector": [],
#     "sectorKey": [],
#     "sectorDisp": [],
#     "city": [],
#     "website": []
# }
#
# # Create the DataFrame
# df = pd.DataFrame(data)
#
# # Assuming `all_comp` is your DataFrame
# # for index, row in all_comp.head(5).iterrows():
# for index, row in all_comp.iterrows():
#     comp = row["Symbol"]
#     comp_full = row["Company Name"]
#     print("===============================================")
#     print(f"Index: {index}  Company Name: {comp_full}")
#     print("===============================================")
#
#     try:
#         ticker = yf.Ticker(comp + ".NS")
#         info = ticker.info
#     except:
#         continue
#
#     # Define the data for the new row
#     new_row_data = {
#         "Symbol": comp,
#         "Company Name": comp_full,
#         "industry": info.get('industry', None),
#         "industryKey": info.get('industryKey', None),
#         "industryDisp": info.get('industryDisp', None),
#         "sector": info.get('sector', None),
#         "sectorKey": info.get('sectorKey', None),
#         "sectorDisp": info.get('sectorDisp', None),
#         "city": info.get('city', None),
#         "website": info.get('website', None)
#     }
#
#     # Append the new row to the DataFrame
#     df = df._append(new_row_data, ignore_index=True)
#
# print(df)
# df.to_excel(r'E:\KHAZMUDDIN\BTECH\PYTHON\Django Projects\DonFin\static\Name_Ind_NSEID.xlsx', index=False)





