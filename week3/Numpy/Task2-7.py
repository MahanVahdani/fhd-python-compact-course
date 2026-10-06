import numpy as np

A = np.arange(256).reshape(16, 16)

result = A.reshape(4, 4, 4, 4).sum(axis=(1, 3))

print(result)