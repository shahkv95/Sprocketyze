import re
import pandas as pd
from faker import Faker

# Create an instance of the Faker library
fake = Faker(locale="hi_IN")

# Create an empty dataframe to store the data
data = pd.DataFrame(columns=['email', 'phone'])

# Generate 100 rows of sample data
for _ in range(5):
    email = fake.email()
    phone = fake.phone_number()
    data = data.append({'email': email, 'phone': phone}, ignore_index=True)

# Save the data to a CSV file
data.to_csv('consistent_customer_data.csv', index=False)

print("Sample data generated and saved to consistent_customer_data.csv file.")

# Load the data from a CSV file
data = pd.read_csv("consistent_customer_data.csv")


def check_phone_format(data: pd.DataFrame, format: str) -> pd.DataFrame:
    """
    Check if the phone number column in the dataframe matches the given format

    Args:
        data : pd.DataFrame
        format : str : regular expression format for the phone number

    Return:
        pd.DataFrame : with new column "phone_format_valid" indicating if the phone number is in the correct format
    """
    data["phone_format_valid"] = data["phone"].apply(
        lambda x: bool(re.match(format, x)))
    return data


data = check_phone_format(data, '^\d{11}$')

# Print the data with the new name_consistent and city_consistent columns
print(data)
