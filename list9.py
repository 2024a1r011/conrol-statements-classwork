# input two lists and create a third list  containing common elements.


n1 = int(input("Enter the number of elements in a list1: "))

list1 = []

for i in range(0,n1):
    num = int(input("Enter the number : "))
    list1.append(num)


n2 = int(input("Enter the number of elements in a list: "))
list2 = []

for i in range(0,n2):
    num = int(input("Enter the number : "))
    list2.append(num)

common = []

for i in list1:
    if i in list2:
        common.append(i)

print("common elements are ",common)