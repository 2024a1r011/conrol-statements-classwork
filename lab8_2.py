# Create a database using lists and tuples. Each student record must contain roll number, name, branch, and CGPA. Store each record as a tuple inside a list. Display all records and search for a student using roll number.


n = int(input("Enter number of students: "))
database = []

for i in range(n):
    roll = int(input("Enter the roll number : "))
    name = input("Enter name : ")
    branch = input("Enter branch : ")
    cgpa = float(input("Enter CGPA : "))
    student = (roll,name,branch,cgpa)
    database.append(student)
print("Student records : ")

for student in database:
    print(database)

search = int(input("Enter the roll number  to search : "))
found = False

for student in database:
    if student[0] == search:
        print("Student Found")
        print("Roll:",student[0])
        print("Name:",student[1])
        print("Branch:",student[2])
        print("CGPA:",student[3])
    if found == False:
        print("Student not found ")