tuples = []

for i in range(5):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    pair = (num1, num2)
    tuples.append(pair)
    print("Current list:", tuples)

result = sorted(tuples, key=lambda x: x[-1])

print("Sorted list:", result)