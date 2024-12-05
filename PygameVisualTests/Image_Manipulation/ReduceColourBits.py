import cv2
import pygame
import time
import numpy as np

pygame.init()

TILE_SIZE = 10

def getImage(image_path, pixel_size):

    # Load the image 
    image = cv2.imread(image_path) 
    
    v_res = round(len(image) / pixel_size)
    h_res = round(len(image[1]) / pixel_size)

    new_res = (h_res, v_res)

    # Convert the image to grayscale 
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        
    return (cv2.resize(image, (h_res, v_res)), new_res)


img, RES = getImage('Images/frog.png', 5)
# img, RES = getImage('landscape.jpg', 5)

RES = [TILE_SIZE * x for x in RES]


win = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

def QuantizeColours(image, n_bits):
    n_levels = (2 ** n_bits) - 1
    for y, row in enumerate(image):
        y *= TILE_SIZE
        for x, pixelVal in enumerate(row):
            
            BGR = pixelVal[::-1]

            new_col = [round(i/255 * n_levels)/n_levels * 255 for i in BGR]

            # new_col = [round(i/255 * n_levels) for i in pixelVal]
            x *= TILE_SIZE
            pygame.draw.rect(win, new_col, (x,y,TILE_SIZE,TILE_SIZE))

def lightenUp(colour, new_min):
    r,g,b = colour

    new_red = round((r / 255) * (255 - new_min) + new_min)
    new_green = round((g / 255) * (255 - new_min) + new_min)
    new_blue = round((b / 255) * (255 - new_min) + new_min)

    return (new_red, new_green, new_blue)

def Pastelize(image):
    for y, row in enumerate(image):
        y *= TILE_SIZE
        for x, pixelVal in enumerate(row):
            
            pixelVal = lightenUp(pixelVal, 150)

            BGR = pixelVal[::-1]

            # new_col = [round(i/255 * n_levels) for i in pixelVal]
            x *= TILE_SIZE
            pygame.draw.rect(win, BGR, (x,y,TILE_SIZE,TILE_SIZE))

def drawFrame():

    win.fill((0,0,0))


    # for i in range(8):
    #     n = 8 - i
    #     print(f"{n}")
    #     QuantizeColours(img, n)

        # cv2.imshow("goop", img)
        # print(img)
        # pygame.draw.rect(win, , (0,0,blocksize,blocksize))

    Pastelize(img)

    pygame.display.update()

    # for i, row in enumerate(img):
    #     for num, tile in enumerate(row):
    #         win.fill(tile)
    #         time.sleep(2)
    #         pygame.display.update()


# drawFrame()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drawFrame()
        