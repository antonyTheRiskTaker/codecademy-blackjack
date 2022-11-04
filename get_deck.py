import random

# Set up the suit constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

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
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(suit), rank))  # Add the numbered cards.
        for rank in ('J', 'Q', 'A', 'K'):
            deck.append((rank, suit))  # Add the face and ace cards.
    random.shuffle(deck)
    return deck


if __name__ == '__main__':
    print(getDeck())
