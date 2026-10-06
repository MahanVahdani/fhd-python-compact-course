import numpy as np

A = np.random.random((3, 4))

row_mean = A.mean(axis=1)

print(A - row_mean[:, np.newaxis])