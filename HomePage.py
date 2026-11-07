# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="🏠",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE
st.title("🛍️ Web Development Lab02")
st.header("CS 1301")
st.subheader("Web Development - Section A")
st.subheader("Melanie Lopez")

st.write("""
Welcome to my Streamlit Web Development Lab02 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. **Visuals**: See where my money goes at 5 stores from June to October (from a JSON file) and compare how much people spend at different stores (from the survey's CSV file).
2. **Survey**: Enter the store you shop at the most and how much you spend there a month. Your answer gets saved and shows up on the Visuals page!
""")

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
# st.image("images/welcome_image.png")
