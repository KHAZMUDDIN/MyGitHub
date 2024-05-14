import pandas as pd


def next_month_return(ind, no_of_months, status='-', line=-0, over_fall=-0):
    def percentage_of_positives(numbers):
        # Count the number of positive numbers
        positive_count = sum(1 for num in numbers if num > 0)

        # Calculate the percentage
        total_count = len(numbers)
        if total_count == 0:
            return 0.0  # Return 0 if the list is empty
        else:
            return (positive_count / total_count) * 100.0

    # Directory containing Excel files
    folder_path = r'E:\KHAZMUDDIN\BTECH\PYTHON\py_projects\PyStock\Industries\\' + ind

    all_comp_stock_returns_of_ind_every_year = pd.read_excel(
        folder_path + '//all_comp_monthly_stock_returns_of_' + ind + '.xlsx')

    series_of_mean_ret_of_ind = all_comp_stock_returns_of_ind_every_year['Mean']

    series_of_mean_ret_of_ind.index = all_comp_stock_returns_of_ind_every_year.iloc[:, 0]
    series_of_mean_ret_of_ind.index = series_of_mean_ret_of_ind.index.map(lambda x: x.date())
    # Reverse the Series along with its index
    series_of_mean_ret_of_ind = series_of_mean_ret_of_ind[::-1]
    series_of_mean_ret_of_ind = series_of_mean_ret_of_ind[1:]

    # for index, value in series_of_mean_ret_of_ind.items():
    #     print(f"End of Month : {index}, mean return: {value}")

    def percent_change(change_percent):
        return total_change * (1 + (change_percent) / 100)

    same_ret = []
    same_ret_date = []
    # Iterate over the integer indexes and access corresponding values
    for i in range(len(series_of_mean_ret_of_ind) - no_of_months):
        total_change = 1
        sum_percant = 0
        break_outer_loop = False
        value = series_of_mean_ret_of_ind.iloc[i]
        index_value = series_of_mean_ret_of_ind.index[i]

        if (status == '-'):
            if (value >= line):
                continue
            # sum_percant = sum_percant + value
            total_change = percent_change(value)
            for j in range(1, no_of_months):
                # sum_percant = sum_percant + series_of_mean_ret_of_ind.iloc[i+j]
                total_change = percent_change(series_of_mean_ret_of_ind.iloc[i + j])
                if (series_of_mean_ret_of_ind.iloc[i + j] >= line):
                    break_outer_loop = True  # Set flag to True
                    break
            if (break_outer_loop):
                continue
            change_percent = (total_change - 1) * 100
            # same_ret.append(series_of_mean_ret_of_ind.iloc[i + no_of_months])
            if (change_percent < over_fall):
                print(
                    f"{series_of_mean_ret_of_ind.index[i + no_of_months]}: {series_of_mean_ret_of_ind.iloc[i + no_of_months]} ({round(change_percent, 2)})")
                same_ret.append(series_of_mean_ret_of_ind.iloc[i + no_of_months])
                same_ret_date.append(series_of_mean_ret_of_ind.index[i + no_of_months])
        else:
            pass

        # print("Integer Index:", i)
        # print("Value:", value)
        # print("index:", index_value)

    # Ensure the lists have the same length
    if len(same_ret) == len(same_ret_date):
        # Create a DataFrame with the lists as columns
        Next_Month_Ret = pd.DataFrame({
            'Next Month End Date': same_ret_date,
            'Next Month Return(in %)': same_ret
        })

    sum_pos = 0
    count_pos = 0
    sum_neg = 0
    count_neg = 0
    for item in same_ret:
        if (item >= 0):
            sum_pos = sum_pos + item
            count_pos = count_pos + 1
        else:
            sum_neg = sum_neg + item
            count_neg = count_neg + 1

    print(f"The scenerio happens {len(same_ret)} times from the date 3rd Jan 2000 out of which {count_pos} "
          f"next months gives positive returns.\n")
    # Calculate the percentage of positive numbers
    percentage = round(percentage_of_positives(same_ret), 2)

    if (no_of_months == 1):
        print(
            f"After {no_of_months} consecutive Months of Negative Returns of the {ind} industry the probability(in %) "
            f"that the {no_of_months + 1}nd or the next month will give positive return is: ", percentage, "%")
    elif (no_of_months == 2):
        print(
            f"After {no_of_months} consecutive Months of Negative Returns of the {ind} industry the probability(in %) "
            f"that the {no_of_months + 1}rd or the next month will give positive return is: ", percentage, "%")
    else:
        print(
            f"After {no_of_months} consecutive Months of Negative Returns of the {ind} industry the probability(in %) "
            f"that the {no_of_months + 1}th or the next month will give positive return is: ", percentage, "%")

    # if(count_pos != 0):
    #     print(f"Average positive return: {round(sum_pos/count_pos,0)}")
    #
    # if (count_neg != 0):
    #     print(f"Average negative return: {round(sum_neg/count_neg,0)}")

    return Next_Month_Ret


if __name__ == "__main__":
    # ================================================
    # ind = 'bank-public'
    ind = 'bank-private'
    # ind = 'aquaculture'
    # ind = 'it-services-consulting'
    # ind = 'paints'
    # ind = 'laminatesdecoratives'
    line = -0
    # status = '+'
    status = '-'
    no_of_months = 3
    over_fall = -0

    # ===============================================
    result = next_month_return(ind, no_of_months, status, line, over_fall)
    print(result)
