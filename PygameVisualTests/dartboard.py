import pygame
import math
import numpy as np

SCALE_MM_TO_PIX = 2
BOARD_DIAMETER_MM = 340

BOARD_RADIUS = (BOARD_DIAMETER_MM / 2) * SCALE_MM_TO_PIX

points_arr = [20,1,18,4,13,6,10,15,2,17,3,19,7,16,8,11,14,9,12,5]

pygame.init()

FPS = 30
RES = (1000, 1000)
clock = pygame.time.Clock()
win = pygame.display.set_mode(RES)

X_OFFSET, Y_OFFSET = [i/2 for i in RES]

BLACK = (0,0,0)
RED = (150,10,10)
GREEN = (10, 150, 10)
GRAY = (200,200,200)
WHITE = (255,255,255)
BLUE = (10,60,250)
GOLD = (50,50,0)

board_img = []

def radialToCartesian(rad, angle):
    angle = math.radians(angle - 90)

    x = rad * math.cos(angle)
    y = rad * math.sin(angle)

    return (x,y)

def rotateAroundPoint(point, pivot, angle):
    angle = math.radians(angle)
    x1, y1 = point
    x2, y2 = pivot

    x_new = (x1-x2)*math.cos(angle) - (y1-y2)*math.sin(angle) + x2
    y_new = (x1-x2)*math.sin(angle) + (y1-y2)*math.cos(angle) + y2

    return (x_new, y_new)

def getPointsScored(hitPoint):
    xPos = hitPoint[0] - X_OFFSET
    yPos = (RES[1] - hitPoint[1]) - Y_OFFSET

    print(xPos, yPos)
    angle = (450 - math.degrees(math.atan2(yPos,xPos))) % 360

    print(angle)

def generateVerts(angle, numCurveVerts):
    verts = []
    verts.append([X_OFFSET, Y_OFFSET])
    for i in range(numCurveVerts):
        pass

def getDist(x, y):
    return math.sqrt(np.sum((x - X_OFFSET)**2 + (y - Y_OFFSET)**2))
    

def GenerateBoardImg():
    pixelArr = pygame.PixelArray(win)

    for i in range(RES[0]):
        for j in range(RES[1]):
            # print(i,j)
            if (getDist(i,j) > BOARD_RADIUS):
                pixelArr[i,j] = BLACK
            else:
                pixelArr[i,j] = GREEN
    print("through all")

    pixelArr.close()


def drawBoard():
    pygame.draw.circle(win, RED, (X_OFFSET, Y_OFFSET), BOARD_RADIUS)
    r = 400
    startAng = -9

    x, y = radialToCartesian(300,30)

    xStart = X_OFFSET + x
    yStart = Y_OFFSET + y


    pygame.draw.circle(win,BLUE,(xStart, yStart), 5)

    newPos = rotateAroundPoint((xStart, yStart), (X_OFFSET, Y_OFFSET), 90)

    pygame.draw.circle(win,BLUE, newPos, 5)

    for i in range(len(points_arr)):
        startAng = i*18 - 9
        verts = generateVerts(startAng)
        
        pass

def drawFrame(mPos):
    win.fill(BLACK)

    drawBoard()
    
    pygame.draw.line(win, WHITE, (X_OFFSET, 0), (X_OFFSET, RES[1]), 1)
    pygame.draw.line(win, WHITE, (0, Y_OFFSET), (RES[0], Y_OFFSET), 1)
    
    pygame.draw.line(win, GREEN, (X_OFFSET, Y_OFFSET), mPos, 2)



    pygame.display.update()

GenerateBoardImg()

running = True
while running:
    clock.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            getPointsScored(mouse_pos)
                    
    # drawFrame(mouse_pos)
    pygame.display.update()