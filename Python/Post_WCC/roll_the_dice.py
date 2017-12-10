import random

dice = [1, 2, 3, 4, 5, 6]


def next_step():
    next_action = raw_input("Do you want to play again? Answer yes or no.")
    next_action = next_action.lower()
    while next_action == "yes":
        random.shuffle(dice)
        print "You rolled " + str(dice.pop()) + "."
        next_action = raw_input("Do you want to play again? Answer yes or no.")
    if next_action == "no":
        print "Okay, have a nice day!"

def roll_dice():
    action = raw_input("Do you want to roll the dice? Answer yes or no.")
    action = action.lower()
    if action == "yes":
        random.shuffle(dice)
        print "You rolled " + str(dice.pop()) + "."
        next_step()
    if action == "no":
        print "Okay, have a nice day!"
    if action != "yes" and action != "no":
        action2 = raw_input("Sorry, I don't understand. Please answer yes or no.")
        action2 = action2.lower()
        if action2 == "yes":
            random.shuffle(dice)
            print "You rolled " + str(dice.pop()) + "."
        if action2 == "no":
            print "Okay, have a nice day!"
        if action2 != "yes" and action2 != "no":
            print "Sorry, I don't understand, and I'm out of energy."

roll_dice()
