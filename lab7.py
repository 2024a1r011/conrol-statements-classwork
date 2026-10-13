
# WAP to create records of n students
# Store each record as a dictionary
# Search for a student using roll number

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

search_roll = int(input("\nEnter roll number to search: "))

found = False

for student in students:
    if student["roll"] == search_roll:
        print("\nStudent found:")
        print(student)
        found = True
        break

if found == False:
    print("Student not found")