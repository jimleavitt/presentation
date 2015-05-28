#tetris variant
#based on tetromino by Al Sweigart al@inventwithpython.com

import random, time, pygame, sys
from pygame.locals import *

#define some constants
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)

BORDERCOLOR = BLUE
BGCOLOR = BLACK
TEXTCOLOR = WHITE
TEXTSHADOWCOLOR = GRAY
COLORS      = (     BLUE,      GREEN,      RED,      YELLOW)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
assert len(COLORS) == len(LIGHTCOLORS) # each color must have light color


def main():
    global DISPLAYSURF
    #init pygame object
    pygame.init()

    #setup main window
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    #add text to the caption
    pygame.display.set_caption('Tetris')
    while True: # main game loop
        for event in pygame.event.get():
              if event.type == QUIT:
                 pygame.quit()
                 sys.exit()
        pygame.display.update()


main()
