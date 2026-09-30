import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load csv
file_path = 'week02/dataset/FakeNewsNet.csv'  # change to your csv path
df = pd.read_csv(file_path)

# class counts
print("Class counts:")
print(df['real'].value_counts())

# define colors (one for each class)
unique_classes = df['real'].unique()
colors = sns.color_palette("hsv", len(unique_classes))

# plot distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='real', palette=colors)
plt.title('Class Distribution of real')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()