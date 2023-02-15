import sys

def getBet(maxBet):
    '''Ask the player how much they want to bet for this round.'''
    while True: # Keep asking until they enter a valid amount.
        print(f'How much do you bet? (1-{maxBet}, or QUIT)')
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        
        if not bet.isdecimal():
            continue # If the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet # Player entered a valid bet.

if __name__ == '__main__':
    bet = getBet(5000)
    print('Betting', bet)