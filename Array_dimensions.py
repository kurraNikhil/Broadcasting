import numpy as np

# Create two arrays with different dimensions
a = np.array([1, 2, 3])
b = np.array([[10, 11, 12], [20, 21, 22]])

# Add the two arrays using broadcasting
c = a + b

# Print the result
print(c)
