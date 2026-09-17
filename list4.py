# Input a list of numbers and create a new list containing only unique elements 


n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Unique elements:", unique)