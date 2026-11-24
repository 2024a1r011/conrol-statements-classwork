
# Program to create a text file and write three lines

file = open("MyFile.txt", "w")

line1 = input("Enter first line: ")
line2 = input("Enter second line: ")
line3 = input("Enter third line: ")

file.write(line1 + "\n")
file.write(line2 + "\n")
file.write(line3 + "\n")

file.close()

print("Data written successfully.")

# Display file contents
file = open("MyFile.txt", "r")

print("\nContents of MyFile.txt:")
print(file.read())

file.close()
