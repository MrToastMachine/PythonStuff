import pygame
from tileMap import *

pygame.init()

FPS = 30
RES = (950, 700)
clock = pygame.time.Clock()
win = pygame.display.set_mode(RES)

BLACK = (0,0,0)
WHITE = (255,255,255)
GOLD = (50,50,0)

def drawFrame():
    win.fill(BLACK)

tile0 = tileMap(win, (4,3), (1,1), (2,3), GOLD)
tile1 = tileMap(win, (4,3), (1,1), (2,3), GOLD)
tile2 = tileMap(win, (4,3), (1,1), (2,3), GOLD)
tile3 = tileMap(win, (4,3), (1,1), (2,3), GOLD)

tileMap.drawTiles()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                    
    drawFrame()