import random

min = int(raw_input("What's your minimum?"))
max = int(raw_input("What's your maximum?"))

def get_guess():

    # Get initial guess
    guess = raw_input("\nI'm thinking of a number between " + str(min) + " and " + str(max) + ". What do you think it is?")

    # Assume it's not valid, until it's proven otherwise
    valid = False

    while valid != True:

        try:
            # Try and convert this number to an integer
            # If it fails, the exception will occur
            guess = int(guess)
        except Exception:
            # Exception was thrown when trying to convert to number,
            # Report the issue and ask again
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()

        # If they get here, it means the number must have been valid
        # Set valid to be true to break out of the while loop
        valid = True

    return guess



# Next, build a function named compare that accepts 2 numbers and returns a string
# high or low depending on whether the first number is greater or less than the second number.

def compare(first, second):
    if first > second:
        return 'Too high.'
    elif first < second:
        return 'Too low.'


# print compare(100,1)  # Expected: 'high'
# print compare(1,100)  # Expected: 'low'
# print compare(99,100) # Expected: 'low'

#Complete this game using a for loop, limiting the user to 5 guesses.
#After each failed message, print a message like this:
#Too [high/low]; you have [count] guesses left.
#If the user loses, i.e. they don't guess the secret number within 5 guesses, print a message like this:
#Sorry, you ran out of guesses. The correct number was [answer]

def play():
    guess_count = 0
    # Pick a secret number
    secret_number = random.randint(min, max)

    # When building your program, the following line will tell you what
    # the secret_number is; this will make it easier to test the game.
    # When done, remove or comment-out this line.
    print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))

    # Print message at the start the game
    #print("\nI'm thinking of a number between 1 and 100; what do you think it is?")

    # Get the player's initial guess
    guess = get_guess()

    # Keep prompting until they get it correct
    # For every failed attempt, print 'Too x. Guess again.' where x is either 'high' or 'low'
    while guess != secret_number:
        guess_count = guess_count + 1
        if guess_count < 5:
            print(compare(guess, secret_number) + ' You have ' + str(5 - guess_count) + ' guesses left.')
            guess = get_guess()
        if guess_count == 5:
            print('Sorry, you ran out of guesses. The correct number was ' + str(secret_number) + '.')

    if  guess == secret_number:
        guess_count = guess_count + 1
        print('You got it! The number was ' + str(secret_number) + '. It took you ' + str(guess_count) + ' guesses.')

# Run the game
play()
