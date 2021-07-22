import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Define the dataframe variable
global df
global numeric_columns
global categorical_columns
global column_names
global text_input

# Title of streamlit Application
st.title("Visualization Application")

# Add a subheading to the side bar
st.sidebar.subheader("Settings")

# Create an upload file section in the sidebar
upload_file = st.sidebar.file_uploader(label="Upload your CSV file", type=["csv"])

if upload_file is not None:
    try:
        df = pd.read_csv(upload_file)
        st.write(df)
        numeric_columns = list(df.select_dtypes(['float','int']).columns)
        categorical_columns = list(df.describe(exclude='number').columns)
        column_names = list(df.columns)
    except Exception as e:
        st.write("Please upload a file in CSV format")

text_input = st.sidebar.text_input(label='Enter chart title')

chart_select = st.sidebar.selectbox(
    label="Select chart type",
    options = ["Scatterplot","Boxplot","Lineplot", "Histogram"]
)


if chart_select == "Scatterplot":
    st.sidebar.subheader("Scatterplot Settings")
    try:
        x_values = st.sidebar.selectbox("X-axis",options=numeric_columns)
        y_values = st.sidebar.selectbox("Y-axis",options=numeric_columns)
        color_values = st.sidebar.selectbox("Color",options=categorical_columns)

        plot = px.scatter(data_frame = df,x = x_values,y=y_values,color=color_values,title=text_input)

        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == "Lineplot":
    st.sidebar.subheader("Lineplot Settings")
    try:
        x_values = st.sidebar.selectbox("X-axis",options=numeric_columns)
        y_values = st.sidebar.selectbox("Y-axis",options=numeric_columns)

        plot = px.line(df, x=x_values, y=y_values, title=text_input)

        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == "Histogram":
    st.sidebar.subheader("Histogram Settings")
    try:
        x_values = st.sidebar.selectbox("X-axis",options=column_names)

        plot = px.histogram(df, x=x_values, title=text_input)

        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == "Boxplot":
    st.sidebar.subheader("Boxplot Settings")
    try:
        y_values = st.sidebar.selectbox("Y-axis",options=column_names)

        plot = px.box(df, y=y_values, title=text_input)

        st.plotly_chart(plot)
    except Exception as e:
        print(e)

        