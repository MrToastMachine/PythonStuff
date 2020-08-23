import noise
import numpy as np
import pygame
import random

pygame.init()

RES = (600,600)
FPS = 10

win = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

#COLOURS
lightGreen = (85,152,22)
darkGreen = (62,107,17)
lightBrown = (92,69,61)
darkBrown = (75,60,52)
blue = (51,99,195)
sand = (211,208,125)
black = (0,0,0)
white = (255,255,255)

world = np.zeros(RES)

scale = 100
octaves = 6
persistence = 0.5
lacunarity = 2.0

def getMapColour(height):
	if(height <= 0.5):
		return blue
	elif(height <= 0.55):
		return sand
	elif(height <= 0.65):
		return lightGreen
	elif(height <= 0.70):
		return darkGreen
	elif(height <= 0.80):
		return lightBrown
	elif(height <= 0.9):
		return darkBrown
	else:
		return white

def blueBoy(val):
	strength = round(255*val)
	return (0,0,strength)

def greyScale(val):
	strength = round(255 * val)
	return (strength, strength, strength)

def newMap():
	for i in range(RES[0]):
		for j in range(RES[1]):
			height = 0.5 + noise.pnoise2(i/scale, 
	                                	j/scale, 
	                                    octaves=octaves, 
	                                    persistence=persistence, 
	                                    lacunarity=lacunarity, 
	                                    repeatx=1024, 
	                                    repeaty=1024, 
	                                    base=0)
			grey = greyScale(height)
			blue = blueBoy(height)
			colour = getMapColour(height)
			pygame.draw.circle(win, colour, (i,j), 0)

	pygame.display.update()

newMap()
running = True
while running:
	clock.tick(FPS)
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			running = False
		elif(event.type == pygame.MOUSEBUTTONDOWN):
			print("Clicked")
			newMap()

pygame.quit()


print("Done")