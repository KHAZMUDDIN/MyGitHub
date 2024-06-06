# import requests
#
# def get_company_logo(domain):
#     response = requests.get(f"https://logo.clearbit.com/{domain}")
#     if response.status_code == 200:
#         return response.url
#     else:
#         return None
#
# # Example usage
# company_domains = ["ril.com", "tcs.com", "infosys.com"]
# logos = {domain: get_company_logo(domain) for domain in company_domains}
#
# for domain, logo_url in logos.items():
#     print(f"{domain}: {logo_url}")


# import os
# import shutil
# import pandas as pd
# import requests
#
# def get_company_logo(domain):
#     response = requests.get(f"https://logo.clearbit.com/{domain}")
#     if response.status_code == 200:
#         return response.url
#     else:
#         return None
#
# def download_image(url, save_path):
#     response = requests.get(url)
#     if response.status_code == 200:
#         with open(save_path, 'wb') as file:
#             file.write(response.content)
#
# # Specify the path to your default image
# default_image_path = r"E:\KHAZMUDDIN\BTECH\PYTHON\Django Projects\DonFin\static\images\default logo.png"
#
# logos = {}
# all_comp = pd.read_excel(r'E:\KHAZMUDDIN\BTECH\PYTHON\Django Projects\DonFin\static\data\NSE_all_comp_extended.xlsx')
#
# # Slice the DataFrame to include only the first 5 rows
# # first_5_rows = all_comp.head(5)
# count = 1
# # for index, row in first_5_rows.iterrows():
# for index, row in all_comp.iterrows():
#     # print(row)
#     # Example usage
#     # company_domains = ["ril.com", "tcs.com", "infosys.com"]
#
#     # Remove "Limited" using replace()
#     row["Company Name"] = row["Company Name"].replace("Limited", "")
#     logos[row["Company Name"]] = get_company_logo(row["website"])
#     print("==================================================================")
#     print(f"index: {count}: {row["Company Name"]}")
#     print("==================================================================")
#     count = count + 1
#     # logos = {domain: get_company_logo(domain) for domain in company_domains}
#
# # Create a folder to save the images
# folder_name = r"E:\KHAZMUDDIN\BTECH\PYTHON\Django Projects\DonFin\static\images\company logos"
# os.makedirs(folder_name, exist_ok=True)
#
# count = 1
# # Download and save each logo
# for domain, logo_url in logos.items():
#     if logo_url:
#         image_name = f"{domain}.png"
#         save_path = os.path.join(folder_name, image_name)
#         download_image(logo_url, save_path)
#         print("==================================================================")
#         print(f"index {count}: Downloaded logo for {domain} and saved as {save_path}")
#         print("==================================================================")
#     else:
#         # If logo_url is not available, save the default image
#         default_save_path = os.path.join(folder_name, f"{domain}.png")
#         shutil.copyfile(default_image_path, default_save_path)
#         print("==================================================================")
#         print(f"index {count}: No logo found for {domain}, saved default image as {default_save_path}")
#         print("==================================================================")
#     count = count + 1
