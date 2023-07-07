import numpy as np
np.set_printoptions(precision=3, suppress=True)

# Define the matrix
A = np.array([[0.5, 0.5], [0.5, 0.5]])

# Perform eigenvalue decomposition
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print()
print(eigenvectors)
print()
# Create a diagonal matrix of eigenvalues
D = np.diag(eigenvalues)
print(D)
print()

# Calculate the inverse of the eigenvector matrix
V_inv = np.linalg.inv(eigenvectors)

# Diagonalize the matrix
diagonalized_matrix = np.dot(np.dot(eigenvectors, D), V_inv)

# Print the diagonalized matrix
print(diagonalized_matrix)
