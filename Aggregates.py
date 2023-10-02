import numpy as np

# Create a 2D array
a = np.array([[1, 2, 3], [4, 5, 6]])

# Broadcast the array using an aggregate function
b = np.sum(a, axis=1)

# Print the result
print(b)
