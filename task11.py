# Write a program that takes the date of birth of a person and the program outputs the
# age in terms of years,months,days TODAY.datetime

# date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")

from datetime import datetime
today = datetime.today()


datebirth = input("please enter your date of birth (YYYY-MM-DD): ")
bod_years = datebirth[0:4]
bod_month = datebirth[5:7]
bod_day = datebirth[8:10]

today_year = today.year
today_month = today.month
today_day = today.day

age_years = today_year - int(bod_years) 
age_month = today_month - int(bod_month)  
age_day = today_day - int(bod_day) 

if age_month<0:
    age_years -= 1
elif age_day<0:
    age_month -= 1
    age_day += 30


print(f"Your age is {age_years} years, {age_month} months, and {age_day} days.")












