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

# print(deck)
# print(len(deck))