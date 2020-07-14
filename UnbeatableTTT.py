import numpy as np
import copy
from random import choice

def AIDefense(dict_inv, remaining):
    
    dict_inv2 = copy.copy(dict_inv)
    
    scores = []
    score = 0
    best_score = 0
    best = 0
    best_pos = []
    
    for pos in remaining:
        if dict_inv2[pos-1] == ' ':
            dict_inv2[pos-1] = 'O'
            
    topRow = ((dict_inv2[0] == dict_inv2[1] == dict_inv2[2]) & (dict_inv2[0] != ' '))
    midRow = ((dict_inv2[3] == dict_inv2[4] == dict_inv2[5]) & (dict_inv2[3] != ' '))
    botRow = ((dict_inv2[6] == dict_inv2[7] == dict_inv2[8]) & (dict_inv2[6] != ' '))
    lCol = ((dict_inv2[0] == dict_inv2[3] == dict_inv2[6]) & (dict_inv2[0] != ' '))
    mCol = ((dict_inv2[1] == dict_inv2[4] == dict_inv2[7]) & (dict_inv2[1] != ' '))
    rCol = ((dict_inv2[2] == dict_inv2[5] == dict_inv2[8]) & (dict_inv2[2] != ' '))
    lrD = ((dict_inv2[0] == dict_inv2[4] == dict_inv2[8]) & (dict_inv2[0] != ' '))
    rlD = ((dict_inv2[2] == dict_inv2[4] == dict_inv2[6]) & (dict_inv2[2] != ' '))
     
    for pos in remaining:
        if (pos-1) == 0:
            if (dict_inv2[pos] == 'X') and (dict_inv2[pos+1] == 'X'):
                score += 5
            if (dict_inv2[pos+2] == 'X') and (dict_inv2[pos+5] == 'X'):
                score += 5
            if (dict_inv2[pos+3] == 'X') and (dict_inv2[pos+7] == 'X'):    
                score += 5
            if (dict_inv2[pos+1] == 'X') and (dict_inv[pos+2] == 'X'):
                score += 5
            if (dict_inv2[pos] == 'X') and (dict_inv[pos+2] == 'X'):
                score += 5
            if (dict_inv2[pos] == 'X') and (dict_inv2[pos+5] == 'X'):
                score += 5
            if score == 0:
                if dict_inv2[pos] == 'X':
                    score += 1
                if dict_inv2[pos+2] == 'X':
                    score += 1
                if dict_inv2[pos+3] == 'X':
                    score += 1
                if dict_inv2[pos+1] == 'X':
                    score += 1
                if dict_inv2[pos+5] == 'X':
                    score += 1
                if dict_inv2[pos+7] == 'X':
                    score += 1
            score += np.count_nonzero([topRow, lCol, lrD])
            scores.append(score)
            score = 0
        if (pos-1) == 1:
            if (dict_inv2[pos] == 'X') and (dict_inv2[pos-2] == 'X'):
                score += 6
            if (dict_inv2[pos+2] == 'X') and (dict_inv2[pos+5] == 'X'):
                score += 7
            if (dict_inv2[pos] == 'X') and (dict_inv2[pos+4] == 'X'):
                score += 8
            if (dict_inv2[pos-2] == 'X') and (dict_inv2[pos+6] == 'X'):
                score += 8
            if score == 0:
                if dict_inv2[pos-2] == 'X':
                    score += 1
                if dict_inv2[pos] == 'X':
                    score += 1
                if dict_inv2[pos+2] == 'X':
                    score += 1
                if dict_inv2[pos+5] == 'X':
                    score += 1
            score += np.count_nonzero([topRow, mCol])
            scores.append(score)
            score = 0
        if (pos-1) == 2:
            if (dict_inv2[pos-2] == 'X') and (dict_inv2[pos-3] == 'X'):
                score += 5
            if (dict_inv2[pos+1] == 'X') and (dict_inv2[pos+3] == 'X'):
                score += 5
            if (dict_inv2[pos+2] == 'X') and (dict_inv2[pos+5] == 'X'):
                score += 5
            if (dict_inv2[pos-3] == 'X') and (dict_inv[pos+2] == 'X'):
                score += 5
            if (dict_inv2[pos-2] == 'X') and (dict_inv[pos+2] == 'X'):
                score += 5
            if (dict_inv2[pos-2] == 'X') and (dict_inv2[pos+5] == 'X'):
                score += 5
            if score == 0:
                if dict_inv2[pos-3] == 'X':
                    score += 1
                if dict_inv2[pos-2] == 'X':
                    score += 1
                if dict_inv2[pos+2] == 'X':
                    score += 1
                if dict_inv2[pos+1] == 'X':
                    score += 1
                if dict_inv2[pos+3] == 'X':
                    score += 1
                if dict_inv[pos+5]  == 'X':
                    score += 1
            score += np.count_nonzero([topRow, rCol, rlD])
            scores.append(score)
            score = 0
        if (pos-1) == 3:
            if (dict_inv2[pos] == 'X') and (dict_inv2[pos+1] == 'X'):
                score += 7
            if (dict_inv2[pos-4] == 'X') and (dict_inv2[pos+2] == 'X'):
                score += 6
            if (dict_inv2[pos-4] == 'X') and (dict_inv2[pos+4] == 'X'):
                score += 8
            if (dict_inv2[pos+2] == 'X') and (dict_inv2[pos-2] == 'X'):
                score += 8
            if score == 0:
                if dict_inv2[pos-4] == 'X':
                    score += 1
                if dict_inv2[pos+2] == 'X':
                    score += 1
                if dict_inv2[pos] == 'X':
                    score += 1
                if dict_inv2[pos+1] == 'X':
                    score += 1
            score += np.count_nonzero([midRow, lCol])
            scores.append(score)
            score = 0
        if (pos-1) == 4:
            for i in range(len(dict_inv2)):
                if dict_inv2[i] == 'X':
                    score += 2
            score += np.count_nonzero([midRow, mCol, lrD, rlD])
            scores.append(score)
            score = 0
        if (pos-1) == 5:
            if (dict_inv2[pos-2] == 'X') and (dict_inv2[pos-3] == 'X'):
                score += 7
            if (dict_inv2[pos+2] == 'X') and (dict_inv2[pos-4] == 'X'):
                score += 6
            if (dict_inv2[pos-4] == 'X') and (dict_inv2[pos] == 'X'):
                score += 8
            if (dict_inv2[pos+2] == 'X') and (dict_inv2[pos-6] == 'X'):
                score += 8
            if score == 0:
                if dict_inv2[pos-2] == 'X':
                    score += 1
                if dict_inv2[pos-4] == 'X':
                    score += 1
                if dict_inv2[pos+2] == 'X':
                    score += 1
                if dict_inv2[pos-3] == 'X':
                    score += 1
            score += np.count_nonzero([midRow, rCol])
            scores.append(score)
            score = 0
        if (pos-1) == 6:
            if (dict_inv2[pos-4] == 'X') and (dict_inv2[pos-7] == 'X'):
                score += 5
            if (dict_inv2[pos] == 'X') and (dict_inv2[pos+1] == 'X'):
                score += 5
            if (dict_inv2[pos-3] == 'X') and (dict_inv2[pos-5] == 'X'):
                score += 5
            if (dict_inv2[pos+1] == 'X') and (dict_inv[pos-4] == 'X'):
                score += 5
            if (dict_inv2[pos] == 'X') and (dict_inv[pos-4] == 'X'):
                score += 5
            if (dict_inv2[pos] == 'X') and (dict_inv2[pos-7] == 'X'):
                score += 5
            if score == 0:
                if dict_inv2[pos-4] == 'X':
                    score += 1
                if dict_inv2[pos] == 'X':
                    score += 1
                if dict_inv2[pos-3] == 'X':
                    score += 1
                if dict_inv2[pos-7] == 'X':
                    score += 1
                if dict_inv2[pos-5] == 'X':
                    score += 1
                if dict_inv2[pos+1] == 'X':
                    score += 1
            score += np.count_nonzero([botRow, lCol, rlD])
            scores.append(score)
            score = 0
        if (pos-1) == 7:
            if (dict_inv2[pos-2] == 'X') and (dict_inv2[pos] == 'X'):
                score += 7
            if (dict_inv2[pos-4] == 'X') and (dict_inv2[pos-7] == 'X'):
                score += 6
            if (dict_inv2[pos] == 'X') and (dict_inv2[pos-8] == 'X'):
                score += 8
            if (dict_inv2[pos-2] == 'X') and (dict_inv2[pos-6] == 'X'):
                score += 8
            if score == 0:
                if dict_inv2[pos-2] == 'X':
                    score += 1
                if dict_inv2[pos] == 'X':
                    score += 1
                if dict_inv2[pos-4] == 'X':
                    score += 1
                if dict_inv2[pos-7] == 'X':
                    score += 1
            score += np.count_nonzero([botRow, mCol])
            scores.append(score)
            score = 0
        if (pos-1) == 8:
            if (dict_inv2[pos-2] == 'X') and (dict_inv2[pos-3] == 'X'):
                score += 5
            if (dict_inv2[pos-4] == 'X') and (dict_inv2[pos-7] == 'X'):
                score += 5
            if (dict_inv2[pos-9] == 'X') and (dict_inv2[pos-5] == 'X'):
                score += 5
            if (dict_inv2[pos-3] == 'X') and (dict_inv2[pos-4] == 'X'):
                score += 5
            if (dict_inv2[pos-2] == 'X') and (dict_inv2[pos-4] == 'X'):
                score += 5
            if (dict_inv2[pos-2] == 'X') and (dict_inv2[pos-7] == 'X'):
                score += 5
            if score == 0:
                if dict_inv2[pos-2] == 'X':
                    score += 1
                if dict_inv2[pos-4] == 'X':
                    score += 1
                if dict_inv2[pos-5] == 'X':
                    score += 1
                if dict_inv2[pos-3] == 'X':
                    score += 1
                if dict_inv2[pos-7] == 'X':
                    score += 1
                if dict_inv2[pos-9] == 'X':
                    score += 1
            score += np.count_nonzero([botRow, rCol, lrD])
            scores.append(score)
            score = 0
        # print(scores)
    for j in range(len(scores)):
        if scores[j] == max(scores):
            best_pos.append(remaining[j])
            best_score = scores[j]
    
    if len(best_pos) > 1:
        best = choice(best_pos)
    else:
        best = best_pos[0]
    
    return best, best_score


# In[3]:


def AIOffense(dict_inv, remaining):

    dict_inv3 = copy.copy(dict_inv)
    
    scores = []
    score = 0
    best_score = 0
    best = 0
    best_pos = []
    
    topRowL = ((dict_inv3[0] == dict_inv3[1]) & (dict_inv3[0] == 'O'))
    topRowR = ((dict_inv3[1] == dict_inv3[2]) & (dict_inv3[1] == 'O'))
    topRowS = ((dict_inv3[0] == dict_inv3[2]) & (dict_inv3[0] == 'O'))
    midRowL = ((dict_inv3[3] == dict_inv3[4]) & (dict_inv3[3] == 'O'))
    midRowR = ((dict_inv3[4] == dict_inv3[5]) & (dict_inv3[4] == 'O'))
    midRowS = ((dict_inv3[3] == dict_inv3[5]) & (dict_inv3[3] == 'O'))
    botRowL = ((dict_inv3[6] == dict_inv3[7]) & (dict_inv3[6] == 'O'))
    botRowR = ((dict_inv3[7] == dict_inv3[8]) & (dict_inv3[7] == 'O'))
    botRowS = ((dict_inv3[6] == dict_inv3[8]) & (dict_inv3[6] == 'O'))
    LColT = ((dict_inv3[0] == dict_inv3[3]) & (dict_inv3[0] == 'O'))
    LColB = ((dict_inv3[3] == dict_inv3[6]) & (dict_inv3[3] == 'O'))
    LColS = ((dict_inv3[0] == dict_inv3[6]) & (dict_inv3[0] == 'O'))
    midColT = ((dict_inv3[1] == dict_inv3[4]) & (dict_inv3[1] == 'O'))
    midColB = ((dict_inv3[4] == dict_inv3[7]) & (dict_inv3[4] == 'O'))
    midColS = ((dict_inv3[1] == dict_inv3[7]) & (dict_inv3[1] == 'O'))
    RColT = ((dict_inv3[2] == dict_inv3[5]) & (dict_inv3[2] == 'O'))
    RColB = ((dict_inv3[5] == dict_inv3[8]) & (dict_inv3[5] == 'O'))
    RColS = ((dict_inv3[2] == dict_inv3[8]) & (dict_inv3[2] == 'O'))
    LRD1 = ((dict_inv3[0] == dict_inv3[4]) & (dict_inv3[0] == 'O'))
    LRD2 = ((dict_inv3[4] == dict_inv3[8]) & (dict_inv3[4] == 'O'))
    LRD3 = ((dict_inv3[0] == dict_inv3[8]) & (dict_inv3[0] == 'O'))
    RLD1 = ((dict_inv3[2] == dict_inv3[4]) & (dict_inv3[2] == 'O'))
    RLD2 = ((dict_inv3[4] == dict_inv3[6]) & (dict_inv3[4] == 'O'))
    RLD3 = ((dict_inv3[2] == dict_inv3[6]) & (dict_inv3[2] == 'O'))
    
    
    dict_inv4 = {}
    positions = [1,2,3,4,5,6,7,8,9]
    
    dict_inv4[0] = np.count_nonzero([topRowR, LColB, LRD2])
    dict_inv4[1] = np.count_nonzero([topRowS, midColB])
    dict_inv4[2] = np.count_nonzero([topRowL, RColB, RLD2])
    dict_inv4[3] = np.count_nonzero([midRowR, LColS])
    dict_inv4[4] = np.count_nonzero([midRowS, midColS, LRD3, RLD3])
    dict_inv4[5] = np.count_nonzero([midRowL, RColS])
    dict_inv4[6] = np.count_nonzero([botRowR, LColT, RLD1])
    dict_inv4[7] = np.count_nonzero([botRowS, midColT])
    dict_inv4[8] = np.count_nonzero([botRowL, RColT, LRD1])
    
    
    values = list(dict_inv4.values())
    for i in range(len(values)):
        if values[i] >= 1:
            if positions[i] in remaining:
                score += 100
                scores.append(score)
                score = 0
        else:
            if positions[i] in remaining:
                score = 0
                scores.append(score)

    
    if max(scores) == 0:
        return AIDefense(dict_inv, remaining)
    
    for j in range(len(scores)):
        if scores[j] == max(scores):
            best_pos.append(remaining[j])
            best_score = scores[j]
    
    if len(best_pos) > 1:
        best = choice(best_pos)
    else:
        best = best_pos[0]
    
    return best, best_score 


# In[4]:


def AIAlgorithm(defense, offense, d_score, o_score, remaining):
    position = 0
    if d_score > o_score:
        position = defense
    if o_score > d_score:
        position = offense
    elif o_score == d_score:
        position = defense
    return position


# In[5]:


def main():
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
            print('Player\'s (X) Move.')
            move = int(input('Position 1-9:'))
            if len(taken_pos) > 1:
                for i in range(len(taken_pos)):
                    if taken_pos[i] == move:
                        remaining = sorted(list((set(all_pos) | set(taken_pos)) - ((set(all_pos)) & set(taken_pos)))) 
                        
                        print('Taken!')
                        print('Player\'s (X) New Move.')
                        print('The remaining positions are:', remaining)
                        move = int(input('Position 1-9:'))
                        if move in remaining:
                            print('Good move!')
                            print()
                            taken_pos.append(move)
                        else:
                            print('You still chose a taken space.')
                            
                            move = remaining[np.random.randint(1, len(remaining))]
                            print('Making random move... ', move)
            taken_pos.append(move)
            remaining = sorted(list((set(all_pos) | set(taken_pos)) - ((set(all_pos)) & set(taken_pos))))    
            dict_inv[move-1] = 'X'

        else:
            print('Computer\'s (O) Move.')
            defense, d_score = AIDefense(dict_inv, remaining)
            offense, o_score = AIOffense(dict_inv, remaining)
               
            move = AIAlgorithm(defense, offense, d_score, o_score, remaining)
            dict_inv[move-1] = 'O'
            taken_pos.append(move)
            remaining = sorted(list((set(all_pos) | set(taken_pos)) - ((set(all_pos)) & set(taken_pos))))

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
                print('You may close the window if you are done playing!')
                input('If you wish to play again, press Enter!')
                num_turns = -1

        else:
            if len(list(set(taken_pos))) == 9:
                print(array_of_board[0][0], '|', array_of_board[0][1], '|', array_of_board[0][2])
                print('--+---+--')
                print(array_of_board[1][0], '|', array_of_board[1][1], '|', array_of_board[1][2])
                print('--+---+--')
                print(array_of_board[2][0], '|', array_of_board[2][1], '|', array_of_board[2][2])

                print('You and the computer have tied!')
                input('If you wish to play again, press Enter!')
                dict_inv = {}
                for i in range(9):
                    dict_inv[i] = ' '

                num_turns = -1

                taken_pos = []
                all_pos = [1,2,3,4,5,6,7,8,9]
                remaining = list((set(all_pos) | set(taken_pos)) - ((set(all_pos)) & set(taken_pos)))   

        if num_turns != -1:
            print(array_of_board[0][0], '|', array_of_board[0][1], '|', array_of_board[0][2])
            print('--+---+--')
            print(array_of_board[1][0], '|', array_of_board[1][1], '|', array_of_board[1][2])
            print('--+---+--')
            print(array_of_board[2][0], '|', array_of_board[2][1], '|', array_of_board[2][2])


# In[ ]:

main()
