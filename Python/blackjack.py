import random

#                                        J   Q   K   A
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

# print(cards) # To see the list before being shuffled
# print(cards) # To see the list after being shuffled

print("Ladies and gentlemen, let's play blackjack!")

random.shuffle(cards)

# Round 1
player_card1 = cards.pop()
computer_card1 = cards.pop()

print('Your card: ' + str(player_card1))
print('Computer card:  ' + str(computer_card1))

# print(cards) # To see the list after two cards have been popped off.

# Round 2
decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

#Determine cards. User can type hit or stay. Computer will always hit.
if decision == 'h':
    player_card2 = cards.pop()
    computer_card2 = cards.pop()
else:
    player_card2 = 0
    computer_card2 = cards.pop()

print('Your cards: ' + str(player_card1)) + ', ' + str(player_card2)
print('Computer cards:  ' + str(computer_card1)) + ', ' + str(computer_card2)

# Round 3
decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

#Determine cards. Use can type hit or stay.
if decision == 'h':
    player_card3 = cards.pop()
else:
    player_card3 = 0
#Computer will only hit if first and second cards are less than 16.
if (computer_card1 + computer_card2) < 16:
    computer_card3 = cards.pop()
else:
    computer_card3 = 0

print('Your cards: ' + str(player_card1)) + ', ' + str(player_card2) + ', ' + str(player_card3)
print('Computer cards:  ' + str(computer_card1)) + ', ' + str(computer_card2) + ', ' + str(computer_card3)

#Determine game outcome. The winner is whoever's cards, when added together, come closest to 21, without going over.
# If both Player and Computer go over, or have an equal value of cards, it's a tie.
print('Game over and the winner is...')
player_card_total = player_card1 + player_card2 + player_card3
computer_card_total = computer_card1 + computer_card2 + computer_card3

if player_card_total <= 21 and (computer_card_total > 21 or computer_card_total < player_card_total):
    print('You win! You were closest to 21 without going over.')
elif computer_card_total <= 21 and (player_card_total > 21 or player_card_total < computer_card_total):
    print('Sorry dude. The computer won. The Machine was closest to 21 without going over.')
elif player_card_total > 21 and player_card_total == computer_card_total:
    print("It's a tie. You both exceeded 21.")
elif player_card_total < 21 and player_card_total == computer_card_total:
    print("It's a tie. You both succeessfully made it under 21 but landed on the same number.")
elif player_card_total > 21 and computer_card_total > 21:
    print ("It's a tie. You both exceeded 21.")
else:
    print('Sorry folks. I forgot a case and do not know who won. Woops!')
