import pygame
import math

pygame.init()

FPS = 10
RES = (300,500)
clock = pygame.time.Clock()

win = pygame.display.set_mode(RES)
pygame.display.set_caption("Number Pad")

pink = (255,200,200)
teal = (10,100,110)
dark_teal = (0,30,40)
sand = (255,255,200)
magenta = (50,50,10)
white = (230,230,230)
black = (0,0,0)

class Button:
	buttons = []

	def __init__(self, x, y, number):
		self.x = x
		self.y = y
		self.radius = 20
		self.number = number
		Button.buttons.append(self)

	@classmethod
	def drawButtons(cls):
		for obj in cls.buttons:
			# pygame.draw.circle(win, sand, obj.centre, obj.radius)
			win.blit(buttonSprite, (obj.x-25, obj.y-25))
			text = buttonFont.render(obj.number, 1, magenta)
			win.blit(text, (obj.x-6, obj.y-13))

	@classmethod
	def checkClicked(cls):
		mousePos = pygame.mouse.get_pos()
		for obj in cls.buttons:
			dist = math.sqrt(((mousePos[0]-obj.x) ** 2) + (mousePos[1]-obj.y) ** 2)
			if(dist <= 25):
				print(f"Button {obj.number} clicked")
				obj.buttonClick()


	def buttonClick(self):
		textBox.value.append(self.number)

class textBox:
	def __init__(self, x, y, width, height, colour):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.colour = colour
		self.value = []

	def drawBox(self):
		pygame.draw.rect(win, self.colour, (self.x,self.y,self.width,self.height))
		content = ""
		for i in self.value:
			content += str(i)
		text = textBoxFont.render(content, 1, black)
		win.blit(text, (self.x + 5, self.y + 5))


def drawFrame():
	win.fill(dark_teal)

	textBox.drawBox()
	Button.drawButtons()
	# win.blit(backSprite, (320,125))

	pygame.display.update()

buttonSprite = pygame.image.load('Pictures/button.png')
backSprite = pygame.image.load('Pictures/backspace.png')
butt_1 = Button(50, 150, "1")
butt_2 = Button(150,150, "2")
butt_3 = Button(250,150, "3")
butt_4 = Button(50, 250, "4")
butt_5 = Button(150,250, "5")
butt_6 = Button(250,250, "6")
butt_7 = Button(50, 350, "7")
butt_8 = Button(150,350, "8")
butt_9 = Button(250,350, "9")
butt_0 = Button(150,450, "0")

textBox = textBox(25,40,250,50,white)

buttonFont = pygame.font.SysFont('bahnschrift', 20, False)
textBoxFont = pygame.font.SysFont('corbel', 35, True)
clicks = 0
running = True
while(running):
	clock.tick(FPS)

	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			running = False
		elif(event.type == pygame.MOUSEBUTTONDOWN):
			clicks += 1
			# print("Click")
			Button.checkClicked()

		keyPressed = pygame.key.get_pressed()
		if(keyPressed[pygame.K_BACKSPACE]):
			try:
				textBox.value.pop(len(textBox.value)-1)
			except:
				print("You can't do that idiot")
		elif(keyPressed[pygame.K_BACKSPACE]):
			textBox.value += str()

	drawFrame()


print("All done")


