import pandas as pd
import matplotlib.pyplot as plt

# Download and load the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = pd.read_csv(url, names=names)

# Basic Data Exploration
print(df.head())  # Display the first 5 rows of the DataFrame
print(df.shape)   # Display the shape of the DataFrame (rows, columns)
print(df.columns) # Display the column names
print(df.dtypes)  # Display the data types of each column
print(df.describe())  # Display summary statistics

# Data Analysis - Group by 'class' and calculate mean of other columns
grouped = df.groupby('class')
print(grouped.mean())

# Filter rows based on condition - Filter rows where 'sepal-length' is greater than 5.0
filtered = df[df['sepal-length'] > 5.0]
print(filtered)

# Create a Histogram for 'sepal-length'
plt.hist(df['sepal-length'], bins=10)
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# Save the filtered DataFrame to a CSV file
filtered.to_csv('filtered_iris.csv', index=False)
