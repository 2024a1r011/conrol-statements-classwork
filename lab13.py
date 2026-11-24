#  13. Write a program that inputs a text file. The program should print all of the unique words in the file in 
# alphabetical order. 
 

# Program to display unique words in alphabetical order

filename = input("Enter file name: ")

with open(filename, "r") as file:
    text = file.read()

words = text.split()

unique_words = set(words)

sorted_words = sorted(unique_words)

print("Unique words in alphabetical order:")

for word in sorted_words:
    print(word)
