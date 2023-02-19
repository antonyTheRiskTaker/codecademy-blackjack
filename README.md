# codecademy-blackjack
A blackjack project as part of the CS Career Path to showcase my Python skills.

## What did I expect to learn from building this project?
By building a blackjack game, I can apply the fundamental concepts of 
programming and practice writing clean, readable code.

## The walkthrough of the game
Since the purpose of this blackjack project is to learn some foundamental 
software development principles, I think it's not a bad idea to first explain 
how does the game work on a big picture perspective. Every time you run the game 
on the terminal, it prints a few lines detailing how to decide who wins the game 
or when does a draw take place, the values the cards are worth, and so on.

To keep the game simple, this programme only allows you to play against a computer-controlled dealer.

Once the game is run, it brings you into a main game loop. As long as no 
game-ending logic is triggered, the game continues. The first conditional checks 
if you have run out of cash to carry on playing. By default you have 5000 to 
play with at the start of the game. 

## Structure of the code
The code of the blackjack CLI game is made up of the following 
modules/functions:
1. `sys`
2. `print_game_info`
3. `getBet()`
4. `getDeck()`
5. `getHandValue()`
6. `displayHands()`
7. `getMove()`

## What does each of these modules/functions do?

### sys
For the context of this project, the module from the standard library is used to
exit the programme when conditions of certain scenarios in the game is met.

### print_game_info
The module contains several functions that simply print out game information
messages, so the code in the entry point `main.py` is made cleaner and easier
to navigate.

### `getBet()`
This function takes one input: the money the player has (5000 default). The code
inside asks the player for the amount he wants to bet for a round of blackjack
game. Checks are made to make sure the player doesn't enter anything other than
integers. It also prevents the player can't bet more than he has. Finally, the
function returns the amount of money he wants to bet for this round.

### `getDeck()`
It returns a list of 52 cards, each of them in the form of a tuple that has a
rank (i.e. ace, number cards from 2 to 10 inclusive, joker, queen and king) 
and its suit (club, diamond, heart and spade). Both values are strings. To make 
sure the deck is shuffled, `shuffle()` from the random module is used on the 
deck before returning it.

### `getHandValue()`
It takes in either a player's or a dealer's hand and returns the aggregated
value of a given hand of cards.