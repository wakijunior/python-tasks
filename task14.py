# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should
# only accept numbers and floats only or otherwise display an error “invalid character
# entered” and take the user to re-enter the inputs .
# Once you learn functions,revisit this and write this code inside a function.

number4 = float(input(" Enter a number: "))
number5 = float(input(" Enter a number: "))
 
sum = number4 + number5
print(f"The sum of the two numbers is: {sum}")

if not isinstance(number4, (int, float)) or not isinstance(number5, (int, float)):
    print("invalid character entered")
    print("Please re-enter {number4} and {number5}")
