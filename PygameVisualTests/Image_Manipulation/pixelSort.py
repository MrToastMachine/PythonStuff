# %%
import cv2
import pygame
import time
import numpy as np
import math
import random

pygame.init()

TILE_SIZE = 10
imgPath = 'Images/forest.jpg'
# imgPath = 'Images/frog.png'


def cvimage_to_pygame(image):
    """Convert cvimage into a pygame image"""
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1],
                                   "BGR")


def sortPixels(img):
    for i in range(3):
        pass



img = cv2.imread(imgPath)
shape = img.shape
img_h, img_w, _ = shape
img = np.array(img)


pg_img = cvimage_to_pygame(img)

npArr = np.array(img).reshape(shape)
npArr = npArr.swapaxes(0,1)

print(npArr.shape)

RES = (img_w*2,img_h)

win = pygame.display.set_mode(RES)
clock = pygame.time.Clock()



def drawFrame():

    win.fill((0,0,0))


    for i, col in enumerate(npArr):
        for j, pixel in enumerate(col):
            record = -1
            swapPos = j 
            brightness = sum(pixel) / 3
            if brightness > 200 or brightness < 0:
                continue
            for k in range(j, len(col)):
                testPixel = col[k]
                avg = sum(testPixel) / 3
                if avg > record:
                    record = avg
                    swapPos = k

            col[j] = col[swapPos]
            col[swapPos] = pixel

    npImg = cvimage_to_pygame(npArr.swapaxes(0,1))




    win.blit(pg_img,(0,0))
    win.blit(npImg, (img_w,0))
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
        
# %%
