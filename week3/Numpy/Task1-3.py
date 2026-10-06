import numpy as np

a = np.random.random((5, 5))

a = (a - a.min()) / (a.max() - a.min())

print(a)