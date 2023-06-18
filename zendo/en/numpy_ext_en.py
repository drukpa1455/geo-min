import numpy as np
import matplotlib.pyplot as plt

# Generate random data for regression
np.random.seed(0)
X = 2 * np.random.rand(100, 1)  # Generate 100 random samples between 0 and 2
y = 4 + 3 * X + np.random.randn(100, 1)  # Generate target values with noise

# Add a column of ones to X for the bias term
X_b = np.c_[np.ones((100, 1)), X]

# Perform linear regression using the normal equation
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Print the regression coefficients
print("Intercept:", theta_best[0])
print("Slope:", theta_best[1])

# Predict using the trained model
X_new = np.array([[0], [2]])  # New input values
X_new_b = np.c_[np.ones((2, 1)), X_new]  # Add a column of ones for bias term
y_predict = X_new_b.dot(theta_best)

# Plot the training data and the linear regression line
plt.plot(X, y, 'b.')  # Scatter plot of the training data
plt.plot(X_new, y_predict, 'r-', label='Predictions')  # Regression line
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()
