# %%
import numpy as np
import cv2
import pygame
import random
import math

pygame.init()

def saveCurrentImage():
    saveFile = fileName.split('.')[0] + "_dotPainting.jpeg"
    print("Saving Image...")
    pygame.image.save(win, 'OutputImages/' + saveFile)
    print("Image Saved.")

def getRawImage(image_path):

    # Load the image 
    image = cv2.imread(image_path) 
    

    # Convert the image to grayscale 
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        
    RES = [x for x in reversed(image.shape[:2])]
    print(RES)
    return (image, RES)

def easeOutCirc(x):
    return math.sqrt(1 - math.pow(x - 1, 2));

imgFolder = "Images/"
# fileName = "mise.jpg"
fileName = "Flowers.JPG"
imgPath = imgFolder + fileName

img, RES = getRawImage(imgPath)

win = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

numPoints = 1000000
maxRad = 1000
minRad = 1

def drawFrame():
    win.fill((0,0,0))

    for i in range(numPoints):
        posX = random.randint(0, RES[0]-1)
        posY = random.randint(0, RES[1]-1)

        colorAtPixel = img[posY][posX][::-1]
        rad = (1 - easeOutCirc(i/numPoints)) * maxRad + minRad

        pygame.draw.circle(win, colorAtPixel, (posX, posY), rad)

        # pygame.display.update()

    pygame.display.update()


drawFrame()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            saveCurrentImage()
            pass
