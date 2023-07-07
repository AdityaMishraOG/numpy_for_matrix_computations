import numpy as np
np.set_printoptions(precision=3, suppress=True)


def gram_schmidt(A):
    # Get the number of vectors and dimensionality
    n, m = A.shape

    # Create an empty matrix to store the orthogonalized vectors
    Q = np.zeros((n, m))

    for i in range(n):
        # Orthogonalize the i-th vector against previous vectors
        Q[i] = A[i]

        for j in range(i):
            Q[i] -= np.dot(A[i], Q[j]) / np.dot(Q[j], Q[j]) * Q[j]

        # Normalize the orthogonalized vector
        Q[i] /= np.linalg.norm(Q[i])

    return Q


# Define the input matrix
A = np.array([[0, 1, 0], [2, 2, 0], [1, 3, 3]])

# Perform Gram-Schmidt process
Q = gram_schmidt(A)

# Print the orthogonalized matrix
print(Q)
