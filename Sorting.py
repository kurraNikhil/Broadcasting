import numpy as np

# Create a 2D array
a = np.array([[1, 3, 2], [4, 6, 5]])

# Broadcast the array using a sorting function
b = np.argsort(a, axis=1)

# Print the result
print(b)
