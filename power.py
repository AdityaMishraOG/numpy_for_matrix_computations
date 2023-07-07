import numpy as np
np.set_printoptions(precision=3, suppress=True)

# Define the matrix A
A = np.array([[0.7, 0.3], [0.3, 0.7]])

# Define the value of n for the power
n = 100000

# Calculate the nth power of the matrix A
A_power = np.linalg.matrix_power(A, n)

# Print the result
print("A raised to the power of", n)
print(A_power)
print()
