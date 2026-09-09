# Write a python prorgam to input a number and check whether it is prime or not .A nnumber is prime if it has no divisor other than 1 and itself

a = int(input("Enter a number  : "))
if a>1:
    for i in range(2,a):
        if a%i !=0:
            print("It is a prime number ")
            break
        else:
            print("It's not a prime number")
            break
