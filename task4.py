# Write a program which accepts email as form input or from terminal. Validate the
# email by checking if it's a valid email.
# Hint: Check if it contains an “@” symbol and “.” symbol.

email = input("Enter your email address: ") 

if "@" in email and "." in email:
    print("Valid email address")    
else:
    print("Invalid email address")
    