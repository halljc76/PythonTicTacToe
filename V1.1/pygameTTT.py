#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
import numpy as np
from random import choice

import TicTacToeAI as computer
from button import Button
import images

pg.init()
pg.font.init()


# In[ ]:

"""
GLOBALS
"""

BOARD_WIDTH = 500
BUTTON_HEIGHT = 50

IMGBORDER = 25
RECTBORDER = 70
SPACING = 120

WIDTH = 775
HEIGHT = 500
FPS = 30

display = pg.display.set_mode([WIDTH, HEIGHT])
display.fill(pg.Color('white'))
pg.display.flip()

blue = (0, 0, 230)
red = (230, 0, 0)
green = (0, 230, 0)
black = pg.Color('black')
white = pg.Color('white')

tinyFont = pg.font.SysFont('comicsansms', 20)
smallFont = pg.font.SysFont('comicsansms', 25)
mediumFont = pg.font.SysFont('comicsansms', 30)
largeFont = pg.font.SysFont('comicsansms', 35)




def drawBoard(display, color):
    """
    Parameters 
    -----------
    display: pg.Surface
         - Game screen.
    color: tuple
         - Color for the lines.
    """
    
    
    display.fill(white)
    
    BORDER = 70
    SPACING = 120
    
    coords = [i for i in range(BORDER, BOARD_WIDTH, SPACING)]
    
    for coord in coords:
        pg.draw.line(display, color, (BORDER, coord), (BOARD_WIDTH - BORDER, coord))
        pg.draw.line(display, color, (coord, BORDER), (coord, BOARD_WIDTH - BORDER))
    
        
    pg.display.flip()


# In[ ]:


def imageCoordinates():
    
    coordValues = [i for i in range(RECTBORDER + IMGBORDER, BOARD_WIDTH - SPACING, SPACING)]
    imageCoords = []
    
    for coord in coordValues:
        for coord2 in coordValues:
            imageCoords.append((coord2, coord))
    
    imageCoords.append((WIDTH - 200, HEIGHT - 200))
    
    return imageCoords


def update(imageCoords, index, image):
    """
    Parameters
    ----------
    imageCoords: List
        - List of image coordinates that are referred to via index parameter.
    index: Integer
        - Parameter corresponding to move input.
    image: type(pg.image.load('imgname.png'))
        - Either the X or O.
    
    Returns
    ---------
    None, but updates the display to reflect necessary changes.
    """
    
    display.blit(image, (imageCoords[index][0], imageCoords[index][1]))
    pg.display.flip()


# In[ ]:


def reset():
    """
    Resets all values for the function within main() that carry heavy functionality.
    """
    numTurns = -1
    positions = [i for i in range(1,10)]
    takenPos = []
    remaining = sorted(list((set(positions) | set(takenPos)) -  ((set(positions)) & set(takenPos))))
    dict_inv = dict()
    for i in range(len(positions)):
        dict_inv[i] = ' '

    return numTurns, positions, takenPos, remaining, dict_inv


# In[ ]:


a = np.array([False, False, True])
np.argmax(a == True)


# In[ ]:


def text(surface, sizeFont, color, message, centerX, centerY):
        """
    
        Parameters
        ----------
        surface : pygame.Surface
            The Screen on which the game is played.
        sizeFont : pygame.font
            The font object that is displayed.
        color : tuple
            Global tuple object of R,G,B values.
        message : String
            Specific string to be displayed for the user.
        centerX : Integer
            x-coordinate of center of pygame.rect object.
        centerY : Integer
            y-coordinate of center of pygame.rect object.
    
        Returns
        -------
        Nothing returned; text object appears on pygame.Surface object.
    
        """
        
        text = sizeFont.render(message, True, color)
        rect = text.get_rect()
        rect.center = (centerX, centerY)
        surface.blit(text, rect)


# In[ ]:


def intro():
    display.fill(pg.Color('white'))
    
    text(display, mediumFont, black, 'Welcome to TicTacToe!', WIDTH // 2, HEIGHT // 4) 
    text(display, smallFont, black, 'Choose a difficulty... and good luck!', WIDTH // 2, HEIGHT // 2.5)
    
    easy = Button(display, blue, white,
                   (WIDTH // 2) - (BUTTON_HEIGHT * 4), HEIGHT * 2 // 3, BUTTON_HEIGHT * 2, BUTTON_HEIGHT, 'Easy!',
                   largeFont)
    hard = Button(display, red, white,
                 (WIDTH // 2) - (BUTTON_HEIGHT), HEIGHT * 2 // 3, BUTTON_HEIGHT * 2, BUTTON_HEIGHT, 'Hard!!',
                 largeFont)
    quit = Button(display, green, white,
                 (WIDTH // 2) + (BUTTON_HEIGHT * 2), HEIGHT * 2 // 3, BUTTON_HEIGHT * 2, BUTTON_HEIGHT, 'Quit.',
                 largeFont)
    pg.display.flip() 
    
    while True:
        if easy.checkUpdates():
            main(0)
        elif hard.checkUpdates():
            main(1)
        elif quit.checkUpdates():
            pg.quit()
       

        event = pg.event.get()

        for e in event:
            if e.type == pg.QUIT:
                pg.quit()

        pg.time.Clock().tick(FPS)


# In[ ]:


def main(index):
    '''
    Parameters
    -----------
    index: Integer
       - Determines which computer AI is chosen, the 'random' or 'algorithm'
    
    Returns
    --------
    None: Simply handles the entire game via a while loop.
    
    '''
    
    positions = [i for i in range(1,10)]
    takenPos = []
    remaining = sorted(list((set(positions) | set(takenPos)) -  ((set(positions)) & set(takenPos))))
    
    counts = [0] * 9
    drawBoard(display, black)
    imageCoords = imageCoordinates()
    
    dict_inv = dict()
    for i in range(len(positions)):
        dict_inv[i] = ' '
    
    numTurns = -1
    needAI = [False, True]
    
   
    
    replay = Button(display, blue, white, WIDTH - (BUTTON_HEIGHT * 4),
                    0, BUTTON_HEIGHT * 4, BUTTON_HEIGHT, 'Replay!',
                    smallFont)
    quit = Button(display, red, white,WIDTH - (BUTTON_HEIGHT * 4), 
                  BUTTON_HEIGHT, BUTTON_HEIGHT * 4, BUTTON_HEIGHT, 'Quit.',
                  smallFont)
    menu = Button(display, green, white,WIDTH - (BUTTON_HEIGHT * 4),
                  BUTTON_HEIGHT * 2, BUTTON_HEIGHT * 4, BUTTON_HEIGHT, 'Menu',
                  smallFont)
    
    update(imageCoords, -1, images.Board)
    
    pg.display.flip()
    
    while True:
        
        numTurns += 1 # Alternates players
        
        if numTurns % 2 == 0:
            moveMade = False
        
        
            while not moveMade:
                """
                A lot of the values that were used for different characteristics
                of the buttons were simply computed as needed. Future releases will
                likely shore this up to make it into SIMPLER invariants.
                """
                if replay.checkUpdates():
                    numTurns, positions, takenPos, remaining, dict_inv = reset()
                    drawBoard(display, pg.Color('black'))
                    replay = Button(display, blue, white, WIDTH - (BUTTON_HEIGHT * 4),
                    0, BUTTON_HEIGHT * 4, BUTTON_HEIGHT, 'Replay!',
                    smallFont)
                    quit = Button(display, red, white,WIDTH - (BUTTON_HEIGHT * 4), 
                                  BUTTON_HEIGHT, BUTTON_HEIGHT * 4, BUTTON_HEIGHT, 'Quit.',
                                  smallFont)
                    menu = Button(display, green, white,WIDTH - (BUTTON_HEIGHT * 4),
                                  BUTTON_HEIGHT * 2, BUTTON_HEIGHT * 4, BUTTON_HEIGHT, 'Menu',
                                  smallFont)
                    
                    pg.display.flip()
                    break
                    
                elif menu.checkUpdates():
                    
                    numTurns, positions, takenPos, remaining, dict_inv = reset()
                    intro()
                    
                    pg.display.flip()
                    break
                    
                if quit.checkUpdates():
                    pg.quit()
                
                e = pg.event.poll()
                pressed = pg.key.get_pressed()
                    
                inputs = pressed[pg.K_1:(pg.K_9 + 1)]
                
                
                
                for i in range(len(inputs)):
                    if inputs[i] == 1:
                        counts[i] += 1

                # Ensure only one player input is recorded
                inputMask = np.array(inputs) == max(inputs)
                numTrue = np.count_nonzero(inputMask) 

                while numTrue > 1:
                    counts[np.argmax(inputMask)] = 0
                    numTrue -= 1

                for j in range(len(counts)):
                    if (counts[j] == max(counts)) and (counts[j] > 0):
                        if positions[j] not in takenPos:
                            update(imageCoords, j, images.X)

                            takenPos.append(positions[j])
                            dict_inv[positions[j] - 1] = 'X'
                            

                            remaining = sorted(list((set(positions) | set(takenPos)) -  ((set(positions)) & set(takenPos))))
                            moveMade = True
                
                if e.type == pg.QUIT:
                    pg.quit()
                
                pg.time.Clock().tick(FPS)
                
            counts = [0] * 9
            
        else:
            
            if needAI[index]:
                defPos, defScore = computer.AIDefense(dict_inv, remaining)
                offPos, offScore = computer.AIOffense(dict_inv, remaining)

                move = computer.AIAlgorithm(defPos, offPos, defScore, offScore)

            elif not needAI[index]:
                move = choice(remaining)
                
            dict_inv[move - 1] = 'O'
            
            update(imageCoords, move - 1, images.O)
            
            takenPos.append(move)
            remaining = sorted(list((set(positions) | set(takenPos)) -  ((set(positions)) & set(takenPos))))
        
        e = pg.event.poll()
        pressed = pg.key.get_pressed()

        topRow = ((dict_inv[0] == dict_inv[1] == dict_inv[2]) & (dict_inv[0] != ' '))
        midRow = ((dict_inv[3] == dict_inv[4] == dict_inv[5]) & (dict_inv[3] != ' '))
        botRow = ((dict_inv[6] == dict_inv[7] == dict_inv[8]) & (dict_inv[6] != ' '))
        lCol = ((dict_inv[0] == dict_inv[3] == dict_inv[6]) & (dict_inv[0] != ' '))
        mCol = ((dict_inv[1] == dict_inv[4] == dict_inv[7]) & (dict_inv[1] != ' '))
        rCol = ((dict_inv[2] == dict_inv[5] == dict_inv[8]) & (dict_inv[2] != ' '))
        lrD = ((dict_inv[0] == dict_inv[4] == dict_inv[8]) & (dict_inv[0] != ' '))
        rlD = ((dict_inv[2] == dict_inv[4] == dict_inv[6]) & (dict_inv[2] != ' '))
        
        """
        Updates from the V1.0; this helped fix bugs encountered when correctly displaying who won.
        Note: These bugs were not present in V1.0, but where in using this for dev of V1.1.
        """
        winConds = np.array([topRow, midRow, botRow, lCol, mCol, rCol, lrD, rlD]) 
        ids = [dict_inv[0], dict_inv[3], dict_inv[6], dict_inv[0], dict_inv[1], dict_inv[2], dict_inv[0], dict_inv[2]]
        
        if (np.any(winConds)) == True:
            if ids[np.argmax(winConds == True)] == 'X':
                text(display, smallFont, black, 'You Won!', 500, 130)
                pg.display.flip()
                
                pg.time.delay(1500)
                intro()    
                    
            else:
                text(display, smallFont, black, 'You Lost!', 500, 250)
                pg.display.flip()
                
                pg.time.delay(1500)
                intro()

        else:
            if len(list(takenPos)) == 9:
                numTurns  = -1
                
                text(display, smallFont, black, 'Tie!', 500, 370)
                pg.display.flip()
                
                pg.time.delay(1500)
                intro()
        
        
        if e.type == pg.QUIT:
            pg.quit()
                
            
        pg.time.Clock().tick(FPS)

if __name__ == '__main__':
    intro()


# In[ ]:




