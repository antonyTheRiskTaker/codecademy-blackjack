# codecademy-blackjack
A blackjack project as part of the CS Career Path to showcase my Python skills.

## What did I expect to learn from building this project?
By building a blackjack game, I can apply the fundamental concepts of programming and practice writing clean, readable code.

## The walkthrough of the game
Since the purpose of this blackjack project is to learn some foundamental software development principles, I think it's not a bad idea to first explain how does the game work on a big picture perspective. Every time you run the game on the terminal, it prints a few lines detailing how to decide who wins the game or when does a draw take place, the values the cards are worth, and so on.

To keep the game simple, this programme only allows you to play against a computer-controlled dealer.

Once the game is run, it brings you into a main game loop. As long as no game-ending logic is triggered, the game continues. The first conditional checks if you have run out of cash to carry on playing. By default you have 5000 to play with at the start of the game. 

## Structure of the code
The code of the blackjack CLI game is made up of the following modules/functions:
1. `print_game_info`
2. `getBet()`
3. `getDeck()`
4. `getHandValue()`
5. `displayHands()`
6. `getMove()`