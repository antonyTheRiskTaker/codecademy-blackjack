'''Blackjack, inspired by Al Sweigart al@inventwithpython.com
Also known as 21 (This version doesn't have splitting or insurance.)'''

import sys

import print_rules
from get_bet import getBet
from get_deck import getDeck
from get_hand_value import getHandValue
from display_hands import displayHands
from get_move import getMove

def main():
    print_rules.print_rules()    

    money = 5000
    while True: # Main game loop
        # Check if the player has run out of money:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()
        
        # Let the player enter their bet for this round:
        print('Money:', money)
        bet = getBet(money)

        # Give the dealer and player two cards from the deck each:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handle player actions:
        print('Bet:', bet)
        while True: # Keep looping until player stands or busts.
            displayHands(playerHand, dealerHand, False)
            print()

            # Check if the player has bust:
            if getHandValue(playerHand) > 21:
                break

            # Get the player's move, either H, S, or D:
            move = getMove(playerHand, money - bet)

            # Handle the player actions:
            if move == 'D':
                # Player is doubling down, they can increase their bet:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f'Bet increased to {bet}.')
                print(f'Bet:', bet)
            
            #* (Line below) equivalent of 
            #* `if move == 'H' or move == 'D'`
            if move in ('H', 'D'):
                # Hit/doubling down take another card.
                newCard = deck.pop()
                rank, suit = newCard
                print(f'You drew a {rank} of {suit}.')
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # The player has busted:
                    continue

            if move in ('S', 'D'):
                # Stand/doubling down stops the player's turn.
                break

        # Handle the dealer's actions:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) <= 17:
                # The dealer hits:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break # The dealer has busted.
                input('Press Enter to continue...')
                print('\n\n')

        # Show the final hands:
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # Handle whether the player won, lost, or tied:
        if dealerValue > 21:
            print(f'Dealer busts! You win ${bet}')
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print(f'You won ${bet}!')
            money += bet
        elif playerValue == dealerValue:
            print("It's a tie, the bet is returned to you.")
        
        input('Press Enter to continue...')
        print('\n\n')



# If the programme is run (instead of imported), run the game:
if __name__ == '__main__':
    main()