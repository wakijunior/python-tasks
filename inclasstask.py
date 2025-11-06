# write a program that reverses a string.

string = "Hello this is python programming"

def reverse_string(str):
    return str[::-1]

my_reversed_string = reverse_string(string)
print(my_reversed_string)

# write a python program to print the even numbers from a given list.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def even_number_selector(numbers):
    list1 = []
    # even = [val for val in list if val % 2 == 0]
    # return even
    for i in numbers:
        if i%2 ==0:
            list1.append(i)
    return list1

even_numbers = even_number_selector(list)   
print(even_numbers) 

# write a python program to create and print a list where the values are the square of 
# numbers between 1 and 30 (both included)

def squares_of_numbers():
    squares = []
    for i in range(1, 31):
        squares.append(i**2)
    return squares

square_of_i = squares_of_numbers()
print(square_of_i)