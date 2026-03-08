import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_csv("jobs_cleaned.csv")

# Connect to SQLite database
conn = sqlite3.connect("jobs_database.db")

# Load data into database table
df.to_sql("jobs", conn, if_exists="replace", index=False)

# Close connection
conn.close()

print("Data successfully loaded into SQLite database")