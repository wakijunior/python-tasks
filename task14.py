# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should
# only accept numbers and floats only or otherwise display an error “invalid character
# entered” and take the user to re-enter the inputs .
# Once you learn functions,revisit this and write this code inside a function.

number = input(" Enter a number: ")
number1 = input(" Enter a number: ")

value = float(number)
value1 = float(number1)
 


if not isinstance(value, (int, float)) or not isinstance(value1, (int, float)):
    print("invalid character entered")
    print("Please re-enter {number4} and {number5}")

sum = value + value1

print(f"The sum of the two numbers is: {sum}")