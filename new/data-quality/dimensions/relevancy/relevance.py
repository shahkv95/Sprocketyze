from datetime import datetime, timedelta
import pandas as pd

# Create a sample dataframe
customer_data = pd.DataFrame({
    'first_name': ['John', 'Jane', 'Mike', 'Emily', 'David'],
    'last_name': ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown'],
    'age': [35, 27, 47, 31, 55],
    'date_column': [datetime.now()-timedelta(days=x) for x in range(5)]
})

# Save the dataframe to a CSV file
customer_data.to_csv('relevant_customer_data.csv', index=False)


def check_data_relevance(data: pd.DataFrame, date_column: str, date_range: list) -> pd.DataFrame:
    # Convert date_column to datetime
    data[date_column] = pd.to_datetime(data[date_column])

    # Convert date_range strings to datetime
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

    # Filter data based on date_range
    data = data[(data[date_column] >= start_date) &
                (data[date_column] <= end_date)]

    # Return filtered data
    return data


# Load data from CSV file
data = pd.read_csv("relevant_customer_data.csv")

# Define date range
date_range = ["2023-01-01", "2023-12-31"]

# Check data relevance
relevant_data = check_data_relevance(data, "date_column", date_range)

# Print relevant data
print(relevant_data)
