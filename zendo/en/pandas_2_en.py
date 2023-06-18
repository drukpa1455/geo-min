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
