import numpy as np
from sklearn.datasets import load_iris

# Introduction to NumPy
# NumPy is a Python library for numerical computation. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

# Arrays
# An array is a central data structure in NumPy. It is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers.

# Creating Arrays
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)  # Convert a list to a NumPy array
print(my_array)
# Output: [1 2 3 4 5]

zeros_array = np.zeros((3, 4))  # Create a 3x4 array of zeros
ones_array = np.ones((2, 2))  # Create a 2x2 array of ones
random_array = np.random.random((2, 3))  # Create a 2x3 array of random numbers between 0 and 1

print(zeros_array)
print(ones_array)
print(random_array)

# Array Attributes
my_array = np.array([[1, 2, 3], [4, 5, 6]])
print(my_array.shape)  # Shape of the array
# Output: (2, 3)
print(my_array.dtype)  # Data type of the array
# Output: int64
print(my_array.size)  # Number of elements in the array
# Output: 6
print(my_array.ndim)  # Number of dimensions of the array
# Output: 2

# Array Indexing
my_array = np.array([1, 2, 3, 4, 5])
print(my_array[0])  # Access the first element
# Output: 1
print(my_array[3])  # Access the fourth element
# Output: 4

my_array = np.array([[1, 2, 3], [4, 5, 6]])
print(my_array[0, 1])  # Access element at row 0, column 1
# Output: 2
print(my_array[1, 2])  # Access element at row 1, column 2
# Output: 6

# Array Slicing
my_array = np.array([1, 2, 3, 4, 5])
print(my_array[1:4])  # Slice elements from index 1 to 3
# Output: [2 3 4]
print(my_array[:3])  # Slice elements from the start to index 2
# Output: [1 2 3]
print(my_array[::2])  # Slice elements with a step size of 2
# Output: [1 3 5]

my_array = np.array([[1, 2, 3], [4, 5, 6]])
print(my_array[:, 1:])  # Slice all rows and columns starting from index 1
# Output: [[2 3]
#          [5 6]]

# Array Reshaping
my_array = np.array([1, 2, 3, 4, 5, 6])
reshaped_array = my_array.reshape((2, 3))  # Reshape the array to a 2x3 matrix

print(reshaped_array)
# Output: [[1 2 3]
#          [4 5 6]]

# Array Operations
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

result = array1 + array2
print(result)
# Output: [5 7 9]

result = array1 * array2
print(result)
# Output: [4 10 18]

result = np.maximum(array1, array2)
print(result)
# Output: [4 5 6]

# Mathematical Functions
array = np.array([0, np.pi/2, np.pi])
result = np.sin(array)
print(result)
# Output: [0.00000000e+00 1.00000000e+00 1.22464680e-16]

array = np.array([1, 10, 100])
result = np.log10(array)
print(result)
# Output: [0. 1. 2.]

array = np.array([0, 1, 2])
result = np.exp(array)
print(result)
# Output: [1.         2.71828183 7.3890561 ]

# Linear Algebra
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = np.matmul(matrix1, matrix2)
print(result)
# Output: [[19 22]
#          [43 50]]

matrix = np.array([[1, 2], [3, 4]])
inverse_matrix = np.linalg.inv(matrix)
print(inverse_matrix)
# Output: [[-2.   1. ]
#          [ 1.5 -0.5]]

# Random Number Generation
random_integer = np.random.randint(10)
print(random_integer)

random_samples = np.random.normal(size=(3, 3))
print(random_samples)

# Input and Output
array = np.array([1, 2, 3, 4, 5])
np.save('my_array.npy', array)

loaded_array = np.load('my_array.npy')
print(loaded_array)
# Output: [1 2 3 4 5]

# Broadcasting
array1 = np.array([1, 2, 3])
scalar = 2
result = array1 * scalar
print(result)
# Output: [2 4 6]

# Advanced Topics

# Vectorized Functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

vectorized_sigmoid = np.vectorize(sigmoid)
array = np.array([0, 1, 2, 3])
result = vectorized_sigmoid(array)
print(result)
# Output: [0.5        0.73105858 0.88079708 0.95257413]

# Memory Optimization
big_array = np.ones((1000, 1000))
print(big_array.nbytes)
# Output: 8000000 (8 megabytes)

# Structured Arrays
structured_array = np.array([(1, 2.0, 'Hello'), (2, 3.5, 'World')],
                            dtype=[('integer', int), ('float', float), ('string', object)])
print(structured_array['integer'])
# Output: [1 2]
print(structured_array['float'])
# Output: [2.  3.5]
print(structured_array['string'])
# Output: ['Hello' 'World']

# Fancy Indexing
array = np.array([1, 2, 3, 4, 5])
mask = array > 2
print(array[mask])
# Output: [3 4 5]

# Universal Functions
array = np.array([1, 2, 3, 4, 5])
result = np.square(array)
print(result)
# Output: [ 1  4  9 16 25]

# Load Iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Target variable

# Perform operations using Iris dataset
# Example: Calculate the mean of sepal lengths using the first feature (sepal length)
mean_sepal_length = np.mean(X[:, 0])
print(mean_sepal_length)

# Example: Select the first three rows of the dataset
subset = X[:3, :]
print(subset)

# Example: Calculate the sum of each column in the dataset
column_sums = np.sum(X, axis=0)
print(column_sums)

# Example: Calculate the dot product of two feature columns
dot_product = np.dot(X[:, 0], X[:, 1])
print(dot_product)

# ... (More advanced topics)

# You can find more detailed information and examples in the official NumPy documentation.