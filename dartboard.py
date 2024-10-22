import pygame
import math
import numpy as np
from time import sleep

RING_WIDTH_MM = 8

SCALE_MM_TO_PIX = 2
BOARD_DIAMETER_MM = 340
BULLSEYE_RAD_MM = 6.35
RING_25_MAX_MM = 16
TRIPLE_INNER_MM = 99
DOUBLE_INNER_MM = 162


BOARD_RADIUS = (BOARD_DIAMETER_MM / 2) * SCALE_MM_TO_PIX

BULLSEYE_RAD_PX = BULLSEYE_RAD_MM * SCALE_MM_TO_PIX
RING_25_RAD_PX = RING_25_MAX_MM * SCALE_MM_TO_PIX
TRIPLE_INNER_PX = TRIPLE_INNER_MM * SCALE_MM_TO_PIX
DOUBLE_INNER_PX = DOUBLE_INNER_MM * SCALE_MM_TO_PIX
RING_WIDTH_PX = RING_WIDTH_MM * SCALE_MM_TO_PIX

points_arr = [20,1,18,4,13,6,10,15,2,17,3,19,7,16,8,11,14,9,12,5]

pygame.init()

FPS = 30
RES = (1000, 1000)
clock = pygame.time.Clock()
win = pygame.display.set_mode(RES, depth=32)

X_OFFSET, Y_OFFSET = [i/2 for i in RES]
CENTER = [X_OFFSET, Y_OFFSET]

BLACK = (0,0,0)
RED = (150,10,10)
GREEN = (10, 150, 10)
GRAY = (200,200,200)
WHITE = (255,255,255)
BLUE = (10,60,250)
GOLD = (50,50,0)
CREAM = (252,232,179)
CYAN = (0,200,200)


board_img = []

# create a 3D array with 30x30x3 (the last dimension is for the RGB color)
cells = np.ndarray((RES[0], RES[1], 3))

def getDist(x, y):
    return math.sqrt(np.sum((x - X_OFFSET)**2 + (y - Y_OFFSET)**2))
    
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

    angle = (459 - math.degrees(math.atan2(yPos,xPos))) % 360


    sector = round(angle // 18)
    points = points_arr[sector]

    points_scored = 0

    dist = getDist(hitPoint[0], hitPoint[1])
    if dist < BULLSEYE_RAD_PX:
        points_scored = 50
    elif dist < RING_25_RAD_PX:
        points_scored = 25
    elif TRIPLE_INNER_PX < dist < (TRIPLE_INNER_PX + RING_WIDTH_PX):
        points_scored = points * 3
    elif DOUBLE_INNER_PX < dist < (DOUBLE_INNER_PX + RING_WIDTH_PX):
        points_scored = points * 2
    elif dist < BOARD_RADIUS:
        points_scored = points
    else:
        points_scored = 0

    return sector, points_scored

def generateVerts(angle, numCurveVerts):
    verts = []
    verts.append([X_OFFSET, Y_OFFSET])
    for i in range(numCurveVerts):
        pass

def GenerateBoardImg():

    temp = np.ndarray((RES[0], RES[1], 3))

    print("starting board generation")
    for i in range(RES[0]):
        for j in range(RES[1]):
            sect, _ = getPointsScored((i,j))
            blackRed = sect % 2 == 0
            dist = getDist(i,j)
            if (dist > BOARD_RADIUS):
                temp[i][j] = BLACK
            else:
                if dist < BULLSEYE_RAD_PX:
                    temp[i][j] = RED
                elif dist < RING_25_RAD_PX:
                    temp[i][j] = GREEN
                elif TRIPLE_INNER_PX < dist < (TRIPLE_INNER_PX + RING_WIDTH_PX):
                    temp[i][j] = RED if blackRed else GREEN
                elif DOUBLE_INNER_PX < dist < (DOUBLE_INNER_PX + RING_WIDTH_PX):
                    temp[i][j] = RED if blackRed else GREEN
                else:
                    temp[i][j] = BLACK if blackRed else CREAM

            
    print("full img generated")

    return temp

def drawBoardImg(img):
    for i, column in enumerate(img):
        for j, colour in enumerate(column):
            win.set_at([i,j],colour)

def drawFrame(mPos):
    win.fill(BLACK)
    overlay.fill(BLACK)

    # drawBoardImg(img)
    win.blit(surf,(0,0))

    pygame.draw.circle(overlay, (0,200,200), mPos, 50)
    pygame.draw.line(win, WHITE, (X_OFFSET, Y_OFFSET), mPos,2)

    win.blit(overlay,(0,0))

    pygame.display.update()



img = GenerateBoardImg()

#create a surface with the size as the array
surf = pygame.Surface((img.shape[0], img.shape[1]))
 # draw the array onto the surface
pygame.surfarray.blit_array(surf, img)
# transform the surface to screen size
# surf = p.transform.scale(surf, (WIDTH, HEIGHT))

overlay = pygame.Surface(RES, depth=32)
overlay.set_alpha(100)

running = True
while running:
    clock.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("mouseClick")
            _, ass = getPointsScored(mouse_pos)
            print(f"Score: [{ass}]")
        elif event.type == pygame.K_SPACE:
            print("SPACEBAR")
                    
    drawFrame(mouse_pos)
    pygame.display.update()