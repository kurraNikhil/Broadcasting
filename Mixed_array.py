import numpy as np

# Create two arrays with mixed types
a = np.array([1, 2, 3], dtype=np.int32)
b = np.array([10.5, 11.5, 12.5], dtype=np.float64)

# Add the two arrays using broadcasting
c = a + b

# Print the result
print(c)
