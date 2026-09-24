# Write a python program to store repeated values in a tuple and count how many times a given value appears

numbers = (10,20,10,20,30,40,30,20,50,60,30,20,10,40)

value = int(input("Enter the number to enter : "))

count = 0
for i in numbers:
    if i == value:
        count+=1

print(f"Number of times the {value} appeared is {count}")
