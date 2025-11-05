# Prompt the user for a number either on a form input or the terminal. Depending on whether 
# the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.

def divisible_numbers():
    a = float(input("Enter a number: "))

    if a % 2 == 0:
        if a % 4 == 0:
            a = "divisible by 4"
        else:
            a = "even"
    else:
        a = "odd"
    return a
result = divisible_numbers()
print(result)