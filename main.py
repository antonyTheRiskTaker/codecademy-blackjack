'''Blackjack, inspired by Al Sweigart al@inventwithpython.com
Also known as 21 (This version doesn't have splitting or insurance.)'''

import random, sys

# Set up the constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'

def main():
    print('''Blackjack, inspired by Al Sweigart al@inventwithpython.com

    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase you bet
      but must hit exactly one more time before standing.
      In the case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.
    ''')

    # TODO: continue from here
    money = 5000
    while True: # Main game loop
        # Check if the player has run out of money:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

# If the programme is run (instead of imported), run the game:
if __name__ == '__main__':
    main()