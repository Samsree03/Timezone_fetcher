# City Time Fetcher Dashboard

## Project Description
The City Time Fetcher Dashboard is an interactive Streamlit-based application that allows users to:
1. Upload a CSV file containing timezones (e.g., `Europe/London`, `Asia/Singapore`).
2. Fetch the current date and time for each timezone using the API Ninjas World Time API.
3. Export the updated CSV file with separate columns for the date and time.

This tool is ideal for organizations working across multiple time zones and simplifies managing time-sensitive data.

---

## Setup Instructions

### Prerequisites
- Python 3.7 or higher installed on your system.
- Basic knowledge of Python and Streamlit.

### Installation Steps
1. Install streamlit, pandas, requests, datetime and pytz libraries using command prompt.
2. Create an account in Ninjas API and get the API Key.
3. Modify and run the python file, task_dashboard.py
   
## Usage Guide

### Running the Application
1. Start the Streamlit application
2. Open the application in your browser (usually at `http://localhost:8501`).

### Using the Dashboard
1. Upload a CSV File:
   - Ensure the CSV file contains a column named `Timezone` with entries like `Europe/London` or `Asia/Singapore`.
   
2. Enter the Command:
   - In the text input field, provide a custom command with the `{timezone}` placeholder, e.g., `"What is the time in {timezone}?"`.

3. Fetch Time:
   - The application fetches the time for each timezone and displays:
     - Date
     - Time
     
4. Download Updated CSV:
   - After processing, download the enriched CSV file with the updated columns.

---

## API Keys and Environment Variables

### API Key
- This application uses the API Ninjas World Time API.
- Obtain an API key by signing up at [API Ninjas](https://www.api-ninjas.com).
- Add your key to the python file.

  The link to the existing app is given below:
  https://timezonefetcher-yusfz2tcmnfcbnem7p2rcs.streamlit.app/
