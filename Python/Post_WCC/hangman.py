word = ["g", "r", "a", "p", "e", "f", "r", "u", "i", "t"]
turns = 10

def start_game():
    counter = 0
    for letter in word:
        counter = counter + 1
    print("I'm thinking of a word with " + str(counter) + " letters: " + ("-" * counter))

start_game()

def guess_letter():
    global turns = turns - 1
    correct_guesses = []
    guess = raw_input("Guess a letter in the word.")
    guess = guess.lower()
    for index, letter in enumerate(word):
        if letter in guess:
            #print(str(guess))
            correct_guesses.insert(index, letter)
            place = str(index + 1)
            print("Your guess " + letter + " is in the following location in the word: " + str(place))
        #if letter not in guess:
            #print("-")
    print("You have guessed the following correct letters: " + str(correct_guesses) + " and you have " + str(turns) + " turns left.")
    next_move()

guess_letter()

def guess_word():
    guess = raw_input("Guess what the word is.")
    guess = guess.lower()
    global turns = turns - 1
    if guess == ''.join(word):
        print("Congratulations, you guessed the word!")
    else:
        print("Sorry, that's not the word.")
    next_move()



def next_move():
    if global turns > 0
        action = raw_input("Do you want to keep guessing letters or are you ready to guess the word? Enter 1 to guess a letter and 2 to guess a word.")
        if action == 1:
            guess_letter
        if action == 2:
            guess_word
    if global turns == 0:
        print("Sorry, you're out of guesses. Better luck next time.")
