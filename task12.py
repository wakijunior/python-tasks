# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken as input from a user.

number = float(input("Enter a number: "))
number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))
number3 = float(input("Enter a number: "))

if number > number1 and number > number2 and number > number3:
    print(f"{number} is the largest")
elif number1 > number and number1 > number2 and number1 > number3:
    print(f"{number1} is the largest")
elif number2 > number and number2 > number1 and number2 > number3:
     print(f"{number2} is the largest")
else:
     print(f"{number3} is the largest")