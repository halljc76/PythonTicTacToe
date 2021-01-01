## Note: This somehow does not work in Pygame's newest version; I'll have to rework this in the future!

Welcome to the Classic Game TicTacToe!

You may choose from one of two difficulties to play:
- The TicTacToe file is simply you against a CPU who makes random moves, 
whether they be intelligent or not.
- The UnbeatableTTT file is a supercharged variant of TicTacToe where the CPU does not 
make any faulty move. Thus, every game is either the CPU winning or a tie! 

UnbeatableTTT Testing Process:
- The testing process for the developed AI was rather rudimentary, consisting of a 2,000,000-game simulation divided between the AI playing against a solely random CPU (started at ~90.3% win-rate, debugging yielded a 100% win-rate) and two AI-based players competing (started at ~95.2% tie rate, debugging yielded a 100% tie-rate). 
- Over 100 games, the average move time for an AI-driven player was ~0.0002 seconds. This AI is not a replica or direct deployment of the concepts of Minimax, though the axioms of Minimax trees directed ideas for the implemented algorithm's structure.

Baseline Understanding of UnbeatableTTT AI:
- Just as a Minimax tree desires the minimum score for a particular scenario controlled by variables (players) A and B, a similar idea is imported here.

Upon each turn, the board is parameterized via a dictionary into the Defense and Offense functions for the AI, which evaluate the effectiveness of placing a token on a particular piece through careful reference to the dictionary. Next, an Algorithm function chooses which advice to follow (Offense or Defense) through comparison of the best positions reported from each function.
