import time
from random import randint
import pygame, sys
from pygame.locals import *

from color import WHITE, BLACK

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

fontObj = pygame.font.Font('freesansbold.ttf', 32)
#textSurfaceObj = fontObj.render('Hello World', True, GREEN, BLUE)

soundObj = pygame.mixer.Sound('sound/beep.wav')
def sound():
    soundObj.play()
    time.sleep(1)
    soundObj.stop()

def random_color():
    return (randint(0,255), randint(0,255), randint(0,255))

while True:
    textSurfaceObj = fontObj.render('Hello World', True, BLACK, random_color())
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (200, 150)

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    sound()