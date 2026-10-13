# Wap to reverse every kth row in a matrix

rows = int(input("Enter the number of rows : "))
col = int(input("Enter the number of columns "))

matrix = []

for i in range(rows):
    row =[]
    for j in range(col):
        num = int(input("Enter element : "))
        row.append(num)
    matrix.append(row)

k = int(input("Enter k :"))

for i in range(len(matrix)):
    if (i+1)%k == 0:
        matrix[i].reverse()

print("Matrix after reversing : ")

for row in matrix:
    print(row)