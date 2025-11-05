
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

