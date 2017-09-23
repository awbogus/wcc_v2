#name = raw_input('What is your name? ')
#print('Hi ' + name)

meal_price = raw_input('How much was your meal?')
tip = 0.2 * float(meal_price)
total_cost = float(meal_price) + float(tip)
print('You should tip $' + str(tip) + '.')
print('Your total cost would be $' + str(total_cost) + '.')
