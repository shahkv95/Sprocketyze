from datetime import datetime, timedelta
import os
from typing import List
import pandas as pd
import random
import re
import numpy as np

# Function to check accuracy of data


def check_email_accuracy(data: pd.DataFrame) -> pd.DataFrame:
    print("\n******************** Accuracy dimension ********************\n")
    print("Checking accuracy of email\n")
    email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    data['email_accurate'] = data['email'].apply(
        lambda x: bool(re.match(email_regex, x)))
    return data

# Function to check completeness of data


def check_completeness(data: pd.DataFrame) -> None:
    print("\n******************** Completeness dimension ********************\n")

    print("Checking missing value percentage in the dataframe\n")
    # Check for missing values in the dataframe
    print("\nDataframe shape: ", data.shape)
    print("\n", data)
    missing_values = data.isnull().sum().sum()
    total_count = data.shape[0] * data.shape[1]
    completeness = (1 - (missing_values / total_count)) * 100
    print(f"\nCompleteness percentage {round(completeness, 2)}%\n")


# Function to check consistency of data
def check_consistency(data: pd.DataFrame) -> None:
    print("\n******************** Consistency dimension ********************\n")
    print("Checking if values is age column are consistent...\n")
    age_values = data['age']
    if all(isinstance(i, int) for i in age_values):
        if all(0 <= i <= 100 for i in age_values):
            print("Age column is consistent")
        else:
            print(
                "Age column is not consistent. Some values are not within the range of 0-100.")
    else:
        print("Age column is not consistent. Some values are not integers.")


# Function to check currency of data
def check_currency(data: pd.DataFrame, file_path: str) -> None:
    print("\n******************** Currency dimension ********************\n")

    modification_time = os.path.getmtime(file_path)

    # Convert the modification time to a datetime object
    date_modified: datetime = datetime.fromtimestamp(modification_time)

    # Calculate the time difference between now and the date modified
    time_diff: timedelta = datetime.now() - date_modified
    print("Time difference is: " + str(time_diff))

    # Check if the data is less than 24 hours old
    if time_diff < timedelta(hours=24):
        print("\nData is up-to-date as data is moodified in less than 24 hours old")
    else:
        print("\nData is not up-to-date as data is moodified in more than 24 hours old")

# Function to check relevancy of data


def check_relevancy(data: pd.DataFrame, date_column: str, date_range: List[str]) -> None:
    print("\n******************** Relevancy dimension ********************\n")

    # Convert date_column to datetime
    data[date_column] = pd.to_datetime(data[date_column])

    # Convert date_range strings to datetime
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

    # Filter data based on date_range
    data = data[(data[date_column] >= start_date) &
                (data[date_column] <= end_date)]
    print("Data that satisfy date_range: ", date_range)
    print("\n", data)


# Function to check uniqueness of data
def check_uniqueness(data: pd.DataFrame) -> None:
    print("\n******************** Uniqueness dimension ********************\n")

    # Check for duplicate rows in the dataframe
    if data.duplicated().any():
        # Check for duplicate rows
        duplicate_rows = data[data.duplicated()]

        # Print duplicate rows
        print("Following are the duplicate rows in the data:\n\n", duplicate_rows)
        raise ValueError("Data contains duplicate rows")
    else:
        print("All rows in the dataframe are unique")


# Function to check validity of data
def check_validity(data: pd.DataFrame) -> None:
    print("\n******************** Validity dimension ********************\n")
    print("Checking if age column has valid values...\n")
    age_values = data["age"]
    if all(isinstance(i, int) and i > 0 for i in age_values):
        print("Age column is valid.\n")
    else:
        print("Age column is not valid. Some values are not positive integers.\n")


def main():
    # Create a sample dataframe
    customer_data = pd.DataFrame({
        'age': [35, 27, 47, 31, 5.5, random.randint(18, 60), random.randint(18, 60)],
        'date_column': [pd.to_datetime('01-01-2023')-pd.DateOffset(days=x) for x in range(7)],
        'email': ['raj@desai.com', 'sheema@desai.com', 'kush@shahcom', 'marshal@desai.com', 'rohan@rotara.com', 'sohan@pathan.com', 'mohan@singh.com']
    })

    # Get the current script's directory
    script_dir: str = os.path.dirname(os.path.abspath(__file__))

    # Create the file name
    file_name: str = 'customer_data.csv'
    file_path: str = os.path.join(script_dir, file_name)

    # Save the DataFrame to a CSV file
    customer_data.to_csv(file_path, index=False)

    # Define date range
    date_range = ["2023-01-01", "2023-12-31"]

    # Check accuracy of data
    print(check_email_accuracy(customer_data))

    # Check completeness of data
    check_completeness(customer_data)

    # Check consistency of data
    check_consistency(customer_data)

    # Check currency of data
    check_currency(customer_data, file_name)

    # Check relevancy of data
    check_relevancy(customer_data, "date_column", date_range)

    # Check uniqueness of data
    check_uniqueness(customer_data)

    # Check validity of data
    check_validity(customer_data)


if __name__ == "__main__":
    main()
