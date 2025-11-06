# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should
# only accept numbers and floats only or otherwise display an error “invalid character
# entered” and take the user to re-enter the inputs .
# Once you learn functions,revisit this and write this code inside a function.





while True:
    number = input(" Enter a number: ")
    number1 = input(" Enter a number: ")

    if number.count('-') > 1 or ('-' in number[1:]):
        validity = False
    elif number.count(".") > 1:
        validity = False
    
    else:
        temp = number.replace("-", "") .replace(".", "") 
        validity = temp.isdigit() 

    if number1.count("-") > 1 or ("-" in number1[1:]):
        validity1 = False
    elif number1.count(".") > 1:
        validity1 = False
    else:
        temp1 = number1.replace("-", "") .replace(".", "") 
        validity1 = temp1.isdigit() 

    if validity and validity1:
        value = float(number)
        value1 = float(number1)

        sum = value + value1
        print(f"The sum of the two numbers is: {sum}")
        
        break
    else:
        print("invalid character entered")
        print("Please re-enter {number} and {number1}")

    

 


# if not isinstance(value, (int, float)) or not isinstance(value1, (int, float)):
#     print("invalid character entered")
#     print("Please re-enter {number4} and {number5}")

# sum = value + value1

