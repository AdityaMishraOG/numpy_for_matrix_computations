import numpy as np
np.set_printoptions(precision=3, suppress=True)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = np.dot(A, B)
D = np.add(A, B)
E = np.subtract(A, B)
F = np.linalg.inv(A)
print(C)
print()
print(D)
print()
print(E)
print()
print(F)
print()
