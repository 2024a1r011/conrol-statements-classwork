# Write a python program to check whether a given value is present in a tuple . if present,display its position.



tup = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
check = int(input("Enter a value to check: "))

found = False

for i in range(len(tup)):
    if tup[i] == check:
        print("Value is present in the tuple")
        print("Position is:", i)
        found = True
        break

if not found:
    print("Value is not present in the tuple")