import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import pytz

api_ninjas_key = 'wfa5PMczHQs8clQwZgqAuA==cogw7CbGIC3dxquk'  # Replace with your API key from API Ninjas

def load_csv(file):
    return pd.read_csv(file)

def fetch_time_for_timezone(timezone):
    url = f"https://api.api-ninjas.com/v1/worldtime?timezone={timezone}"
    
    headers = {
        'X-Api-Key': api_ninjas_key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        time_data = response.json()

        time = time_data.get("datetime", None)
        if time:
            return time
        else:
            return None
    
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data from API Ninjas: {e}")
        return None

def split_datetime(datetime_str):
    if datetime_str is None:
        return None, None
    try:
        date, time = datetime_str.split(" ")
        return date, time
    except ValueError:
        return None, None

st.title('Timezone Time Fetcher using API')
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = load_csv(uploaded_file)
    st.write("CSV Data:")
    st.dataframe(df)
    command = st.text_input("Enter the text command with {timezone} placeholder")
    
    timezone_column = st.selectbox("Select the column for timezone", df.columns)
    
    if st.button("Fetch Time and Update CSV"):
        if command and timezone_column:
            df['Datetime'] = df[timezone_column].apply(lambda timezone: fetch_time_for_timezone(timezone))
            df[['Date', 'Time']] = df['Datetime'].apply(
                lambda datetime_str: pd.Series(split_datetime(datetime_str))
            )
            df.drop(columns=['Datetime'], inplace=True)
            st.write("Updated CSV Data:")
            st.dataframe(df)
            updated_csv = df.to_csv(index=False)
            st.download_button("Download Updated CSV", updated_csv, file_name="updated_timezones.csv")
        else:
            st.error("Please provide both the text command and select a timezone column.")
