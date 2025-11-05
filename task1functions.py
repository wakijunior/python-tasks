# Write a program that prompts the user to enter the base and 
# height of a triangle and returns its area.
def find_area():
    base = float(input("Enter the base of triangle: ")) 
    height = float(input("Enter the height of triangle: "))
    x = 1/2 * base * height
    return x
area = find_area()
print(area)