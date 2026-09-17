# Wap to count how many times a particular element appears in a list

n = int(input("Enter the number of elements in a list: "))

list = []

for i in range(0,n):
    num = int(input("Enter the number : "))
    list.append(num)



element = int(input("Enter element to search: "))

count = 0
for i in list:
    if i ==element:
        count+=1

print("no of times a element appears in a list : ",count)
