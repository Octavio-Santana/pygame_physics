import pygame, sys
from pygame.locals import *

from color import WHITE

pygame.init()
FPS = 30 # Frames por segundo
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

catImg = pygame.image.load('img/cat.png')
cat_posX = 10
cat_posY = 10
direction = 'right'

while True:
    DISPLAYSURF.fill(WHITE)
    if direction == 'right':
        cat_posX += 5
        if cat_posX == 280:
            direction = 'down'
    elif direction == 'down':
        cat_posY += 5
        if cat_posY == 220:
            direction = 'left'
    elif direction == 'left':
        cat_posX -= 5
        if cat_posX == 10:
            direction = 'up'
    elif direction == 'up':
        cat_posY -= 5
        if cat_posY == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (cat_posX, cat_posY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    fpsClock.tick(FPS)