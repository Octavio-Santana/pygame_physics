import sys
import random
import pygame

from player import Player
from wall import *

def exit_game():
    pygame.quit()
    sys.exit()

pygame.init()        
pygame.display.set_caption('Get to the red square!')
screen = pygame.display.set_mode((320, 240))

clock = pygame.time.Clock()

end_maze, walls = maze()
player = Player()

dx, dy = 0, 0
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit_game()

    dx, dy = player.controll()

    for wall in walls:
        if player.rect.colliderect(wall):
            player.collision(dx, dy, wall)

    if player.rect.colliderect(end_maze):
        print("You win!")
        raise SystemExit

    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_maze)        
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.display.flip()