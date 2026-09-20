from math import factorial

n = int(input("Enter a number: "))

# Method 1 – using the math module
print("Factorial using math:", factorial(n))

# Method 2 – using a for-loop
result = 1
for i in range(1, n + 1):
    result = result * i

print("Factorial using loop:", result)