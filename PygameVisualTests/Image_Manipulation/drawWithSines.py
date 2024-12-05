import cv2
import pygame
import numpy as np

pygame.init()

RES = (1000,1000)
FPS = 0.1

win = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

#Colours
WHITE = (250,250,250)
BLACK = (0,0,0)
GREEN = (10,250,10)
RED = (250,10,10)

y_offset = (RES[1]-20)/2

# DATA TO PLOT

blocksize = 20

min_amplitude = 0.001
max_amplitude = blocksize/2

x_axis = np.linspace(0,2*np.pi,blocksize)

scale = blocksize/x_axis[-1]
x_scaled = np.array([i * scale for i in x_axis])

def drawFunc():
    for i in range(1, len(y)):
        start_point = (x_scaled[i-1], y[i-1] + y_offset)
        end_point = (x_scaled[i], y[i] + y_offset)
        pygame.draw.line(win, WHITE, start_point, end_point,2)

def sineTests():
    
    for i in range(20):
        c = (i/20 * 255) / 255

        amp = c * max_amplitude
        freq = (i // 2) + 1
        print(freq)
        
        xStart = i * blocksize
        xVals = x_scaled + xStart
        yStart = round(blocksize/2)
        yVals = amp * np.sin(x * freq)

        for j in range(1, len(xVals)):
            
            # win.set_at((round(xVals[j]), yStart + round(yVals[j])), BLACK)
            start_point = (xVals[j-1], yVals[j-1] + yStart)
            end_point = (xVals[j], yVals[j] + yStart)
            pygame.draw.line(win, BLACK, start_point, end_point,2)

        

        # pygame.draw.rect(win, (c,c,c), (xStart,yStart,xStart+blocksize,blocksize))

def drawImgWithSines(image, darkness_levels = 5):
    for y, row in enumerate(image):
        for x, pixelVal in enumerate(row):
            strength = 255 - pixelVal

            amp = (strength/255) * max_amplitude
            freq = round((strength / 255) * darkness_levels)

            xStart = x * blocksize
            xVals = x_scaled + xStart
            yStart = (y*blocksize) + round(blocksize/2)
            yVals = amp * np.sin(x_axis * freq)

            for j in range(1, len(xVals)):
                
                # win.set_at((round(xVals[j]), yStart + round(yVals[j])), BLACK)
                start_point = (xVals[j-1], yVals[j-1] + yStart)
                end_point = (xVals[j], yVals[j] + yStart)
                pygame.draw.line(win, BLACK, start_point, end_point,2)


def drawFrame():
    global t
    global y

    win.fill(WHITE)
    # drawFunc()
    # sineTests()

    img = getImage('Images/images.jpg')
    drawImgWithSines(img)
    
    # pygame.draw.rect(win, , (0,0,blocksize,blocksize))
    
    pygame.display.update()

def getImage(image_path):
    low_res = (50,50)

    # Load the image 
    image = cv2.imread(image_path) 
        
    # Convert the image to grayscale 
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        
    return cv2.resize(gray_image, low_res)

drawFrame()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # drawFrame()