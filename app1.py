import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd

import json


# Load in the sales data
import csv
import random
import datetime

locations = ["New York", "Chicago", "San Francisco", "Los Angeles", "Miami"]

# Generate random sales data
data = []
for i in range(100):
    date = datetime.datetime.now() - datetime.timedelta(days=i)
    location = random.choice(locations)
    # Generate a random latitude and longitude for the location
    latitude = random.uniform(25, 50)  # Random value between 25 and 50
    longitude = random.uniform(-125, -65)  # Random value between -125 and -65
    sales = random.randint(100, 1000)
    data.append((date.strftime("%Y-%m-%d"), location, latitude, longitude, sales))

# Write the data to a CSV file
with open("sales_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "location", "latitude", "longitude", "sales"])
    writer.writerows(data)

# Load in the sales data
df = pd.read_csv("sales_data.csv")

def intro():
    st.markdown("#### This sample collection was made for studies purposes only.")
    st.markdown("###### It was made with python and streamlit in just a couple of minutes with dummy data, just for proving the concept. Have fun! :smile: ")

def show_sales_over_time():
    # Group the data by date and sum the sales
    sales_by_date = df.groupby("date")["sales"].sum().reset_index()

    # Create a line chart showing the sales over time
    fig = px.line(sales_by_date, x="date", y="sales")
    st.plotly_chart(fig)

def show_sales_by_location():
    # Group the data by location and sum the sales
    sales_by_location = df.groupby("location")["sales"].sum().reset_index()

    # Create a bar chart showing the sales by location
    fig = px.bar(sales_by_location, x="location", y="sales")
    st.plotly_chart(fig)

def show_map():
    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", color="sales")
    fig.write_html("data_graph.html")

    with open("data_graph.html", "r") as f:
        file = f.read()

    st.markdown("#### The data graph is opened in a new tab on your browser.")
    st.download_button(on_click=fig.update_layout(mapbox_style="open-street-map").show(), label="Download the data graph", file_name="data_graph.html", data=file)


st.title("Sales Analysis Dashboard")

# Add a sidebar with options to show different views of the data
view = st.sidebar.selectbox("Choose a view", ["intro", "Sales over time", "Sales by location", "Map"])


if view == "intro":
    intro()
elif view == "Sales over time":
    show_sales_over_time()
elif view == "Sales by location":
    show_sales_by_location()
elif view == "Map":
    show_map()
