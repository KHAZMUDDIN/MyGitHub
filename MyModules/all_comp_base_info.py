import os
import pandas as pd
import json

# comp_base_info() returns a dataframe which contains all the 4000+ companies basic data like the followings
# ['Name', 'Ind', 'NSEID','BSEID','About','City','State','Nifty50','Sensex','BSE100','BSE200','BSE500','CNXMIDCAP200','Web','Email']

def comp_base_info():
    globalDF = pd.DataFrame(columns=['Name', 'Ind', 'NSEID','BSEID','About','City','State','Nifty50','Sensex','BSE100','BSE200','BSE500','CNXMIDCAP200','Web','Email'])
    # Directory containing Excel files
    folder_path = r'E:\KHAZMUDDIN\BTECH\PYTHON\py_projects\PyStock\Industries'
    all_ind = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]
    countPerfect = 0
    countError = 0

    for ind in all_ind:
        path = folder_path + '/' + ind + '/' + '/company_info'

        # Ensure the provided directory exists
        if not os.path.isdir(path):
            raise NotADirectoryError(f"The provided path '{path}' is not a directory or does not exist.")

        # List all files in the directory
        files = os.listdir(path)

        # Filter out only the JSON files and remove their extensions
        json_files = [os.path.splitext(file)[0] for file in files if file.endswith('.json')]

        for comp in json_files:
            comp_path = path + '/' + comp + '.json'
            # Open and read the file content
            with open(comp_path, 'r') as file:
                content = json.load(file)

            # Check if the content is an empty JSON object or array
            if content == {} or content == []:
                continue
            else:
                # Define the new dictionary with keys
                try:
                    new_row = {
                        'Name': comp,
                        'Ind': ind,
                        'NSEID': content["details"]["nseId"],
                        'BSEID': content["details"]["bseId"],
                        'About': content["About the Company"],
                        'City': content["address"]["city"],
                        'State': content["address"]["state"],
                        'Nifty50': next((item["value"] for item in content["listing"] if item["name"] == "NIFTY 50"), None),
                        'Sensex': next((item["value"] for item in content["listing"] if item["name"] == "SENSEX"), None),
                        'BSE100': next((item["value"] for item in content["listing"] if item["name"] == "BSE 100"), None),
                        'BSE200': next((item["value"] for item in content["listing"] if item["name"] == "BSE 200"), None),
                        'BSE500': next((item["value"] for item in content["listing"] if item["name"] == "BSE 500"), None),
                        'CNXMIDCAP200': next(
                            (item["value"] for item in content["listing"] if item["name"] == "CNX MIDCAP 200"), None),
                        'Web': content["address"]["web"],
                        'Email': content["address"]["email"]
                    }

                    # print(new_row)

                    # Add the new row to the DataFrame
                    globalDF.loc[len(globalDF)] = new_row
                    countPerfect = countPerfect + 1
                except:
                    countError = countError + 1
                    continue
    # print(f"Error: {countError}")
    # print(f"Perfect: {countPerfect}")
    return globalDF


if __name__ == "__main__":
    # Code here will only execute when the file is run directly
    data = comp_base_info()
    print(data)

    try:
        data.to_excel(r'E:\KHAZMUDDIN\BTECH\PYTHON\py_projects\PyStock\Industries\\all_companies_info.xlsx', index=False)
    except:
        pass




