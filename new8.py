# Write a python program to repeatedly calculate the sum of digits of a number untill the result becomes a single digit

num = int(input("Enter the number : "))
sum = 0
while num >9 or sum>9:
    if num>9:
        sum = sum +num%10
        num =num//10
    else:
        num = sum
        sum =0
print(num)