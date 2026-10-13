# wap to perform seaching using linear and binary search

n = int(input("total no of students : "))

list =[]

for i in range(0,n):
    a = int(input("marks of student : "))
    list.append(a)

x = int(input("Enter the element to search : "))
if x in list:
    print("Element found -- linear search ",x)
else:
    print("Element not found ")


list.sort()

low = 0
high = len(list) -1

while low<=high:
    mid = (low+high)//2

    if list[mid] == x:
        print("Element found ")
        break
    elif list[mid] < x:
         low = mid +1
    elif list[mid] > x:
        high = mid-1
    else:
        print("Element not found")






