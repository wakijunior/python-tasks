# Write that prompts the user to input student marks. The input should be between 0
# and 100.Then output the correct grade:
# A > 79 , B - 60 to 79, C > 49 to 59, D - 40 to 49, E - less 40

marks = float(input("Enter the student marks (0-100): "))

if 0 <= marks <= 100:
    if marks > 79:
        grade = 'A'
    elif 60 <= marks <= 79:
        grade = 'B'
    elif 50 <= marks <= 59:
        grade = 'C'
    elif 40 <= marks <= 49:
        grade = 'D'
    else:
        grade = 'E'
    
    print(f"The grade is: {grade}")