import os

import pandas as pd


def comp_name_of_ind(ind):
    # Directory path
    directory = r'E:\KHAZMUDDIN\BTECH\PYTHON\py_projects\PyStock\Industries\\' + ind + '\\profit-lossVI'

    # Get all file names in the directory
    files = os.listdir(directory)

    # Extract file names without extensions
    file_names = [os.path.splitext(file)[0] for file in files]

    # Print the file names without extensions
    # for file_name in file_names:
    #     print(file_name)
    return file_names


def all_ind():
    path = r'E:\KHAZMUDDIN\BTECH\PYTHON\py_projects\PyStock\Industries\\all_industries.xlsx'
    all_ind = pd.read_excel(path)
    all_ind_name = all_ind['Industry_Name'].tolist()
    return all_ind_name


def init():
    all_ind_name = all_ind()
    # print(all_ind_name)
    all_comp = []
    for item in all_ind_name:
        result = comp_name_of_ind(item)
        all_comp = all_comp + result
    return all_comp
    # # Count the number of empty strings using a loop
    # empty_count = 0
    # for item in all_comp:
    #     if item == "":
    #         empty_count += 1
    # print(empty_count)


if __name__ == "__main__":
    result = init()
    print(result)
