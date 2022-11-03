class Card:
    '''
    This class creates an assemble of suits and values to represent a playing card.
    '''

    def __init__(self, suit, value, card_value):

        # Suit of the Card like Spades and Clubs
        self.suit = suit

        # Representing the value of the Card like 'A' for Ace, 'K' for King
        self.value = value

        # Score value for the Card like 10 for King
        self.card_value = card_value
