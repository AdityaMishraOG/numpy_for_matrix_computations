import numpy as np
np.set_printoptions(precision=3, suppress=True)


# Define the matrix
A = np.array([[1, 2, 2], [-1, 1, 2], [-1, 0, 1], [1,1,2]])

# Perform QR factorization
Q, R = np.linalg.qr(A)

# Print the factorized matrices
print("Q:")
print(Q)
print()
print("R:")
print(R)
print()


Qt = np.transpose(Q)
I = np.dot(Qt, Q)
I2 = np.dot(Q, Qt)
print(I)
print()
print(I2)
print()
