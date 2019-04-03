import pygame

class Wall(object):
    def __init__(self, pos):        
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

level = [
"WWWWWWWWWWWWWWWWWWWW",
"W                  W",
"W         WWWWWW   W",
"W   WWWW       W   W",
"W   W        WWWW  W",
"W WWW  WWWW        W",
"W   W     W W      W",
"W   W     W   WWW WW",
"W   WWW WWW   W W  W",
"W     W   W   W W  W",
"WWW   W   WWWWW W  W",
"W W      WW        W",
"W W   WWWW   WWW   W",
"W     W    E   W   W",
"WWWWWWWWWWWWWWWWWWWW",
]

def maze():    
    # Percorra a lista string. 
    # W = wall , E = exit
    x, y = 0, 0
    walls = []
    for row in level:
        for col in row:
            if col == 'W':
                walls.append(Wall((x,y)))
            elif col == 'E':
                end_maze = pygame.Rect(x, y, 16,16)        
            x += 16
        y += 16
        x = 0
    return end_maze, walls