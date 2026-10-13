# Create a class and object .student details
# Problem : create a student class to store a student's name and roll number . Create an object and disply the details
# using an instance method

class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def display(self):
        print("Student Name :",self.name)
        print("Student's roll_no : ",self.rollno)

s1 = Student("Vishu",101)

s1.display()