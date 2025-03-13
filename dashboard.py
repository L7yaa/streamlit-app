import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

st.title("Bike Rental Dashboard")
st.header("Exploring Bike Rentals based on Weather and Time")

# File upload section
st.subheader("Upload Data Files")
uploaded_day = st.file_uploader("Upload day.csv", type=["csv"])
uploaded_hour = st.file_uploader("Upload hour.csv", type=["csv"])

if uploaded_day and uploaded_hour:
    try:
        df_day = pd.read_csv(uploaded_day)
        df_hour = pd.read_csv(uploaded_hour)
        
        st.subheader("Day Dataset Preview")
        st.dataframe(df_day.head())
        
        st.subheader("Hour Dataset Preview")
        st.dataframe(df_hour.head())
        
        # Ensure required columns exist
        required_columns = {'weathersit', 'cnt', 'hr', 'weekday'}
        if not required_columns.issubset(df_day.columns) or not required_columns.issubset(df_hour.columns):
            st.error("Missing required columns in the uploaded files.")
        else:
            # Visualizations
            st.subheader("Bike Rentals by Weather Condition (Day Dataset)")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.boxplot(x='weathersit', y='cnt', data=df_day, ax=ax)
            ax.set_title("Bike Rentals by Weather Condition (Day Dataset)")
            st.pyplot(fig)
            
            # Correlation Heatmap
            st.subheader("Correlation Heatmap for Day Dataset")
            correlation_day = df_day.corr(numeric_only=True)
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(correlation_day, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
            ax.set_title("Correlation Heatmap for Day Dataset")
            st.pyplot(fig)
            
            # Weather condition descriptions
            weather_descriptions = {
                1: "Cerah",
                2: "Cerah Berawan",
                3: "Mendung",
                4: "Hujan"
            }
            
            st.subheader("Weather Condition Descriptions")
            for key, desc in weather_descriptions.items():
                st.write(f"**Condition {key}:** {desc}")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.warning("Please upload both day.csv and hour.csv to proceed.")
