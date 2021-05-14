# Numpy array (aka. ndarray, numbered dimensions array) is an array type that hold multiple dimensions
# You can have a 1-D array, 2-D array, 3-D array, and more
# The number of square brackets in the beginning show the dimension of the array

import numpy as np 

# 1-D array
one_d_array = np.array([1, 2, 3, 4])
print(f"1-D array: {one_d_array}")

# 2-D array
two_d_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"2-D array: {two_d_array}")

# Mathematical operations can be simultaneously performed on each elements of the entire array
print(f"mathematical subtractions on numpy 1-D array: {one_d_array - 2}")
print(f"mathematical subtractions on numpy 2-D array: {two_d_array - 2}")
