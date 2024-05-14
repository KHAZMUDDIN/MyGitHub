import streamlit as st
import os
import sys
# Add the path to the main program folder
sys.path.append(r'E:\KHAZMUDDIN\BTECH\PYTHON\py_projects\PyStock\my_modules')
import extreme
import all_comp_ind_as_list

# Append the parent directory to the system path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import MyModules.After_N_Neg_Months as NMR
import pandas as pd
import streamlit as st


# TopBot_Finder has a function name <nova>. It takes 4 arguments or parameters (in order) <company name> (string), <TopBot_line> (float b/w (0,1)),
# <start_date> (string 'yyyy-mm-dd') and <end_date> (string 'yyyy-mm-dd') respectively.
# when nova call as <TopBot2.nova(all parameters in order)> it will return the Top and Bottom details of the companies closing price on
# daily basis which happens b/w <start_date> and <end_date> for TobBot_line.

# ================================================================
comp_name = 'wipro'
TopBot_line = 0.2  # 0.1 for 10% or 0.25 for 25%
start_date = '2003-01-03'
end_date = '2024-04-01'
# =================================================================

def main():
    st.title("Streamlit Multi-Page App")

    # Add a sidebar
    st.sidebar.title("Navigation")
    page_options = ["Home", "After Negative Month", "Contact"]
    page = st.sidebar.selectbox("Go to", page_options)

    # Display different pages based on the user's selection
    if page == "Home":
        show_home_page()
    elif page == "After Negative Month":
        After_Negative_Month()
    elif page == "Contact":
        show_contact_page()

def show_home_page():
    st.header("Home Page")
    st.write("Welcome to the Home Page!")
    all_comp_name = all_comp_ind_as_list.init()

    # =====================Streamlit======================================
    # Title
    st.title("Top and Bottom Finder of any stock")

    # Markdown
    st.markdown("Enter the name of any publicaly listed company of India")

    # Selection box

    # first argument takes the titleof the selectionbox
    # second argument takes options
    company_name = st.selectbox("Company name: ",
                                all_comp_name)

    # print the selected hobby
    st.write("Company you entered: ", company_name)

    TopBot = extreme.nova(company_name)

    if (st.button('Submit')):
        if (TopBot.empty):
            print(f"No Data for {company_name}")
        else:
            st.write(f"Processing data for: {company_name}")
            st.write(TopBot)
            st.success(f"TopBot of {company_name}")

def After_Negative_Month():
    st.header("After Negative Month")
    st.write("After N consecutive months of negative returns of the given industry the probability(in %) "
             "that the n+1 or next month will give positive return is:")
    all_ind_name = all_comp_ind_as_list.all_ind()
    # Markdown
    # st.markdown("Enter the name of the Industry")

    # Selection box

    # first argument takes the titleof the selectionbox
    # second argument takes options
    ind_name = st.selectbox("Enter the name of the Industry:",all_ind_name)
    # st.markdown("Enter the number of negative months of return:")

    # Create an integer input widget
    no_of_months = st.number_input(
        label="Enter the number of negative months of return:",  # The label for the input field
        min_value=1,  # Minimum value (optional)
        max_value=10,  # Maximum value (optional)
        value=3,  # Default value
        step=1,  # Step size
        format="%d"  # Format to ensure integer input
    )

    # print the selected hobby
    st.write("Industry you entered: ", ind_name)
    next_months_df = NMR.next_month_return(ind_name,no_of_months)
    if (st.button('Submit')):
        if (next_months_df.empty):
            print(f"No Data for {ind_name}")
        else:
            st.write(f"Processing data for: {ind_name}")
            # st.write(next_months_df)
            st.dataframe(next_months_df, width=400)
            # st.success(f"TopBot of {company_name}

    def percentage_of_positives(numbers):
        # Count the number of positive numbers
        positive_count = sum(1 for num in numbers if num > 0)

        # Calculate the percentage
        total_count = len(numbers)
        if total_count == 0:
            return 0.0  # Return 0 if the list is empty
        else:
            return (positive_count / total_count) * 100.0

    same_ret = next_months_df.iloc[:, 1].tolist()

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

    st.write(f"The scenerio happens {len(same_ret)} times from the date 3rd Jan 2000 out of which {count_pos} next months gives positive returns.\n")
    # Calculate the percentage of positive numbers
    percentage = round(percentage_of_positives(same_ret), 2)

    if (no_of_months == 1):
        st.write(
            f"After {no_of_months} consecutive Months of Negative Returns of the {ind_name} industry the probability(in %) that the {no_of_months + 1}nd or the next month will give positive return is: ", percentage, "%")
    elif (no_of_months == 2):
        st.write(
            f"After {no_of_months} consecutive Months of Negative Returns of the {ind_name} industry the probability(in %) that the {no_of_months + 1}rd or the next month will give positive return is: ", percentage, "%")
    else:
        st.write(
            f"After {no_of_months} consecutive Months of Negative Returns of the {ind_name} industry the probability(in %) that the {no_of_months + 1}th or the next month will give positive return is: ", percentage, "%")




def show_contact_page():
    st.header("Contact Page")
    st.write("You can contact us at contact@example.com.")

if __name__ == "__main__":
    main()
