import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import pytz

# Set API key for API Ninjas
api_ninjas_key = 'wfa5PMczHQs8clQwZgqAuA==cogw7CbGIC3dxquk'  # Replace with your API key from API Ninjas

# Load CSV file
def load_csv(file):
    return pd.read_csv(file)

# Function to fetch time using API Ninjas World Time API
def fetch_time_for_timezone(timezone):
    # URL for API Ninjas World Time API
    url = f"https://api.api-ninjas.com/v1/worldtime?timezone={timezone}"
    
    headers = {
        'X-Api-Key': api_ninjas_key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        time_data = response.json()

        # Extract datetime from response
        time = time_data.get("datetime", None)
        if time:
            return time
        else:
            return None
    
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data from API Ninjas: {e}")
        return None

# Function to split datetime into separate date and time
def split_datetime(datetime_str):
    if datetime_str is None:
        return None, None
    try:
        date, time = datetime_str.split(" ")
        return date, time
    except ValueError:
        return None, None

# Streamlit app UI
st.title('Timezone Time Fetcher using API')

# File uploader for CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Load and display CSV data
    df = load_csv(uploaded_file)
    st.write("CSV Data:")
    st.dataframe(df)
    
    # Text input for the command
    command = st.text_input("Enter the text command with {timezone} placeholder")
    
    # Column selection for timezone
    timezone_column = st.selectbox("Select the column for timezone", df.columns)
    
    # Button to execute the process
    if st.button("Fetch Time and Update CSV"):
        if command and timezone_column:
            # Create a new column for Time
            df['Datetime'] = df[timezone_column].apply(lambda timezone: fetch_time_for_timezone(timezone))
            
            # Split Datetime into Date and Time
            df[['Date', 'Time']] = df['Datetime'].apply(
                lambda datetime_str: pd.Series(split_datetime(datetime_str))
            )
            
            # Drop the combined Datetime column (optional)
            df.drop(columns=['Datetime'], inplace=True)
            
            # Display updated DataFrame
            st.write("Updated CSV Data:")
            st.dataframe(df)
            
            # Provide option to download the updated CSV
            updated_csv = df.to_csv(index=False)
            st.download_button("Download Updated CSV", updated_csv, file_name="updated_timezones.csv")
        else:
            st.error("Please provide both the text command and select a timezone column.")
