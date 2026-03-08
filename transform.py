import pandas as pd

# Load the raw dataset
df = pd.read_csv("jobs_raw.csv")

# Clean column names
df.columns = df.columns.str.lower()

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv("jobs_cleaned.csv", index=False)

print("Data cleaned and saved to jobs_cleaned.csv")