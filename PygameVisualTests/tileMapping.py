import pygame
from tileMap import *

pygame.init()

FPS = 10
RES = (950, 700)
clock = pygame.time.Clock()
win = pygame.display.set_mode(RES, pygame.RESIZABLE)

BLACK = (0,0,0)
WHITE = (255,255,255)
GOLD = (100,100,0)
RED = (200,50,50)
GREEN = (50,200,50)
BLUE = (50,50,200)
GRAY = (50,50,50)

def drawFrame():
    win.fill(BLACK)

    tileMap.drawTiles()

    pygame.display.update()

# tileMap(win, grid_size, grid_pos_start, grid_pos_end, colour)
tile0 = tileMap(win, (20,20), (1,1), (20,2), GRAY)
tile1 = tileMap(win, (20,20), (1,19), (20,20), GRAY)
tile2 = tileMap(win, (20,20), (1,3), (3,18), GRAY)
tile3 = tileMap(win, (20,20), (15,3), (20,18), GRAY)
tile4 = tileMap(win, (20,20), (4,3), (14,18), GREEN)

tileMap.drawTiles()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                    
    drawFrame()