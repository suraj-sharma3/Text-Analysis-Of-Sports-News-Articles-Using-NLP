import pandas as pd

# List of CSV file paths to merge
csv_files = ['..\\scraped_articles_files\\scraped_articles_csv_files\\ESPN_Cricket_articles_1.csv', 
             '..\\scraped_articles_files\\scraped_articles_csv_files\\ESPN_Cricket_articles_2.csv']

# Initialize an empty list to store DataFrames
dfs = []

# Loop through the CSV files and read them into DataFrames
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    dfs.append(df)

# Concatenate the DataFrames into one DataFrame
merged_df = pd.concat(dfs, ignore_index=False)  # Set ignore_index=True to reset the index

# Save the merged DataFrame to a new CSV file (optional)
merged_df.to_csv('..\\scraped_articles_files\\scraped_articles_csv_files\\merged.csv', index=True)  # Set index=False to exclude the index column

# Print a summary of the merged DataFrame
print("Merged DataFrame:")
print(merged_df.head())


