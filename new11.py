'''write a python program to print a right angles triangle triangle using stars.
*
**
***
****'''

n = int(input("Enter the number of rows : "))

for i in range(0,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()