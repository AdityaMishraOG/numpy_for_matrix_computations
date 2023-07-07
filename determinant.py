import numpy as np
np.set_printoptions(precision=3, suppress=True)

matrix = np.array([[1, 2], [3, 4]])

det = np.linalg.det(matrix)

print(det)
