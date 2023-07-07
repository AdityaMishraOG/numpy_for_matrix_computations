import numpy as np
from scipy.linalg import lu
np.set_printoptions(precision=3, suppress=True)

# Define the matrix
matrix = np.array([[1, 2, 3], [4, 8, 12], [7, 8, 9]])

# Apply LU decomposition
P, L, U = lu(matrix)

# Perform row operations to achieve row reduced echelon form
U[np.abs(U) < 1e-10] = 0

# Print the row reduced echelon form
print(U)
