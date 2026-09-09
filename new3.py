#Write a python program to input two number and find the greatest common divisor using a loop 
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

if a>b:
    num1 = a
    num2 = b
else:
    num1 =b
    num2 =a

while num2 !=0:
    rem = num1 % num2
    num1 = num2
    num2 = rem

print("GCD is : ",num1)

