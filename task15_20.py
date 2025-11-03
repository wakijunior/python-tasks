# Write a program that takes the date of birth of a person and the program outputs the
# age in terms of years,months,days TODAY.datetime

# date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")

# from datetime import date

# age = datetime.now() - datetime.strptime(date_of_birth, "%Y-%m-%d")
# years = age.days // 365
# months = (age.days % 365) // 30
# days = (age.days % 365) % 30





 


# print(f"Your age in months is: {years} years")
# print(f"Your age in months is: {months} months")
# print(f"Your age in days is: {days} days")

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
     print("{number3} is the largest")

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
value1 = input("Enter your password")

if value == username and value1 == password:
     print("Login is Successful")
else:
    if value != username and value1 != password:
      print("Invalid username or password")
      attempts -= 1
      if attempts == 0:
           print("You have been blocked")
           

   




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



# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them
# to find the gross salary then uses the gross salary to find the NHIF.
# To find the Kenya NHIF Rate using THIS LINK:
# Write a normal program but use functions if you feel comfortable.

basic_salary = float(input("Enter your basic salary: "))
benefits = float(input("Enter your benefits: "))
gross_salary = basic_salary + benefits
print(f"Your gross salary is: {gross_salary}")

if gross_salary <= 5999:
    nhif = 150  
elif gross_salary <= 7999:
    nhif = 300
elif gross_salary <= 11999:
    nhif = 400
elif gross_salary <= 14999:
    nhif = 500
elif gross_salary <= 19999:
    nhif = 600                  
elif gross_salary <= 24999:
    nhif = 750
elif gross_salary <= 29999:
    nhif = 850      
elif gross_salary <= 34999:
    nhif = 900
elif gross_salary <= 39999:
    nhif = 950
elif gross_salary <= 44999:
    nhif = 1000 
elif gross_salary <= 49999:
    nhif = 1100     
elif gross_salary <= 59999:
    nhif = 1200         
elif gross_salary <= 69999:
    nhif = 1300
elif gross_salary <= 79999:
    nhif = 1400
elif gross_salary <= 89999:
    nhif = 1500
elif gross_salary <= 99999:
    nhif = 1600 
else:
    nhif = 1700 
print(f"Your NHIF deduction is: {nhif}")    


# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use the gross salary to find the NSSF.
# To find the Kenya NSSF Rate using 6% of the Gross Salary. BUT ONLY A MINIMUM OF
# 18,000 Gross Salary CAN BE USED IN NSSF.
# Write a normal program but use functions if you feel comfortable.

if gross_salary >= 18000:
    nssf = gross_salary * 0.06  
else:
    nssf = 0
print(f"Your NSSF deduction is: {nssf}")

# Task 17: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s NHDF using:
# i.e NHDF = gross_salary * 0.015
# Write a normal program but use functions if you feel comfortable.

nhdf = gross_salary * 0.015
print(f"Your NHDF deduction is: {nhdf}")    

# Task 18: Using Python or PHP or Java or Ruby or JavaScript
# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF)
# Write a normal program but use functions if you feel comfortable.

taxable_income = gross_salary - (nssf + nhdf + nhif)
print(f"Your taxable income is: {taxable_income}")  

# TASK 19: Using Python or PHP or Java or Ruby or JavaScript *********************************
# Continue with the same program and find the person's PAYEE using the taxable
# income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK
# Write a normal program but use functions if you feel comfortable.

if taxable_income < 24000:
    payee = taxable_income * 0.1
elif taxable_income <= 32333:   
    payee = taxable_income * 0.25
else:
    payee = taxable_income * 0.3
print(f"Your PAYEE deduction is: {payee}")


# Task 20: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s Net Salary using:
# net_salary = gross_salary - (nhif + nhdf + nssf + payee)
# Create a class called Payroll whose major task is to calculate an individual’s Net
# Salary by getting the inputs basic salary and benefits. Create 5 different class
# methods which will calculate the payee, nhif_deductions, nhdf_deductions,
# nssf_deductions, gross_salary and net_salary.

net_salary = gross_salary - (nhif + nhdf + nssf + payee)
print(f"Your Net Salary is: {net_salary}")  

# class Payroll:
#     def __init__(self, basic_salary, benefits):
#         self.basic_salary = basic_salary
#         self.benefits = benefits
#         self.gross_salary = self.calculate_gross_salary()
#         self.nhif = self.calculate_nhif()
#         self.nssf = self.calculate_nssf()
#         self.nhdf = self.calculate_nhdf()
#         self.payee = self.calculate_payee()
#         self.net_salary = self.calculate_net_salary()

#     def calculate_gross_salary(self):
#         return self.basic_salary + self.benefits

#     def calculate_nhif(self):
#         gross_salary = self.gross_salary
#         if gross_salary <= 5999:
#             return 150  
#         elif gross_salary <= 7999:
#             return 300
#         elif gross_salary <= 11999:
#             return 400
#         elif gross_salary <= 14999:
#             return 500
#         elif gross_salary <= 19999:
#             return 600                  
#         elif gross_salary <= 24999:
#             return 750
#         elif gross_salary <= 29999:
#             return 850      
#         elif gross_salary <= 34999:
#             return 900
#         elif gross_salary <= 39999:
#             return 950
#         elif gross_salary <= 44999:
#             return 1000 
#         elif gross_salary <= 49999:
#             return 1100     
#         elif gross_salary <= 59999:
#             return 1200         
#         elif gross_salary <= 69999:
#             return 1300
#         elif gross_salary <= 79999:
#             return 1400
#         elif gross_salary <= 89999:
#             return 1500
#         elif gross_salary <= 99999:
#             return 1600 
#         else:
#             return 1700 

#     def calculate_nssf(self):
#         if self.gross_salary >= 18000:
#             return self.gross_salary * 0.06  
#         else:
#             return 0

#     def calculate_nhdf(self):
#         return self.gross_salary * 0.015

#     def calculate_payee(self):
#         taxable_income = self.gross_salary - (self.nssf + self.nhdf + self.nhif)
#         if taxable_income < 24000:
#             return taxable_income * 0.1
#         elif taxable_income <= 32333:   
#             return taxable_income * 0.25
#         else    
#             return taxable_income * 0.3
#     def calculate_net_salary(self):
#         return self.gross_salary - (self.nhif + self.nhdf + self.nssf + self.payee)
# payroll = Payroll(basic_salary, benefits)
# print(f"Your Net Salary is: {payroll.net_salary}")  