import numpy as np

a = np.random.random(5) * 10

print("Original:", a)
print("astype:", a.astype(int))
print("floor:", np.floor(a))
print("ceil:", np.ceil(a))
print("trunc:", np.trunc(a))
print("divide:", (a // 1).astype(int))