# Write a python prorgam to show that the tuple values cannot be changed directly . Convert tuple into list ,update it and convert it back into tuple


numbers = (10,20,30,40)

print("Original tuple: ",numbers)

temp = list(numbers)
temp[1] = 200

numbers = tuple(temp)

print("Updated tuple :",numbers)