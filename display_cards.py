import constants

def displayCards(cards):
    '''Display all the cards in the cards list.'''

    # The text to display on each row (a list of five empty strings)
    # The final empty character acts as a space separating the dealer's cards
    # and the player's cards.
    rows = ['' for _ in range(5)]
    
    for i, card in enumerate(cards):
        rows[0] += ' ___  ' # Print the top line of the card.
        if card == constants.BACKSIDE:
            # Print a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front:
            rank, suit = card # The card is a tuple data structure.
            rows[1] += f'|{rank.ljust(2)} | '
            rows[2] += f'| {suit} | '
            rows[3] += f'|_{rank.rjust(2, "_")}| '
    
    # Print each row on the screen:
    for row in rows:
        print(row)

if __name__ == '__main__':
    print(displayCards())