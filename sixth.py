# Write a python program to input four numbers from the user and find the greatest number among them

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
d = int(input("Enter 4th number : "))

if a>=b and b>=c and c>=d:
    print("A is the greatest number")
elif b>=c and c>=d:
    print("B is the greatest number")
elif c>=d:
    print("C is the greatest number") 