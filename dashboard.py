import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

sns.set(style='dark')

st.title("Bike Rental Dashboard")
st.header("Exploring Bike Rentals based on Weather and Time")

# File upload section
st.subheader("Upload Data Files")
uploaded_day = st.file_uploader("Upload day.csv", type=["csv"])
uploaded_hour = st.file_uploader("Upload hour.csv", type=["csv"])

if uploaded_day is not None and uploaded_hour is not None:
    df_day = pd.read_csv(uploaded_day)
    df_hour = pd.read_csv(uploaded_hour)
    
    st.subheader("Day Dataset Preview")
    st.dataframe(df_day.head())
    
    st.subheader("Hour Dataset Preview")
    st.dataframe(df_hour.head())
    
    # Visualizations
    st.subheader("Bike Rentals by Weather Condition (Day Dataset)")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='weathersit', y='cnt', data=df_day, ax=ax)
    ax.set_title("Bike Rentals by Weather Condition (Day Dataset)")
    ax.set_xlabel("Weather Condition")
    ax.set_ylabel("Bike Rentals (cnt)")
    st.pyplot(fig)
    
    st.subheader("Bike Rentals by Weather Condition (Hour Dataset)")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='weathersit', y='cnt', data=df_hour, ax=ax)
    ax.set_title("Bike Rentals by Weather Condition (Hour Dataset)")
    ax.set_xlabel("Weather Condition")
    ax.set_ylabel("Bike Rentals (cnt)")
    st.pyplot(fig)
    
    # Total Bike Rentals by Hour
    st.subheader("Total Bike Rentals by Hour of the Day (Hourly Dataset)")
    grouped_hourly = df_hour.groupby('hr')['cnt'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='hr', y='cnt', data=grouped_hourly, marker='o', ax=ax)
    ax.set_title("Total Bike Rentals by Hour of the Day")
    ax.set_xlabel("Hour of the Day")
    ax.set_ylabel("Total Bike Rentals (cnt)")
    ax.set_xticks(range(0, 24))
    ax.grid(True)
    st.pyplot(fig)
    
    # Correlation Heatmap - Day Dataset
    st.subheader("Correlation Heatmap for Day Dataset")
    correlation_day = df_day.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_day, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
    ax.set_title("Correlation Heatmap for Day Dataset")
    st.pyplot(fig)
    
    # Correlation Heatmap - Hour Dataset
    st.subheader("Correlation Heatmap for Hour Dataset")
    correlation_hour = df_hour.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_hour, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
    ax.set_title("Correlation Heatmap for Hour Dataset")
    st.pyplot(fig)
    
else:
    st.warning("Please upload both day.csv and hour.csv to proceed.")
