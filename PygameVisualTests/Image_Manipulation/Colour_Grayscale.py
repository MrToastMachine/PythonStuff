import cv2
import pygame
import time
import numpy as np
import math
import random

pygame.init()

TILE_SIZE = 10
imgPath = 'Images/mise.jpg'


def hexToRGB(h):
    hexVal = h.split('x')[1]

    return tuple(int(hexVal[i:i+2], 16) for i in (0, 2, 4))

WHITE = hexToRGB("0xFcFcFc")

CYAN = hexToRGB("0x4cc9f0")
PINK = hexToRGB("0xf72585")

BLUE = hexToRGB("0x2ec4b6")
GOLD = hexToRGB("0xff9f1c")

ORANGE = hexToRGB("0xf46036")
PURPLE = hexToRGB("0x2e294e")

SHADOWS = PINK
HIGHLIGHTS = CYAN

def remap_greyscale(inputColour, minColour, maxColour):

    minMaxDiff = [maxColour[i] - minColour[i] for i in range(3)]
    offset = [d*inputColour for d in minMaxDiff]



    return([minColour[i] + offset[i] for i in range(3)])

def remap(inputColour, minColour, maxColour):
    greyscale01 = (sum(inputColour) / len(inputColour)) / 255

    minMaxDiff = [maxColour[i] - minColour[i] for i in range(3)]
    offset = [d*greyscale01 for d in minMaxDiff]


    return([minColour[i] + offset[i] for i in range(3)])

def getGrayImage(image_path):

    # Load the image 
    image = cv2.imread(image_path) 
    

    # Convert the image to grayscale 
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    
    RES = [x for x in reversed(image.shape[:2])]
    print(RES)
    return (gray_image, RES)

def getRawImage(image_path):

    # Load the image 
    image = cv2.imread(image_path) 
    

    # Convert the image to grayscale 
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        
    RES = [x for x in reversed(image.shape[:2])]
    print(RES)
    return (image, RES)


img, RES = getGrayImage(imgPath)
# img, RES = getImage('landscape.jpg', 5)
print(img.min())

win = pygame.display.set_mode(RES)
clock = pygame.time.Clock()


def Colorize(image):
    for y, row in enumerate(image):
        for x, pixelVal in enumerate(row):
            
            col = remap_greyscale(pixelVal, SHADOWS, HIGHLIGHTS)
            win.set_at((x,y), col)

def AltColorize(image):
    for y, row in enumerate(image):
        for x, pixelVal in enumerate(row):
            
            gray01 = (pixelVal/255) 

            noise_val = (random.random()) # * (pixelVal / 255)


            # if noise_val < 0.95:
            if gray01 < 0.3:
                col = remap_greyscale(gray01,SHADOWS,WHITE)
            else:
                col = remap_greyscale(gray01,HIGHLIGHTS,WHITE)


            # col = remap_greyscale(pixelVal/255, PINK, CYAN)

            # col = remap(col, col, WHITE)
            win.set_at((x,y), col)
    

def drawFrame():

    win.fill((0,0,0))


    # for i in range(8):
    #     n = 8 - i
    #     print(f"{n}")
    #     QuantizeColours(img, n)

        # cv2.imshow("goop", img)
        # print(img)
        # pygame.draw.rect(win, , (0,0,blocksize,blocksize))

    AltColorize(img)

    pygame.display.update()

    # for i, row in enumerate(img):
    #     for num, tile in enumerate(row):
    #         win.fill(tile)
    #         time.sleep(2)
    #         pygame.display.update()


drawFrame()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # drawFrame()
        