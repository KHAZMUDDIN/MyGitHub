import streamlit as st
import sys
# Add the path to the main program folder
sys.path.append(r'E:\KHAZMUDDIN\BTECH\PYTHON\py_projects\PyStock\my_modules')
import extreme
import all_comp_ind_as_list
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
    page_options = ["Home", "About", "Contact"]
    page = st.sidebar.selectbox("Go to", page_options)

    # Display different pages based on the user's selection
    if page == "Home":
        show_home_page()
    elif page == "About":
        show_about_page()
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

def show_about_page():
    st.header("About Page")
    st.write("This is the About Page. Learn more about us here.")

def show_contact_page():
    st.header("Contact Page")
    st.write("You can contact us at contact@example.com.")

if __name__ == "__main__":
    main()
