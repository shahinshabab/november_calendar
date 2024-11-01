import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os

# Constants
YEAR = 2024
MONTH = 11
DAYS_IN_MONTH = 30
CSV_FILE = "completion_status.csv"

# Initialize CSV file if it doesn't exist
if not os.path.exists(CSV_FILE):
    dates = [datetime(YEAR, MONTH, day).strftime('%Y-%m-%d') for day in range(1, DAYS_IN_MONTH + 1)]
    df = pd.DataFrame({'date': dates, 'completed': [False] * DAYS_IN_MONTH})
    df.to_csv(CSV_FILE, index=False)
else:
    df = pd.read_csv(CSV_FILE)
    df['completed'] = df['completed'].astype(bool)

# Title
st.title("November 2024 Daily Completion Tracker")

# Instructions
st.write("Mark each day as completed and the status will be saved.")

# Display each day and checkbox
for index, row in df.iterrows():
    day_label = f"Day {index + 1} - {row['date']}"
    is_completed = st.checkbox(day_label, value=row['completed'], key=row['date'])

    # Update dataframe if checkbox status changes
    if is_completed != row['completed']:
        df.at[index, 'completed'] = is_completed
        df.to_csv(CSV_FILE, index=False)  # Save the updated status to CSV

# Final message
st.write("Your progress will be saved until the end of November.")
