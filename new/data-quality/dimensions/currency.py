import os
from datetime import datetime, timedelta


def check_data_currency(file_path: str) -> None:
    # Get the modification time of the file
    modification_time = os.path.getmtime(file_path)

    # Convert the modification time to a datetime object
    date_modified: datetime = datetime.fromtimestamp(modification_time)

    # Calculate the time difference between now and the date modified
    time_diff: timedelta = datetime.now() - date_modified
    print("Time difference is: " + str(time_diff))

    # Check if the data is less than 24 hours old
    if time_diff < timedelta(hours=24):
        print("Data is up-to-date as data is less than 24 hours old")
    else:
        print("Data is not up-to-date as data is more than 24 hours old")


# Define the file path
file_path: str = "complete_customer_data.csv"

# Check the data currency
check_data_currency(file_path)
