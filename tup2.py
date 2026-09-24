# Write a python program to store all month names in a tuple . input a month number and display the corresponding month name 

months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

num = int(input("Enter a month number (1-12) : "))

if 1 <= num <= 12:
    print(f"month number is {num}, Monthname is {months[num-1]}")
else:
    print("Invalid month entered")