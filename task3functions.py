# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in 
# three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 

def find_largest_value():
    value1 = float(input("Enter a number: "))
    value2 = float(input("Enter a number: "))
    value3 = float(input("Enter a number: "))

    if value1 > value2 and value1 > value3:
        return value1

    if value2 > value1 and value2 > value3:
        return value2

    else:
        return value3
output = find_largest_value()
print(output)

    

   
   


