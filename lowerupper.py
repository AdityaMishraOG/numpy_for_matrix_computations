import numpy as np
import scipy.linalg
np.set_printoptions(precision=3, suppress=True)

# Define the matrix
A = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])

# Perform LU decomposition
P, L, U = scipy.linalg.lu(A)

# Print the decomposed matrices
print("P is: ")
print(P)
print()
print("L is: ")
print(L)
print()
print("U is: ")
print(U)
print()
