s1 = input("Enter a string: ")

total = 0
count = 0

for char in s1:
    if char.isdigit():
        total += int(char)
        count += 1

if count > 0:
    average = total / count
    print("Sum:", total)
    print("Average:", average)
else:
    print("No digits found.")