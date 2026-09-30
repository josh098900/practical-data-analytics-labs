import pandas as pd

# load csv
file_path = 'Dataset\FakeNewsNet.csv'  # change to your csv path
df = pd.read_csv(file_path)

# total rows
total_rows = len(df)

# missing values
missing_count = df.isnull().sum()
missing_percent = (missing_count / total_rows) * 100

# combine in one table
missing_stats = pd.DataFrame({
    'Missing Count': missing_count,
    'Missing Percent': missing_percent
}).sort_values(by='Missing Count', ascending=False)

print("Missing values statistics for all columns:")
print(missing_stats)