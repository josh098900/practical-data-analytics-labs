import pandas as pd
import matplotlib.pyplot as plt
#seahorn is plotting library
from requests import head
import seaborn as sns

# load csv
# file_path = 'week02/dataset/FakeNewsNet.csv'  # change to your csv path
file_path = 'week02/dataset/creditcard.csv'  # change to your csv path
target_col = 'Class'  # change to your target column name
df = pd.read_csv(file_path)

#how to print first 5 rows of df2

# class counts
print("Class counts:")
#this is same as i saw in activity 1, but without normalize=true, so we get raw counts
print(df[target_col].value_counts())

# define colors (one for each class)
unique_classes = df[target_col].unique()
        
colors = sns.color_palette("hsv", len(unique_classes))

# plot distribution
plt.figure(figsize=(6,4))
#countplot does the counting, and draws a bar per class in one go, palette gives each bar its own colour
sns.countplot(data=df, x=target_col, palette=colors)
plt.title(f'Class Distribution of {target_col}')
plt.xlabel('Class')
plt.ylabel('Count')
plt.yscale('log')  # use logarithmic scale for better visibility, A log scale spaces the axis in powers of ten (1, 10, 100, 1,000, …)
#opens chart in a window
plt.show()

# head -1 week02/dataset/creditcard.csv