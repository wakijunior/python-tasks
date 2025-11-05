# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,then a functions that finds the grade according to the table below. 

# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40



def find_total_marks():
    maths = float(input("Enter your Score: "))
    eng = float(input("Enter your Score: "))
    swa = float(input("Enter your Score: "))
    sci = float(input("Enter your Score: "))
    sos = float(input("Enter your Score: "))
    x = maths + eng + swa + sci + sos
    return x
marks = find_total_marks()
print(marks)

def average_marks():
    y = marks / 5
    return y
avr = average_marks()
print(avr)

def find_grade():
    if avr >79:
       return "A"
    elif avr >= 60 and avr <= 79:
        return "B"
    elif avr >= 50 and avr <= 59:
        return "C"
    elif 40 <= avr >= 49:
        return "D"
    else:
        return "E"
grade = find_grade()
print(grade)
    

    



    
