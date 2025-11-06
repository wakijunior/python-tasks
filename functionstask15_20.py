# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them
# to find the gross salary then uses the gross salary to find the NHIF.
# To find the Kenya NHIF Rate using THIS LINK:
# Write a normal program but use functions if you feel comfortable.

basic_salary = float(input("Enter your basic salary: "))
benefits = float(input("Enter your benefits: "))

def find_gross_salary(x,y):
    return x + y
gross_salary = find_gross_salary(basic_salary, benefits)

def get_nhif(value):
    if value == 5999:
        return 150  
    elif value >= 6000 and value <= 7999:
        return 300
    elif value >= 8000 and value <= 11999:
        return 400
    elif value >= 12000 and value <= 14999:
        return 500
    elif value >= 15000 and value <= 19999:
        return 600                  
    elif value >= 20000 and value <= 24999:
        return 750
    elif value >= 25000 and value <= 29999:
        return 850      
    elif value >= 30000 and value <= 34999:
        return 900
    elif value >= 35000 and value <= 39999:
        return 950
    elif value >= 40000 and value <= 44999:
        return 1000 
    elif value >= 45000 and value <= 49999:
        return 1100     
    elif value >= 50000 and value <= 59999:
        return 1200         
    elif value >= 60000 and value <= 69999:
        return 1300
    elif value >= 70000 <= 79999:
        return 1400
    elif value >= 80000 <= 89999:
        return 1500
    elif value >= 90000 and value <= 99999:
        return 1600 
    elif value > 100000:
        return 1700 
    else:
        return "In eligible salary"

nhif = get_nhif(gross_salary)


# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM 
# OF 18,000 Gross Salary CAN BE USED IN NSSF. 

def get_nssf(social):
     if social >= 18000:
        return social * 0.06
     else:
         return "Ineligible"
nssf = get_nssf(gross_salary)

# Task 17: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015
# Write a normal program but use functions if you feel comfortable.
 
def get_nhdf(x):
    return x * 0.015
nhdf = get_nhdf(gross_salary)

# Task 18: Using Python or PHP or Java or Ruby or JavaScript
# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 

def get_total_deductions(a,b,c):
    return a + b + c
total_deductions = get_total_deductions(nssf, nhdf, nhif)

def find_taxable_income(y, z):
    return y - z
taxable_income = find_taxable_income(gross_salary, total_deductions)

# TASK 19: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and find the person's PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK

def get_payee(d):
    if d > 24000 and d <=32333:
        a = d - 24000
        b = a * 0.25
        return a - 2400
    elif d > 32333 and d <= 500000:
        a = 8333 * 0.25
        b = d - 32333
        c = b * 0.3
        return a + c - 2400
    elif d > 500000 and d <= 800000:
        a = 8333 * 0.25
        b = 467667 * 0.3
        c = d - 500000
        e = e * 0.325
        return a + b + e - 2400
    else:
        if d > 800000:
            a = 8333 * 0.25
            b = 467667 * 0.3
            c = d - 800000
            e = c * 0.35
            return a + b + e - 2400
payee = get_payee(taxable_income)

# Task 20: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

def get_net_salary():
    x = gross_salary
    y = total_deductions + payee
    return x - y
net_salary = get_net_salary()



print("Your gross salary is: ", gross_salary)
print("Your NHIF deductions amount to: ", nhif)
print("Your NSSF deductions amount to: ", nssf)
print("Your NHDF deductions amount to: ", nhdf)
print("Your total deductions is: ", total_deductions)
print("Your taxable income is: ", taxable_income)
print("Your PAYEE is: ", payee)
print("Your ner salary is: ", net_salary)