# This creates the page for displaying data visualizations.

import streamlit as st
import json
import pandas as pd
import plotly.express as px

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈")


# PART 1: GRAPHS FROM data.json
# --- YOUR CODE GOES HERE ---
with open("data.json") as f:
    data = json.load(f)

st.subheader("Total Spending by Store")
st.write("This is a static visualization! It always looks the same.")

stores = []
totals = []
for point in data["data_points"]:
    stores.append(point["label"])
    totals.append(sum(point["spending"]))

fig1 = px.pie(names=stores, values=totals, title="Total Spending by Store (Jun–Oct)")
st.plotly_chart(fig1)
st.subheader("Monthly Spending Over Time")
st.write("This is a dynamic visualization! Pick stores to compare.")

# session state: remembers which stores are picked
if "selected_stores" not in st.session_state:
    st.session_state.selected_stores = stores[:]

st.multiselect("Choose stores", stores, key="selected_stores")

# build the lists for the line chart
x_months = []
y_spending = []
store_color = []
for point in data["data_points"]:
    if point["label"] in st.session_state.selected_stores:
        for i in range(len(data["months"])):
            x_months.append(data["months"][i])
            y_spending.append(point["spending"][i])
            store_color.append(point["label"])

if len(x_months) == 0:
    st.warning("Pick at least one store!")
else:
    fig2 = px.line(x=x_months, y=y_spending, color=store_color, markers=True,
                   title="Monthly Spending by Store",
                   labels={"x": "Month", "y": "Spending ($)", "color": "Store"})
    st.plotly_chart(fig2)


# PART 2: GRAPHS FROM data.csv
# --- YOUR CODE GOES HERE ---
csv_data = pd.read_csv("data.csv")
csv_stores = list(csv_data["Category"])
csv_amounts = list(csv_data["Value"])

if len(csv_stores) == 0:
    st.warning("No survey data yet! Go fill out the Survey page.")
else:
    # STATIC CHART: average spending per store
    st.subheader("Average Monthly Spending by Store (Survey)")
    st.write("This is a static visualization! It always looks the same.")

    # dictionary: store -> [total $, number of answers]
    store_info = {}
    for i in range(len(csv_stores)):
        store = csv_stores[i]
        if store not in store_info:
            store_info[store] = [0, 0]
        store_info[store][0] += csv_amounts[i]
        store_info[store][1] += 1

    bar_stores = []
    bar_averages = []
    for store, info in store_info.items():
        bar_stores.append(store)
        bar_averages.append(info[0] / info[1])

    fig3 = px.bar(x=bar_stores, y=bar_averages, title="Average Monthly Spending by Store",
                  labels={"x": "Store", "y": "Average Spending ($)"})
    st.plotly_chart(fig3)

    # DYNAMIC CHART: every answer, filtered by a slider
    st.subheader("Survey Answers Above a Spending Amount")
    st.write("This is a dynamic visualization! Move the slider to filter answers.")

    # session state: remembers the slider value
    if "min_spend" not in st.session_state:
        st.session_state.min_spend = 0

    st.slider("Minimum spending ($)", 0, max(csv_amounts), key="min_spend")

    x_stores = []
    y_amounts = []
    for i in range(len(csv_stores)):
        if csv_amounts[i] >= st.session_state.min_spend:
            x_stores.append(csv_stores[i])
            y_amounts.append(csv_amounts[i])

    if len(x_stores) == 0:
        st.warning("No answers that high! Move the slider down.")
    else:
        fig4 = px.scatter(x=x_stores, y=y_amounts, title="Survey Answers by Store",
                          labels={"x": "Store", "y": "Monthly Spending ($)"})
        st.plotly_chart(fig4)
