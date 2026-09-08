# # 1. Write a Python program to determine whether a student is eligible for a scholarship.
# The scholarship should be granted if the student satisfies either of the following conditions:
# a) The student has a CGPA of 8.5 or above and attendance of 85 percent or above.
# b) The student has won a national-level competition.
# The program should take CGPA, attendance percentage, and national-level competition status as input, then display whether the student is eligible for the scholarship.

cgpa = float(input("Enter the cgpa of the student : "))
att =int(input("Enter the attendance in % : "))

NLC = (input("if any national level comp won/ not :"))

if cgpa >8.5 and att >85:
    print("Scholarship Granted ")
elif NLC == "won":
    print("Scholarship Granted ")
else:
    print("Scholarship not granted")

