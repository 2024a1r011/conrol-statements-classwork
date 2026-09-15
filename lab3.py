# String operations

text = "Welcome to Python world"

# Count the number of alphabets
count = 0

for char in text:
    if char.isalpha():
        count += 1

print("Number of alphabets:", count)

# Extract characters from a range
print("Characters from index 11 to 17:", text[11:18])

# Check whether the string is alphanumeric
print("Is the string alphanumeric?", text.isalnum())