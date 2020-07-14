# Welcome to TicTacToe, version 1.1!

This directory contains a 2D TicTacToe game using the pygame library that merges the two .py files in the root directory into one interface.
The user may choose which difficulty (random or algorithmic) they would like to play against.

The random is a slight improvement from the TicTacToe.py file in the root directory, trading np.random.randint for the random.choice module.
The algorithm is the same as that used in the .\UnbeatableTTT.py file.
The file button.py originates from my PygameSnake repository file of the same name.

The file pygameTTT.py is the base for the entire project. 

For the user:
- The 'replay' button allows you to start a new game, mid-game, if you made a move you did not intend to make.
- The 'quit' button allows you to exit the program.
- The 'menu' button allows you to return to the main menu.
- The keys 1-9 are valid commands for making moves in this game.
- At the end of each game, after a brief pause, the menu will appear.

