# Write  a python program that asks the user to enter a username and password . the user should get only 3 attempts . if the correct credentials are entered ,display "login succesfull" and stop the loop .if all the atempts are used ,display "Account Locked"
username = "admin"
correct_pass  = "Vishavjeet001"
for i in range(0,2):
    username1 =input("Enter a username : ")
    password = input("Enter the password : ")

    if password == correct_pass and username == username1:
        print("Login succesfull")
        break
    else:
        print("Login failed")
        



    
