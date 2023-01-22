import pandas as pd
import os
from typing import List, Dict
import re

# Create a list of customer data
customer_data: List[Dict[str, str]] = [
    {"name": "Kush Shah", "email": "kushshah@example.com"},
    {"name": "Shah Kush", "email": "shahkush@example.com"},
    {"name": "K Shah", "email": "kshah@examplecom"},
]

# Convert the list of customer data to a DataFrame
data: pd.DataFrame = pd.DataFrame(customer_data)

# Get the current script's directory
script_dir: str = os.path.dirname(os.path.abspath(__file__))

# Create the file name
file_name: str = 'accurate_customer_data.csv'
file_path: str = os.path.join(script_dir, file_name)

# Save the DataFrame to a CSV file
data.to_csv(file_path, index=False)

# Load the data from a CSV file
data = pd.read_csv(file_path)


def check_email_accuracy(data: pd.DataFrame) -> pd.DataFrame:
    email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    data['email_accurate'] = data['email'].apply(
        lambda x: bool(re.match(email_regex, x)))
    return data


# Apply the email accuracy check to the data
data = check_email_accuracy(data)

# Print the data with the new email_accurate column
print(data)
