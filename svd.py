import numpy as np
np.set_printoptions(precision=3, suppress=True)

# Define the matrix A
A = np.array([[1, 0, 1], [-1, 1, 0]])

# Perform Singular Value Decomposition (SVD)
U, S, V = np.linalg.svd(A)

# Print the factorized matrices
print("U:")
print(U)
print()
print("S:")
print(S)
print()
print("V:")
print(V)
print()
