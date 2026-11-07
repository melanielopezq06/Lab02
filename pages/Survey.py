# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("Data Collection Survey 📝")
st.write("Please fill out the form below to add your data to the dataset.")

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):
    # Create text input widgets for the user to enter data.
    # The first argument is the label that appears above the input box.
    category_input = st.text_input("Where do you shop the most? (ex: Target)")
    value_input = st.text_input("How much do you spend there a month? (whole number, ex: 40)")

    # The submit button for the form.
    submitted = st.form_submit_button("Submit Data")

    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
        # clean the inputs: strip spaces + same case so "Target " and "target" match
        store = category_input.strip().lower()
        amount = value_input.strip()

        if store == "" or amount == "":
            st.error("Please fill out both boxes!")
        elif not amount.isdigit():
            st.error("Spending has to be a whole number (ex: 40)")
        else:
            # "a" = append mode, adds a new row without erasing the old ones
            with open("data.csv", "a") as f:
                f.write(store + "," + amount + "\n")

            st.success("Your data has been submitted!")
            st.write("You entered: **Store:** {}, **Spending:** ${}".format(store, amount))

# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")
