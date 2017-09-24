print(1 == 1)

print('----')

print(1 == 2) # Expected output: False

print(1 > 2) # Expected output: False

print(2 > 1) # Expected output: True

print(1 >= 1) # Expected output: True

print(2 == 2) # Expected output: True

print(2 != 2) # Expected output: False

print('----')

age = 30

print(age > 10) # Expected outcome: True

print(10 < age) # Expected outcome: True

print(age > 10 + 20) # Expected outcome: False

print(age + 20 > 10) # Expected outcome: True

print ('----')

print('a' > 'z') # Expected outcome: False

print('z' > 'a') # Expected outcome: True

print('apples' > 'oranges') # Expected outcome: False

print('oranges' > 'apples') # Expected outcome: True

print('cat' > 'car') # Expected outcome: True

print('car' > 'cat') # Expected outcome: False

print ('----')

age = 1
print(age > 12 and age < 19) # Expected outcome: False

age = 14
print(age > 12 and age < 19) # Expected outcome: True

age = 19
print(age > 12 and age < 19) # Expected outcome: False

age = 18
print(age > 12 and age < 19 and age != 5) # Expected outcome: True

age = 5
print(age > 12 and age < 19 and age != 5) # Expected outcome: False

age = -1
print(age > 12 and age < 19) # Expected outcome: False

age = 10
print(age > 25 and age < 15) # Expected outcome: False
# Could the above expression ever be True? If the 'and' changed to an 'or'

print ('----')

gesture = 'rock'
print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome: True

gesture = 'pape'
print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome: False

print ('----')

age = int(raw_input('How old are you?'))
print(age > 4 and age < 11) # Goal: To print true if age entered is between 5 and 10 (including those numbers)
print(age == 5 or age == 6 or age == 7 or age == 8 or age == 9 or age == 10)
print(4 < age < 11)
print(age <= 10 and age >= 5)

print ('----')
age = int(raw_input('How old are you?'))
print(age > 5 and age < 10) # Goal: To print true if age entered is between 5 and 10 (NOT including those numbers)
print(age == 6 or age == 7 or age == 8 or age == 9)
print(5 < age < 10)
