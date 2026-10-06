import numpy as np

points = np.random.random((100, 2))

distances = np.sqrt(np.sum(points ** 2, axis=1))

print(distances)