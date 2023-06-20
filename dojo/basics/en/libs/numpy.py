# Required libraries are imported
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import seaborn as sns
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

# Loop through the dictionary to download each dataset and save as a .csv file
for filename, url in datasets.items():
    response = requests.get(url)
    with open(filename, 'w') as f:
        f.write(response.text)

# --------------- LOADING AND WRITING DATA ---------------
# Load the Titanic dataset as a DataFrame
df_titanic = pd.read_csv('titanic.csv')
print("\nRead CSV file:")
print(df_titanic.head())

# Save the DataFrame back to a CSV file
df_titanic.to_csv('output.csv', index=False)
print("\nWrite CSV file: Successfully written.")

# --------------- DATA MANIPULATION ---------------
# Load the Iris dataset and sort it by 'sepal_length'
df_iris = pd.read_csv('iris.csv')
df_sorted = df_iris.sort_values(by='sepal_length')
print("\nSorted DataFrame:")
print(df_sorted.head())

# Load the Melting Potatoes dataset and reshape it using the melt function
df_melting_potatoes = pd.read_csv('melting_potatoes.csv')
melted_df = pd.melt(df_melting_potatoes, id_vars=['id'], value_vars=['time_1', 'time_2'], var_name='time_type', value_name='time_value')
print("\nMelted DataFrame:")
print(melted_df.head())

# --------------- WORKING WITH SERIES ---------------
# Create a Series from a Python list
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("\nSeries:")
print(s)

# Load the Boston Housing dataset and perform basic operations on a Series
df_boston = pd.read_csv('boston_housing.csv')
s_sum = df_boston['RM'].sum()
s_mean = df_boston['RM'].mean()
print("\nSum:", s_sum)
print("Mean:", s_mean)

# --------------- SELECTING DATA FROM A DATAFRAME ---------------
# Load the Wine Quality dataset and select specific columns
df_wine = pd.read_csv('wine_quality.csv')
df_subset = df_wine[['pH', 'quality']]
print("\nSubset of DataFrame:")
print(df_subset.head())

# --------------- INDEXING ---------------
# Create an Index object
index = pd.Index(['A', 'B', 'C', 'D'])
print("\nIndex:")
print(index)

# --------------- GROUPING DATA ---------------
# Load the NYC Weather dataset and group data
df_weather = pd.read_csv('nyc_weather.csv')
grouped = df_weather.groupby('month').mean()
print("\nGrouped Data:")
print(grouped)

# --------------- PLOTTING ---------------
# Load the Stock Prices dataset and create a basic plot
df_stock_prices = pd.read_csv('stock_prices.csv')
df_stock_prices.plot(x='date', y='price')
plt.show()

# --------------- PIVOTING DATA ---------------
# Load the Sales dataset and create a pivot table
df_sales = pd.read_csv('sales.csv')
pivot_table = pd.pivot_table(df_sales, values='sales', index='region', columns='product')
print("\nPivot Table:")
print(pivot_table)
