import pandas as pd

# load csv
file_path = 'week02/dataset/FakeNewsNet.csv'  # change to your csv path
df = pd.read_csv(file_path)

# total rows
total_rows = len(df)
print(f"Total rows in the dataset: {total_rows}")

# missing values
#df.isnull builds grid the shame shape as data, with true wherever a cell is blank and false for rest
# sum adds up each column, true is 1 and false is 0, so we get a count of missing values for each column 
missing_count = df.isnull().sum()
#this turns the count into percentages, a percentage is more useful than a raw count, 330 blanks is nothing in 1 mullion rows but lot in 500
missing_percent = (missing_count / total_rows) * 100


# combine in one table
#glues the count and percentages into new table, with worst columns at top
missing_stats = pd.DataFrame({
    'Missing Count': missing_count,
    'Missing Percent': missing_percent
}).sort_values(by='Missing Count', ascending=False)

print("Missing values statistics for all columns:")
print(missing_stats)

#testing if the missingingness is random
#df[df['source_domain'].isnull()] makes a true/false value for each row, putting that inside df[] keeps only the rows where its true,
#so missing rows is a smaller df containing only the rows where source_domain is missing
missing_rows = df[df['source_domain'].isnull()]

print("\nclass mix in all rows:")
#.value_counts() counts how many times each value appears in a column, adding normluae=true gives us proportions instead of counts, 0.75 instead of 17441
print(df['real'].value_counts(normalize=True))

print("\nclass mix in rows missing source domain:")
print(missing_rows['real'].value_counts(normalize=True))
