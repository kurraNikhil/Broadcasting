import numpy as np

# Create two masked arrays
a = np.ma.masked_array([1, 2, 3], mask=[True, False, False])
b = np.ma.masked_array([10, 20, 30])

# Add the two masked arrays using broadcasting
c = a + b

# Print the result
print(c)
