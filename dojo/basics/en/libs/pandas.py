import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Download the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv(url, names=names)

# Basic Data Exploration
print(df.head(), df.describe(), df.info(), df.isnull().sum())

# Indexing, selecting and computational tools
print(df['class'], df.loc[:10, 'sepal_width'], df.corr(), df['class'].str.upper())

# Groupby, filtering and visualization
grouped = df.groupby('class').mean()
print(grouped)
filtered = df[df['sepal_length'] > 5.0]
print(filtered)
sns.scatterplot(x="sepal_length", y="sepal_width", hue="class", data=df)
plt.show()

# Saving and loading a DataFrame
filtered.to_csv('filtered_iris.csv', index=False)
df_loaded = pd.read_csv('filtered_iris.csv')
print(df_loaded.head())

# Changing pandas options
pd.set_option('display.max_rows', 10)
print(df)

# Enhancing performance and handling duplicates
df['class'] = df['class'].astype('category')
print(df.info())
print(df[df.duplicated()])

# Scaling to large datasets, working with categorical data and dates
df_sample = df.sample(frac=0.1)
print(df_sample.head())
df['class'] = df['class'].astype('category')
dates = pd.date_range(start='1/1/2022', periods=len(df))
df['date'] = dates
print(df.head())

# Advanced topics
df['interval'] = pd.cut(df['sepal_length'], 5)
print(df.head())

# Download other datasets
datasets = {
    'titanic.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv',
    'iris.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/iris.csv',
}

for filename, url in datasets.items():
    df = pd.read_csv(url)
    print(f"\n{filename} dataset head:\n", df.head())

# Reshaping, sorting, and creating pandas objects
df = pd.DataFrame(np.random.rand(5, 5), columns=['A', 'B', 'C', 'D', 'E'])
df_melt = pd.melt(df, id_vars=['A'], value_vars=['B', 'C', 'D', 'E'])
print("\nMelted DataFrame:\n", df_melt)
df_sorted = df.sort_values(by='A')
print("\nSorted DataFrame:\n", df_sorted.head())
s = pd.Series([1, 2, 3, 4, 5])
print("\nSeries:\n", s)
