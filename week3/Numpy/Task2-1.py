import numpy as np

def numbers(start, end):
    for i in range(start, end):
        yield i

start = int(input("From: "))
end = int(input("To: "))

a = np.array(list(numbers(start, end)))

print(a)