import numpy as np

A = np.array([
    [3, 8, 2],
    [1, 5, 7],
    [2, 4, 6]
])

A = A[A[:, 1].argsort()]

print(A)