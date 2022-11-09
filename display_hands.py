import constants
from get_hand_value import getHandValue
from display_cards import displayCards

def displayHands(playerHand, dealerHand, showDealerHand):
    '''Show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False.'''
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        #* (Line below) list concatenation applied
        displayCards([constants.BACKSIDE] + dealerHand[1:])
    
    # Show the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)