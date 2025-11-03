# Write a program that calculates the total stock in a company from the array/list
# below if we know that the stock is the last digit in every array/list.
# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’],
# [‘coffee’,’5kshs’,’79’]]
# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS
# THE ABOVE LIST WILL GIVE YOU AN ERROR.

prods = [['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'],
         ['coffee','5kshs','79']]   

total_stock = 0
for product in prods:
    stock = int(product[-1])  # Get the last element which is the stock
    total_stock += stock
print(f"The total stock in the company is: {total_stock}")
