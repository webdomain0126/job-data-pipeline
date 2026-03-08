import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("jobs_cleaned.csv")

# Count jobs by location
location_counts = df["location"].value_counts()

# Create bar chart
location_counts.plot(kind="bar")

plt.title("Job Count by Location")
plt.xlabel("Location")
plt.ylabel("Number of Jobs")

# Save chart
plt.savefig("job_location_chart.png")

print("Chart created and saved as job_location_chart.png")