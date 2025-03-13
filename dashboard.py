import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

sns.set(style='dark')

# Judul aplikasi
st.title("🚴‍♂️ Bike Rental Dashboard")
st.header("📊 Exploring Bike Rentals based on Weather and Time")

# Upload file CSV
st.subheader("Upload Data Files")
uploaded_day = st.file_uploader("Upload day.csv", type=["csv"])
uploaded_hour = st.file_uploader("Upload hour.csv", type=["csv"])

if uploaded_day is not None and uploaded_hour is not None:
    try:
        df_day = pd.read_csv(uploaded_day, on_bad_lines='skip')
        df_hour = pd.read_csv(uploaded_hour, on_bad_lines='skip')

        if df_day.empty or df_hour.empty:
            st.error("One or both uploaded files are empty. Please upload valid datasets.")
        else:
            required_columns_day = {'weathersit', 'cnt', 'temp', 'hum', 'windspeed', 'casual', 'registered', 'workingday'}
            required_columns_hour = {'weathersit', 'cnt', 'hr', 'weekday'}

            if not required_columns_day.issubset(df_day.columns):
                st.error("Uploaded day.csv is missing required columns!")
            elif not required_columns_hour.issubset(df_hour.columns):
                st.error("Uploaded hour.csv is missing required columns!")
            else:
                st.subheader("Day Dataset Preview")
                st.dataframe(df_day.head())
                
                st.subheader("Hour Dataset Preview")
                st.dataframe(df_hour.head())

                # Konversi tanggal jika tersedia
                if 'dteday' in df_day.columns:
                    df_day['dteday'] = pd.to_datetime(df_day['dteday'])

                # Keterangan Cuaca dalam Bentuk Gambar
                st.subheader("🌦️ Weather Condition Overview")
                weather_icons = {1: "☀️ Clear", 2: "⛅ Misty/Cloudy", 3: "🌧️ Light Rain/Snow", 4: "⛈️ Heavy Rain/Snow"}
                if 'weathersit' in df_day.columns:
                    df_day['weather_desc'] = df_day['weathersit'].map(weather_icons)
                    st.write(df_day[['weathersit', 'weather_desc']].drop_duplicates())

                # Visualisasi Tren Penggunaan Sepeda (harian)
                st.subheader("📅 Daily Bike Rental Trends")
                fig, ax = plt.subplots(figsize=(10, 6))
                if 'dteday' in df_day.columns:
                    sns.lineplot(x=df_day['dteday'], y=df_day['cnt'], marker='o', ax=ax)
                else:
                    sns.lineplot(x=df_day.index, y=df_day['cnt'], marker='o', ax=ax)
                ax.set_title("Daily Bike Rentals")
                ax.set_xlabel("Date")
                ax.set_ylabel("Total Rentals")
                fig.autofmt_xdate()
                st.pyplot(fig)

                # Visualisasi Tren Penggunaan Sepeda (per jam)
                st.subheader("🕒 Hourly Bike Rental Trends")
                grouped_hourly = df_hour.groupby('hr')['cnt'].sum().reset_index()
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.lineplot(x='hr', y='cnt', data=grouped_hourly, marker='o', ax=ax)
                ax.set_title("Total Bike Rentals by Hour of the Day")
                ax.set_xlabel("Hour of the Day")
                ax.set_ylabel("Total Bike Rentals")
                ax.set_xticks(range(0, 24))
                st.pyplot(fig)

                # Heatmap jumlah pengguna berdasarkan jam dan hari dalam seminggu
                st.subheader("🔥 Heatmap: Bike Rentals by Hour and Weekday")
                pivot_table = df_hour.pivot_table(values='cnt', index='weekday', columns='hr', aggfunc=np.sum)
                fig, ax = plt.subplots(figsize=(12, 6))
                sns.heatmap(pivot_table, cmap='coolwarm', linewidths=0.5, annot=True, fmt='.0f')
                ax.set_title("Bike Rentals Heatmap")
                st.pyplot(fig)

                # Scatter plot hubungan suhu terhadap jumlah pengguna
                st.subheader("🌡️ Temperature vs Bike Rentals")
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.scatterplot(x='temp', y='cnt', data=df_day, alpha=0.5, ax=ax)
                ax.set_title("Temperature vs Bike Rentals")
                ax.set_xlabel("Temperature")
                ax.set_ylabel("Bike Rentals")
                st.pyplot(fig)

                # Histogram distribusi pengguna dalam kondisi cuaca
                st.subheader("☁️ User Distribution by Weather Condition")
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.histplot(df_day['weathersit'], discrete=True, kde=True, ax=ax)
                ax.set_title("Weather Condition Distribution")
                ax.set_xlabel("Weather Condition")
                ax.set_ylabel("Count")
                st.pyplot(fig)

                # Pie chart proporsi casual vs registered
                st.subheader("👥 Casual vs Registered Users")
                user_counts = [df_day['casual'].sum(), df_day['registered'].sum()]
                fig, ax = plt.subplots(figsize=(6, 6))
                ax.pie(user_counts, labels=['Casual', 'Registered'], autopct='%1.1f%%', colors=sns.color_palette('pastel'))
                ax.set_title("Casual vs Registered Users")
                st.pyplot(fig)

                # Bar chart perbandingan pengguna per hari kerja vs akhir pekan
                st.subheader("📆 Bike Rentals: Workday vs Weekend")
                workday_counts = df_day.groupby('workingday')['cnt'].sum()
                fig, ax = plt.subplots(figsize=(6, 6))
                sns.barplot(x=workday_counts.index, y=workday_counts.values, ax=ax)
                ax.set_xticklabels(["Weekend", "Workday"])
                ax.set_title("Bike Rentals: Workday vs Weekend")
                ax.set_xlabel("Day Type")
                ax.set_ylabel("Total Rentals")
                st.pyplot(fig)

    except Exception as e:
        st.error(f"An error occurred while processing the files: {e}")
else:
    st.warning("Please upload both day.csv and hour.csv to proceed.")
