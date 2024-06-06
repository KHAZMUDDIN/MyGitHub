import os
import pandas as pd
import json
def comp_data(comp):
    # Directory containing Excel files
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
            return comp_data_json

            # if len(comp_data_json) == 0:
            #     print(f"No data for {comp}")
            #     continue

if __name__ == "__main__":
    # Code here will only execute when the file is run directly
    comp = "wipro"
    data = comp_data(comp)
    print(data)


