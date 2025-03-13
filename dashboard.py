import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Judul aplikasi
st.title("Bike Rental Dashboard")
st.header("Exploring Bike Rentals based on Weather and Time")

# Upload file CSV
st.subheader("Upload Data Files")
uploaded_day = st.file_uploader("Upload day.csv", type=["csv"])
uploaded_hour = st.file_uploader("Upload hour.csv", type=["csv"])

if uploaded_day is not None and uploaded_hour is not None:
    try:
        # Membaca dataset
        df_day = pd.read_csv(uploaded_day)
        df_hour = pd.read_csv(uploaded_hour)

        # Pastikan dataset tidak kosong
        if df_day.empty or df_hour.empty:
            st.error("One or both uploaded files are empty. Please upload valid datasets.")
        else:
            # Pastikan dataset memiliki kolom yang diperlukan
            required_columns_day = {'weathersit', 'cnt'}
            required_columns_hour = {'weathersit', 'cnt', 'hr'}

            if not required_columns_day.issubset(df_day.columns):
                st.error("Uploaded day.csv is missing required columns!")
            elif not required_columns_hour.issubset(df_hour.columns):
                st.error("Uploaded hour.csv is missing required columns!")
            else:
                # Menampilkan preview dataset
                st.subheader("Day Dataset Preview")
                st.dataframe(df_day.head())

                st.subheader("Hour Dataset Preview")
                st.dataframe(df_hour.head())

                # Visualisasi 1: Boxplot Bike Rentals by Weather Condition (Day Dataset)
                st.subheader("Bike Rentals by Weather Condition (Day Dataset)")
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.boxplot(x='weathersit', y='cnt', data=df_day, ax=ax)
                ax.set_title("Bike Rentals by Weather Condition (Day Dataset)")
                ax.set_xlabel("Weather Condition")
                ax.set_ylabel("Bike Rentals (cnt)")
                st.pyplot(fig)

                # Visualisasi 2: Boxplot Bike Rentals by Weather Condition (Hour Dataset)
                st.subheader("Bike Rentals by Weather Condition (Hour Dataset)")
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.boxplot(x='weathersit', y='cnt', data=df_hour, ax=ax)
                ax.set_title("Bike Rentals by Weather Condition (Hour Dataset)")
                ax.set_xlabel("Weather Condition")
                ax.set_ylabel("Bike Rentals (cnt)")
                st.pyplot(fig)

                # Visualisasi 3: Lineplot Total Bike Rentals by Hour
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

                # Visualisasi 4: Correlation Heatmap - Day Dataset
                st.subheader("Correlation Heatmap for Day Dataset")
                correlation_day = df_day.select_dtypes(include=['float64', 'int64']).corr()
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.heatmap(correlation_day, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
                ax.set_title("Correlation Heatmap for Day Dataset")
                st.pyplot(fig)

                # Visualisasi 5: Correlation Heatmap - Hour Dataset
                st.subheader("Correlation Heatmap for Hour Dataset")
                correlation_hour = df_hour.select_dtypes(include=['float64', 'int64']).corr()
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.heatmap(correlation_hour, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
                ax.set_title("Correlation Heatmap for Hour Dataset")
                st.pyplot(fig)

    except Exception as e:
        st.error(f"An error occurred while processing the files: {e}")

else:
    st.warning("Please upload both day.csv and hour.csv to proceed.")
