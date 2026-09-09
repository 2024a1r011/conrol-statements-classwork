# write a python program to check whether a number is perfect number . A number is perfect if the sum of its proper divisors is equal to the number itself 

a = int(input("Enter a number : "))

divisor_sum = 0

for i in range(1,a):
    if a%i == 0:
        divisor_sum +=i

if  divisor_sum == a:
    print("its a perfect number ")
else:
    print("It's not a perfect number")