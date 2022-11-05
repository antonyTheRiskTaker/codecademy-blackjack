def getHandValue(cards):
    '''Returns the value of the cards. Face cards are worth 10, aces are worth 11 or 1 (this function picks the most suitable ace value).'''
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0] # card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'): # Face cards are worth 10 points.
            value += 10
        else:
            value += int(rank) # Numbered cards are worth their number
    
    # Add the value for the aces:
    value += numberOfAces # Add 1 per ace.
    for i in range(numberOfAces):
        #// If another 10 can be added with busting, do so:
        # If another 10 can be added without busting, do so:
        if value + 10 <= 21:
            value += 10
    
    return value