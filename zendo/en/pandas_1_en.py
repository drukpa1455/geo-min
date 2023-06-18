import pandas as pd
import matplotlib.pyplot as plt

# Download and load the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = pd.read_csv(url, names=names)

# Basic Data Exploration
print(df.head())  # Glimpse initial rows
print(df.shape)   # Reveal DataFrame's shape
print(df.columns) # Unveil column names
print(df.dtypes)  # Expose column data types
print(df.describe())  # Provide summary statistics

# Data Analysis - Group by 'class' and calculate mean of other columns
grouped = df.groupby('class')
print(grouped.mean())  # Compute means within each group

# Filter rows based on condition - Filter rows where 'sepal-length' is greater than 5.0
filtered = df[df['sepal-length'] > 5.0]
print(filtered)  # Display filtered rows

# Create a Histogram for 'sepal-length'
plt.hist(df['sepal-length'], bins=10)
plt.title('Histogram of Sepal Length')  # Assign plot title
plt.xlabel('Sepal Length')  # Label X-axis
plt.ylabel('Frequency')  # Label Y-axis
plt.show()  # Present the histogram

# Save the filtered DataFrame to a CSV file
filtered.to_csv('filtered_iris.csv', index=False)  # Save filtered DataFrame to CSV
