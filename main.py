from card import Card
import card_value

# The deck of cards
deck = []

# (Lines below) logic to generate 52 playing cards

# Loop for every type of suit
for suit in card_value.suits:

    # Loop for every type of card in a suit
    for card in card_value.cards:

        # Adding card to the deck
        deck.append(Card(card_value.suits_values[suit], card, card_value.cards_values[card]))

# (Lines below) test if playing cards are properly created in the deck
# print(deck)
# print(len(deck))

def blackjack_game(deck):
    '''Function for a single game of blackjack'''
    global cards_values

    # Cards for both dealer and player
    player_cards = []
    dealer_cards = []

    # Scores for both dealer and player
    player_score = 0
    dealer_score = 0

    # Initial dealing for player and dealer
    while len(player_cards) < 2:

        # Randomly dealing a card
        # (Line below) choice method of the random library returns a random element from the deck list
        player_card = random.choice(deck)
        player_cards.append(player_card)
        # (Line below) .remove() method removes the first item of the value of the argument
        deck.remove(player_card)

        # TODO (Continue from here...)