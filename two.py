# 2. White a Python program to simulate a digital lock system.
# The lock should ask the user to enter a 4-digit PIN.
#  If the entered PIN does not contain exactly 4 digits,
#  the program should display an error message and ask again. 
# If the entered PIN is correct, the lock should open. Otherwise, 
# the program should ask the user to try again.


while True:
    pin = input("Enter the pin : ")

    if len(pin)!=4 or not pin.isdigit():
        print("Error pin must contain exactly 4 digits " )
        continue

    correct_pin = "1234"
    if pin == correct_pin:
        print("Lock will open")
        break
    else:
        print("Incorrect pin")

    


