import numpy as np

# Create a 2D array
a = np.array([[1, 2, 3], [4, 5, 6]])

# Broadcast the array using a reduction function
b = np.min(a, axis=0)

# Print the result
print(b)
