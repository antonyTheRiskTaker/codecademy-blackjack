import random

import constants

#! Later we will try to rewrite the code applying OOP
# class Card:

#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank
    
#     def __repr__(self):
#         return str(vars(self))


def getDeck():
    '''Return a list of (rank, suit) tuples for all 52 cards.'''
    deck = []
    for suit in (constants.HEARTS, constants.DIAMONDS, constants.SPADES, constants.CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # Add the numbered cards.
        for rank in ('J', 'Q', 'A', 'K'):
            deck.append((rank, suit))  # Add the face and ace cards.
    random.shuffle(deck)
    return deck


if __name__ == '__main__':
    print(getDeck())
