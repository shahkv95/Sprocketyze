import pandas as pd

# Create a sample dataframe
employee_data = pd.DataFrame({
    'employee_id': [1, 2, 2, 5, 5],
    'name': ['John Doe', 'Jane Smith', 'Jane Smith', 'Emily Williams', 'Emily Williams']
})

# Save the dataframe to a CSV file
employee_data.to_csv('unique_customer_data.csv', index=False)

# Load data from CSV file
data = pd.read_csv("unique_customer_data.csv")

# Check for duplicate rows
duplicate_rows = data[data.duplicated()]

# Print duplicate rows
print("Following are the duplicate rows in the data:\n\n", duplicate_rows)
