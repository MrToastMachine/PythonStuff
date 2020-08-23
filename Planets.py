import pygame
import math
pygame.init()

RES = (1920, 1080)
FPS = 60

win = pygame.display.set_mode(RES, pygame.FULLSCREEN)
clock = pygame.time.Clock()

white = (200,200,200)
black = (0,0,10)
yellow = (255,255,0)
green = (100,255,100)
red = (255,50,50)

class PlanetClass():
    planets = []

    def __init__(self, name, x, y, radius, colour, mass, velocity=[0,0]):
        self.name = name
        self.pos = [x,y]
        self.radius = radius
        self.colour = colour
        self.mass = mass
        self.velocity = velocity
        PlanetClass.planets.append(self)

    @classmethod
    def UpdateVelocity(cls):
        for planet in PlanetClass.planets:
            for other in PlanetClass.planets:
                if other is not planet:
                    sqrDist = (getDist(planet.pos, other.pos) ** 2) 
                    forceDir = getNormal(planet.pos, other.pos)
                    force = [x * gravConstant * other.mass / sqrDist for x in forceDir]
                    planet.velocity[0] += force[0]
                    planet.velocity[1] += force[1]

    @classmethod
    def UpdatePosition(cls):
        for planet in PlanetClass.planets:
            for i in range(len(planet.pos)):
                planet.pos[i] += int(round(planet.velocity[i], 0))

    @classmethod
    def drawPlanets(cls):
        for planet in PlanetClass.planets:
            pygame.draw.circle(win, planet.colour, planet.pos, planet.radius)



def getDist(posA, posB):
    return math.sqrt(((posA[0] - posB[0]) ** 2) + (posA[1] - posB[1]) ** 2)

def getNormal(posA, posB):
    vector = ((posB[0] - posA[0]), (posB[1] - posA[1]))
    mag = math.sqrt((vector[0] ** 2) + (vector[1] ** 2))
    normal = [x / mag for x in vector]
    return normal # Returns list

def drawFrame():
    win.fill(black)
    PlanetClass.UpdateVelocity()
    PlanetClass.UpdatePosition()

    PlanetClass.drawPlanets()
    pygame.display.update()

midX = int(win.get_width()/2)
midY = int(win.get_height()/2)

#PLANETS -->       (name,             x,    y, radius, colour,   mass, velocity)
sun   = PlanetClass("Sun",         midX,  midY,    30, yellow, 30000000)
earth = PlanetClass("Earth", midX - 200,  midY,    10,  green,    100, [0,  12])
mars  = PlanetClass("Mars",  midX - 300,  midY,     8,    red,     10, [0, -10])
moon  = PlanetClass("Moon",  midX - 220,  midY,     4,  white,      1, [2,  11])
gravConstant = 0.001

running = True
while(running):
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == 5:
            print("Click")

    keyPressed = pygame.key.get_pressed()
    if(keyPressed[pygame.K_ESCAPE]):
        running = False


    drawFrame()

pygame.quit()



"""
TO ADD:
+ Menu to right of window to add and edit planets
"""