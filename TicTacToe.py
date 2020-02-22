import numpy as np

dict_inv = {}
for i in range(9):
    dict_inv[i] = ' '

noWinner = True
num_turns = -1

taken_pos = []
all_pos = [1,2,3,4,5,6,7,8,9]

while noWinner:
    num_turns += 1
    if num_turns % 2 == 0:
        print('Player\'s Move.')
        move = int(input('Position 1-9:'))
        if len(taken_pos) > 1:
            for i in range(len(taken_pos)):
                if taken_pos[i] == move:
                    print('Taken!')
                    print('Player\'s New Move.')
                    print('The remaining positions are:', list((set(all_pos) | set(taken_pos)) - ((set(all_pos)) & set(taken_pos))))
                    move = int(input('Position 1-9:'))
                    if move in (list((set(all_pos) | set(taken_pos)) - ((set(all_pos)) & set(taken_pos)))):
                        print('Good move!')
                        print()
                        taken_pos.append(move)
        taken_pos.append(move)
        dict_inv[move-1] = 'X'
            
    else:
        print('Computer\'s Move.')
        move = np.random.randint(1,9)
        for i in range(len(taken_pos)):
            if taken_pos[i] == move:
                print('Computer\'s New Move.')
                remaining = list((set(all_pos) | set(taken_pos)) - ((set(all_pos)) & set(taken_pos)))
                index = np.random.randint(1,len(remaining))
                move = remaining[index]
        dict_inv[move-1] = 'O'
        taken_pos.append(move)
    
    values = dict_inv.values()
    array_of_board = np.array(list(values)).reshape(3,3)
    
    topRow = ((dict_inv[0] == dict_inv[1] == dict_inv[2]) & (dict_inv[0] != ' '))
    midRow = ((dict_inv[3] == dict_inv[4] == dict_inv[5]) & (dict_inv[3] != ' '))
    botRow = ((dict_inv[6] == dict_inv[7] == dict_inv[8]) & (dict_inv[6] != ' '))
    lCol = ((dict_inv[0] == dict_inv[3] == dict_inv[6]) & (dict_inv[0] != ' '))
    mCol = ((dict_inv[1] == dict_inv[4] == dict_inv[7]) & (dict_inv[1] != ' '))
    rCol = ((dict_inv[2] == dict_inv[5] == dict_inv[8]) & (dict_inv[2] != ' '))
    lrD = ((dict_inv[0] == dict_inv[4] == dict_inv[8]) & (dict_inv[0] != ' '))
    rlD = ((dict_inv[2] == dict_inv[4] == dict_inv[6]) & (dict_inv[2] != ' '))
    
    if (topRow | midRow | botRow | lCol | mCol | rCol | lrD | rlD) == True:
        if dict_inv[move-1] == 'X':
            print('Player, you won!')
            taken_pos = []
            for i in range(len(dict_inv)):
                dict_inv[i] = ' '
            values = dict_inv.values()
            array_of_board = np.array(list(values)).reshape(3,3)
            print()
            print()
            print('You may close the window if you are done playing!')
            input('If you wish to play again, press Enter!')
            num_turns = -1
            
        else:
            print('Player, the computer has won.')
            taken_pos = []
            for i in range(len(dict_inv)):
                dict_inv[i] = ' '
            values = dict_inv.values()
            array_of_board = np.array(list(values)).reshape(3,3)
            print()
            print()
            print('You may close the window if you are done playing!')
            input('If you wish to play again, press Enter!')
            num_turns = -1
    
    if num_turns != -1:
        print(array_of_board[0][0], '|', array_of_board[0][1], '|', array_of_board[0][2])
        print('--+---+--')
        print(array_of_board[1][0], '|', array_of_board[1][1], '|', array_of_board[1][2])
        print('--+---+--')
        print(array_of_board[2][0], '|', array_of_board[2][1], '|', array_of_board[2][2])
  
