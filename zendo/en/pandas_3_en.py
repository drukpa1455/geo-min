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
