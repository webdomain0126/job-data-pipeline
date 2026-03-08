import pandas as pd

data = {
    "Job_Title": ["Data Engineer", "Python Developer", "Data Analyst"],
    "Company": ["Google", "Amazon", "Microsoft"],
    "Location": ["USA", "Remote", "UK"]
}

df = pd.DataFrame(data)

df.to_csv("jobs_raw.csv", index=False)

print("Data extracted and saved to jobs_raw.csv")