from typing import List
import os
from typing import List, Dict
import pandas as pd

# Create a list of customer data
customer_data: List[Dict[str, str]] = [
    {"name": "Kush", "email": "k@example.com", "phone": "1234123412",
     },
    {"name": "Shah", "email": "s@example.com", "phone": "2345234567",
     },
    {"name": "Missing", "email": "", "phone": "",
     },
]

# Convert the list of customer data to a DataFrame
data: pd.DataFrame = pd.DataFrame(customer_data)

# Get the current script's directory
script_dir: str = os.path.dirname(os.path.abspath(__file__))

# Create the file name
file_name: str = 'complete_customer_data.csv'
file_path: str = os.path.join(script_dir, file_name)

# Save the DataFrame to a CSV file
data.to_csv(file_path, index=False)


# Load the data from a CSV file
data: pd.DataFrame = pd.read_csv("complete_customer_data.csv")

# Define a list of required columns
required_columns: List[str] = [
    "name", "email", "phone"]

# Create a new dataframe with a subset of columns
new_data: pd.DataFrame = data[required_columns].copy()

# remove column from the new dataframe
new_data = new_data.drop("phone", axis=1)

# Define a function to check for completeness of data


def check_column_completeness(data: pd.DataFrame, required_columns: List[str]) -> None:
    missing_columns: set = set(required_columns) - set(data.columns)
    if missing_columns:
        for column in missing_columns:
            if column not in data.columns:
                print(
                    f"The following column is missing from the data: {column}")
    else:
        print("All required columns are present in the data.")


# Apply the column completeness check to the data
check_column_completeness(new_data, required_columns)

# Define a function to check for completeness of data in each row


def check_row_completeness(data: pd.DataFrame, required_columns: List[str]) -> None:
    missing_data = data[required_columns].isnull().any(axis=1)
    if missing_data.any():
        print(
            f"The following rows are missing data: {missing_data.index[missing_data]}")
    else:
        print("All rows have complete data.")


# Apply the row completeness check to the data
check_row_completeness(data, required_columns)
