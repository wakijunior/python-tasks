class Payroll:
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