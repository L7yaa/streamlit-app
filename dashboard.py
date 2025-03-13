import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


# Load the datasets
df_day = pd.read_csv('/mnt/data/day.csv')
df_hour = pd.read_csv('/mnt/data/hour.csv')

# Set up the page title and header
st.title("Bike Rental Dashboard")
st.header("Exploring Bike Rentals based on Weather and Time")

# Show the dataframes to the user
st.subheader("Day Dataset Preview")
st.dataframe(df_day.head())

st.subheader("Hour Dataset Preview")
st.dataframe(df_hour.head())

# Visualizations Section

# Boxplot for Bike Rentals by Weather Condition (Day Dataset)
st.subheader("Bike Rentals by Weather Condition (Day Dataset)")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=df_day, ax=ax)
ax.set_title("Bike Rentals by Weather Condition (Day Dataset)")
ax.set_xlabel("Weather Condition")
ax.set_ylabel("Bike Rentals (cnt)")
st.pyplot(fig)

# Boxplot for Bike Rentals by Weather Condition (Hour Dataset)
st.subheader("Bike Rentals by Weather Condition (Hour Dataset)")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=df_hour, ax=ax)
ax.set_title("Bike Rentals by Weather Condition (Hour Dataset)")
ax.set_xlabel("Weather Condition")
ax.set_ylabel("Bike Rentals (cnt)")
st.pyplot(fig)

# Lineplot for Total Bike Rentals by Hour of the Day
st.subheader("Total Bike Rentals by Hour of the Day (Hourly Dataset)")
grouped_hourly = df_hour.groupby('hr')['cnt'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=grouped_hourly, marker='o', ax=ax)
ax.set_title("Total Bike Rentals by Hour of the Day (Hourly Dataset)")
ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Total Bike Rentals (cnt)")
ax.set_xticks(range(0, 24))  # Show all 24 hours
ax.grid(True)
st.pyplot(fig)

# Barplot for Total Bike Rentals by Day of the Week
st.subheader("Total Bike Rentals by Day of the Week (Hourly Dataset)")
grouped_weekday = df_hour.groupby('weekday')['cnt'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='weekday', y='cnt', data=grouped_weekday, ax=ax)
ax.set_title("Total Bike Rentals by Day of the Week (Hourly Dataset)")
ax.set_xlabel("Day of the Week")
ax.set_ylabel("Total Bike Rentals (cnt)")
ax.set_xticklabels(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
st.pyplot(fig)

# Histogram for Bike Rentals Distribution (Day Dataset)
st.subheader("Distribution of Bike Rentals (cnt) - Day Dataset")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(df_day['cnt'], bins=30, kde=True, color='blue', ax=ax)
ax.set_title("Distribution of Bike Rentals (cnt) - Day Dataset")
ax.set_xlabel("Bike Rentals (cnt)")
ax.set_ylabel("Frequency")
ax.grid(True)
st.pyplot(fig)

# Histogram for Bike Rentals Distribution (Hour Dataset)
st.subheader("Distribution of Bike Rentals (cnt) - Hour Dataset")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(df_hour['cnt'], bins=30, kde=True, color='green', ax=ax)
ax.set_title("Distribution of Bike Rentals (cnt) - Hour Dataset")
ax.set_xlabel("Bike Rentals (cnt)")
ax.set_ylabel("Frequency")
ax.grid(True)
st.pyplot(fig)

# Heatmap for Correlation - Day Dataset
st.subheader("Correlation Heatmap for Day Dataset")
correlation_day = df_day.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_day, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
ax.set_title("Correlation Heatmap for Day Dataset")
st.pyplot(fig)

# Heatmap for Correlation - Hour Dataset
st.subheader("Correlation Heatmap for Hour Dataset")
correlation_hour = df_hour.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_hour, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
ax.set_title("Correlation Heatmap for Hour Dataset")
st.pyplot(fig)

# Bike Rentals by Weather Condition (Grouped)
st.subheader("Total Bike Rentals by Weather Condition (weathersit) - Day Dataset")
grouped_weather = df_day.groupby('weathersit')['cnt'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=grouped_weather, palette="Blues_d", ax=ax)
ax.set_title("Total Bike Rentals by Weather Condition (weathersit) - Day Dataset")
ax.set_xlabel("Weather Condition")
ax.set_ylabel("Total Bike Rentals (cnt)")
st.pyplot(fig)

# Casual vs Registered Bike Rentals by Hour of the Day
st.subheader("Total Casual vs Registered Bike Rentals by Hour of the Day (Hourly Dataset)")
df_hour['casual_registered'] = df_hour['casual'] + df_hour['registered']
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='casual_registered', data=df_hour, marker='o', color='brown', ax=ax)
ax.set_title("Total Casual vs Registered Bike Rentals by Hour of the Day (Hourly Dataset)")
ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Total Bike Rentals (Casual + Registered)")
ax.set_xticks(range(0, 24))  # Show all 24 hours
ax.grid(True)
st.pyplot(fig)