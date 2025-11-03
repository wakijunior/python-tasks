# Write a program that lets the user input a password. Give them only 4 attempts to
# check the passwords entered against “admin@123”. If the password is correct
# access is granted. After you show them a message , the account is blocked.    

correct_password = "admin@123"
attempts = 4

while attempts > 0:
    password = input("Enter your password: ")
    
    if password == correct_password:
        print("Access granted")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. You have {attempts} attempts left.")
        
        if attempts == 0:
            print("Account is blocked.")
