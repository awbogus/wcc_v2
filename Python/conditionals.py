temp = int(raw_input('What is the temperature?'))

print('You should bring the following items:')
if temp <= 40:
    print('Coat')
    print('Hat')
    print('Gloves')
elif temp <= 70:
    print('Coat')
    print('Hat')
else:
    print('Nothing!')

print('----')

# Update your tip calculator code to handle a case where the user does not type in an a, b, or c.
# For this additional case, it should:
# 1) Set the percentage to .20
# 2) print You did not enter a valid option, defaulting to 20%.

meal_price = float(raw_input('How much was your meal? '))
print('How would you rate the service? ')
print('a. Not so good')
print('b. Good')
print('c. Excellent!')
chosen_option = raw_input('Choose an option: ')

if chosen_option == 'a':
    percentage = .15
elif chosen_option == 'b':
    percentage = .18
elif chosen_option == 'c':
    percentage = .20
else:
    percentage = .20

tip = meal_price * percentage
total_price = meal_price + tip
if chosen_option != 'a' and chosen_option != 'b' and chosen_option != 'c':
    print('You did not enter a valid option, so we are defaulting your tip to 20%.')
print('You should tip $' + str(tip))
print('Your total cost would be $' + str(total_price))
