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

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the iris dataset
iris = sns.load_dataset('iris')

# Display the first five rows of the dataset
print("\nLoaded Iris dataset:")
print(iris.head())

# --------------- ESSENTIAL BASIC FUNCTIONALITY --------------- 
# 'describe' method provides basic statistics for each column in the dataset.
print("\nDescriptive statistics of Iris dataset:")
print(iris.describe())

# 'info' method prints information about a DataFrame including the index dtype and columns, non-null values, and memory usage.
print("\nInformation about Iris dataset:")
print(iris.info())

# --------------- INDEXING AND SELECTING DATA ---------------
# Selects a specific column from the iris dataset
print("\nSelect 'species' column from Iris dataset:")
print(iris['species'])

# Selects first 10 rows of a specific column using label-based indexing
print("\nFirst 10 rows of the 'petal_width' column:")
print(iris.loc[:10, 'petal_width'])

# --------------- COMPUTATIONAL TOOLS ---------------
# 'corr' method calculates the correlation matrix for the iris dataset
print("\nCorrelation matrix for Iris dataset:")
print(iris.corr())

# --------------- WORKING WITH TEXT DATA ---------------
# 'str.upper' method converts the species names to uppercase
print("\nSpecies column in uppercase:")
print(iris['species'].str.upper())

# --------------- WORKING WITH MISSING DATA ---------------
# 'isnull().sum()' method returns the count of missing values in each column
print("\nCount missing values in each column:")
print(iris.isnull().sum())

# --------------- GROUP BY ---------------
# 'groupby' method groups the data by species and calculates the mean for each group
print("\nMean of all numerical columns, grouped by species:")
print(iris.groupby('species').mean())

# --------------- VISUALIZATION ---------------
# Plotting a bar plot of average petal length for each species
print("\nBar plot of average petal length for each species:")
iris.groupby('species')['petal_length'].mean().plot(kind='bar')
plt.show()

# Plotting histograms for each feature in the dataset
iris.hist(edgecolor='black', linewidth=1.2)
plt.show()

# Plotting a scatter plot with color encoding by species
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris)
plt.show()

# --------------- OPTIONS AND SETTINGS ---------------
# 'set_option' changes the maximum displayed rows
pd.set_option('display.max_rows', 10)
print("\nNew max displayed rows setting:")
print(iris)

# --------------- ENHANCING PERFORMANCE ---------------
# Changing the data type of 'species' column to 'category', saving memory
iris['species'] = iris['species'].astype('category')
print("\nIris dataset with 'species' as category type:")
print(iris.info())

# --------------- SCALING TO LARGE DATASETS ---------------
# 'sample' method extracts a random sample (10%) from the dataframe
iris_sample = iris.sample(frac=0.1)
print("\nSampled Iris dataset:")
print(iris_sample.head())

# --------------- HANDLING DUPLICATE LABELS ---------------
# 'duplicated()' method prints duplicated rows in the iris dataset
print("\nDuplicate rows in Iris dataset:")
print(iris[iris.duplicated()])

# --------------- WORKING WITH CATEGORICAL DATA ---------------
# Changing 'species' to a categorical data type
iris['species'] = iris['species'].astype('category')
print("\nSpecies column as a category:")
print(iris['species'])

# --------------- WORKING WITH DATES AND TIME SERIES ---------------
# Create a simple date range (one for each row of the iris dataset)
dates = pd.date_range(start='1/1/2022', periods=len(iris))
iris['date'] = dates
print("\nIris dataset with date column:")
print(iris.head())

# --------------- ADVANCED TOPICS ---------------
# Creating an interval index
df = pd.DataFrame({'A': range(5)})
df.index = pd.IntervalIndex.from_breaks([0, 1, 2, 3, 4, 5])
print("\nDataFrame with Interval Index:")
print(df)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import StringIO

# Download the necessary datasets
datasets = {
    'titanic.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv',
    'iris.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/iris.csv',
    'melting_potatoes.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/melting_potatoes.csv',
    'boston_housing.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/boston_housing.csv',
    'wine_quality.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/wine_quality.csv',
    'nyc_weather.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/nyc_weather.csv',
    'stock_prices.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/stock_prices.csv',
    'sales.csv': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/sales.csv',
}

for filename, url in datasets.items():
    response = requests.get(url)
    with open(filename, 'w') as f:
        f.write(response.text)

# Example of reading a CSV file (using Titanic dataset)
df = pd.read_csv('titanic.csv')
print("\nRead CSV file:")
print(df.head())

# Example of writing a CSV file
df.to_csv('output.csv', index=False)
print("\nWrite CSV file: Successfully written.")

# Example of sorting DataFrame by column values (using Iris dataset)
df = pd.read_csv('iris.csv')
df_sorted = df.sort_values(by='sepal_length')
print("\nSorted DataFrame:")
print(df_sorted.head())

# Example of reshaping DataFrame using melt function (using Melting Potatoes dataset)
df = pd.read_csv('melting_potatoes.csv')
melted_df = pd.melt(df, id_vars=['id'], value_vars=['time_1', 'time_2'], var_name='time_type', value_name='time_value')
print("\nMelted DataFrame:")
print(melted_df.head())

# Example of creating a Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("\nSeries:")
print(s)

# Example of basic operations on a Series (using Boston Housing dataset)
df = pd.read_csv('boston_housing.csv')
s_sum = df['RM'].sum()
s_mean = df['RM'].mean()
print("\nSum:", s_sum)
print("Mean:", s_mean)

# Example of creating a DataFrame (using Wine Quality dataset)
data = pd.read_csv('wine_quality.csv')
df = data[['pH', 'alcohol', 'quality']]
print("\nDataFrame:")
print(df.head())

# Example of selecting data from a DataFrame
df_subset = df[['pH', 'quality']]
print("\nSubset of DataFrame:")
print(df_subset.head())

# Example of using pandas arrays and scalars
array = pd.array([1, 2, 3, 4, 5])
scalar = pd.Series(10)
print("\nPandas Array:")
print(array)
print("\nPandas Scalar:")
print(scalar)

# Example of creating an index object
index = pd.Index(['A', 'B', 'C', 'D'])
print("\nIndex Object:")
print(index)

# Example of using date offsets (using NYC Weather dataset)
df = pd.read_csv('nyc_weather.csv')
dates = pd.to_datetime(df['date'])
offset = pd.offsets.Day(1)
new_dates = dates + offset
print("\nNew Dates:")
print(new_dates.head())

# Example of using window functions (using Stock Price dataset)
df = pd.read_csv('stock_prices.csv')
s = df['price']
rolling_sum = s.rolling(window=2).sum()
print("\nWindow Functions:")
print(rolling_sum.head())

# Example of using groupby operation (using Sales dataset)
df = pd.read_csv('sales.csv')
grouped = df.groupby('region').sum()
print("\nGrouped Data:")
print(grouped.head())

# Example of resampling time series data (using Stock Price dataset)
df = pd.read_csv('stock_prices.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
resampled_df = df.resample('M').mean()
print("\nResampled Time Series:")
print(resampled_df.head())

# Example of applying styles to a DataFrame
styled_df = df.head().style.background_gradient(cmap='cool')
print("\nStyled DataFrame:")
print(styled_df)

# Example of plotting a DataFrame
df.plot(kind='line', x='date', y='price')
plt.title('Stock Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# Example of setting options
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)
print("\nOptions and Settings:")
print(df.head())

# Example of creating a custom function in pandas
def custom_function(df):
    # Custom function implementation
    return df

# Usage of the custom function
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = custom_function(df)
print(result)

