import pygame
pygame.init()

RES = (500,500)
FPS = 60

win = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

#Colours
white = (250,250,250)
black = (10,10,10)
green = (10,250,10)
red = (250,10,10)

def drawFrame():
    win.fill(black)
    x, y = pygame.mouse.get_pos()
    print((x,y))
    textX = font.render(f"X: {x}", 1, white)
    textY = font.render(f"Y: {y}", 1, white)
    win.blit(textX, (5,5))
    win.blit(textY, (5,30))
    
    pygame.draw.line(win, green, (0,y),(RES[0],y), 1 )
    pygame.draw.line(win, red, (x,0),(x, RES[1]), 1 )
    
    pygame.display.update()
    
font = pygame.font.SysFont('corbel', 30 , True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    drawFrame()