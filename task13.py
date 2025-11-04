# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user and checks if
# they are equal to “admin@mail.com” and password is “Admin@123” , if so then print
# “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3
# tries after which it notifies you that you have been blocked.
# Once you learn functions,revisit this and write this code inside a function.

username = "admin@mail.com"
password = "Admin@123"
attempts = 3

value = input("Enter your username: ").lower
value1 = input("Enter your password: ")

while attempts > 0:
    if value == username and value1 == password:
        print("Login is Successful")
    else:
        if value != username and value1 != password:
            print("Invalid username or password")
            attempts -= 1  
            value1 = input("Enter your password: ") 
        else:      
            if attempts == 0:
                print("You have been blocked")