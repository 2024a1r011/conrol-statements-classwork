# Write a python program to input marks of 5 students .
# For each student , the program should the check whether the entered mask are valid or invalid .Marks are considered valid only if they are between 0 and 100 . if the marks are invalid the program should display "Invalid marks skipped " and move and move to the next student without printing those marks .
# If the marks are valid the program should display the valid marks

for i in range(5):
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks skipped")
        continue

    print("Valid marks:", marks)