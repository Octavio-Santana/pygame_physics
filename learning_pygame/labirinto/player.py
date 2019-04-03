import pygame

class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):
        # Move cada eixo separadamente
        if dx != 0:            
            self.rect.x += dx
        elif dy != 0:
            self.rect.y += dy
        #return dx, dy

    def collision(self, dx, dy, block):
        # Se colidir com algum bloco
        if dx > 0:
            self.rect.right = block.rect.left
        elif dx < 0:
            self.rect.left = block.rect.right
        if dy > 0:
            self.rect.bottom = block.rect.top
        elif dy < 0:
            self.rect.top = block.rect.bottom

    def controll(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.move(-2,0)
            return -2, 0
        if key[pygame.K_RIGHT]:
            self.move(2,0)
            return 2, 0
        if key[pygame.K_UP]:
            self.move(0,-2)
            return 0, -2
        if key[pygame.K_DOWN]:
            self.move(0,2)        
            return 0, 2
        else:
            return 0, 0                  
