import pandas as pd

# Path to your original CSV file
csv_file_path = 'train.csv'

# Path to the file where deleted rows will be saved
deleted_file_path = 'deleted_rows.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Check if the index 10500 is within the range of the DataFrame
if len(df) > 10000:
    # Separate the DataFrame into two parts: remaining rows and deleted rows
    deleted_df = df.iloc[:10000]
    remaining_df = df.iloc[10000:].reset_index(drop=True)

    # Write the remaining DataFrame back to the original CSV file
    remaining_df.to_csv(csv_file_path, index=False)
    print(f"Updated CSV file saved to {csv_file_path}")

    # Write the deleted DataFrame to a new CSV file
    deleted_df.to_csv(deleted_file_path, index=False)
    print(f"Deleted rows saved to {deleted_file_path}")
else:
    print(f"The DataFrame has fewer than 10500 rows. No rows were deleted.")