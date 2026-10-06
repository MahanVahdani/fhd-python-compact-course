import numpy as np

data = np.array([
    (10, 20, 255, 0, 0),
    (30, 40, 0, 255, 0)
], dtype=[
    ("x", "i4"),
    ("y", "i4"),
    ("r", "i4"),
    ("g", "i4"),
    ("b", "i4")
])

print(data)