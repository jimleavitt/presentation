#tetris variant
#based on tetromino by Al Sweigart al@inventwithpython.com

import random, time, pygame, sys
from pygame.locals import *

#define some constants
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

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
