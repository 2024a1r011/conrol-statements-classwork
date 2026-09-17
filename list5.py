# to input numbers in a list and create two seperate lists for even and odd numbers

n = int(input("Enter the number of elements in a list: "))

list = []

for i in range(0,n):
    num = int(input("Enter the number : "))
    list.append(num)

even_list = []
odd_list = []

for i in list:
    if i%2 ==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("even list :",even_list)
print("Odd list : ",odd_list)
