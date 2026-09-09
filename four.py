# Write a program to create a simple password validation system.
# The prorgam should repeatdely ask the user to enter a password untill a valid password is entered .A password will be considered  valid only if it has atleast 8 characters and contains the @ symbol.
# Once the user enters a valid password , the program should display " Password accepted ." and stop otherwise  it should display "Weak password .Try again"  and ask for the password again.

while True:
    password = input("Enter password: ")

    if len(password) >= 8 and "@" in password:
        print("Password accepted.")
        break
    else:
        print("Weak password. Try again")