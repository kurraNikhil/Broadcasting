import numpy as np

# Create a 3D array
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Broadcast the array using advanced indexing
b = a[Ellipsis, None, 1]

# Print the result
print(b)
