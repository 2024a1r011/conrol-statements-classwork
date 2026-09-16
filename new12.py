'''write a python program to print inverted right angled triangle using stars.
****
***
**
*'''

print("Inverted Right angled traingle")
n=5
for i in range(n):
    for j in range(i,n):
        print("*",end = " ") 
    for j in range(i+1):
        print(" ",end = "")
    print()
    