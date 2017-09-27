def isPositive(a):
    return a > 0
print isPositive(8)
print isPositive(-9)

def multiply(a, b):
    result = a * b
    return result

# Test the function:
solution = multiply(4, 5) # Invoke multiply giving it the arguments 4 and 5
print(solution) # Expected: 20

def cube(a):
    product = a * a * a
    return product

print('-----')

def mystery(x, y, z):
    mystery = x + y * z
    return mystery
print mystery('Hello', 3, '!') # Expected: 'Hello!!!'
print mystery('Goodbye', 2, '@') # Expected: 'Goodbye@@'

print('-----')

# Define a function called calculate_tip
#This function should take two parameters:
#1) Float: Price of the meal
# 2) String: Service rating A, B, or C
#The service rating should correspond to this tip amount:
#A = 20%
#B = 18%
#C = 15%
#The function should return how much tip should be left, taking into account the price of the meal and the service rating.


def calculate_tip(meal_price, service):
    if service == 'A':
        tip_percentage = 0.2
    elif service == 'B':
        tip_percentage = 0.18
    elif service == 'C':
        tip_percentage = 0.15
    calculate_tip = meal_price * tip_percentage
    return calculate_tip
print(calculate_tip(30.50, 'C')) # Expected: 4.575
print(calculate_tip(15.00, 'B')) # Expected: 2.7
print(calculate_tip(20.00, 'A')) # Expected: 4
