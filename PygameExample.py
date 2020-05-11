import pygame
# import DotClass

pygame.init()

FPS = 60
RESOLUTION = (800,600)
clock = pygame.time.Clock()

window = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("This is the title BOIII")

pink = (255,200,200)

class Player:
	def __init__(self,x,y,width,height,colour):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.velocity = 9
		self.colour = colour
		self.isJump = False
		self.jumpForce = 10
		self.maxJump = 10
		self.hitbox = (self.x, self.y, self.width, self.height)

	def draw(self, win, fill=True):
		if(fill):
			pygame.draw.rect(window, self.colour, (self.x,self.y,self.width,self.height))
		else:
			pygame.draw.rect(window, self.colour, (self.x,self.y,self.width,self.height), 3)

		self.hitbox = (self.x, self.y, self.width, self.height)
		# pygame.draw.rect(window, (255,0,0), self.hitbox, 2)

class Block:
	def __init__(self, x, y, width, height, colour=(255,255,255)):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.colour = colour
		self.hitbox = (self.x, self.y, self.width. self.height)


def drawFrame():

	window.fill((10,100,110))
	guy.draw(window, fill)

	mPos = mouseFont.render(str(mousePos), 1, pink)
	window.blit(mPos, (5,5))
	if 10 > clicks >= 5:
		text = font.render("Dead Babies", 1, pink)
		window.blit(text, (100, 30))
	elif clicks >= 10:
		text = font.render("Even more Dead Babies", 1, pink)
		window.blit(text, (100, 30))

	pygame.display.update()

def getDist(pointA, pointB):
	xDiff = pointA[0] - pointB[0]
	yDiff = pointA[1] - pointB[1]
	dist = math.sqrt((xDiff ** 2) + (yDiff ** 2))
	return dist

clicks = 0


#MainLoop
mousePos = (0,0)
guy = Player(40, 530, 40, 60, (255,200,200))
font = pygame.font.SysFont('bahnschrift', 50, False)
mouseFont = pygame.font.SysFont('bahnschrift', 15, False) 
fill = False
dB = False

run = True
while(run):
	clock.tick(FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		elif event.type == 5:
			print("Clicked")
			clicks += 1
			fill = not fill
			mousePos = pygame.mouse.get_pos()
			print(mousePos)

	keys = pygame.key.get_pressed()
	if((keys[pygame.K_LEFT] or keys[pygame.K_a]) and guy.x > 0):
		guy.x -= guy.velocity
	if((keys[pygame.K_RIGHT] or keys[pygame.K_d]) and guy.x < RESOLUTION[0] - guy.width):
		guy.x += guy.velocity
	if (not guy.isJump):
		if(keys[pygame.K_SPACE]):
			guy.isJump = True
	else:
		if guy.jumpForce >= -guy.maxJump:
			if guy.jumpForce < 0:
				mult = -1
			else:
				mult = 1
			guy.y -= mult*(guy.jumpForce ** 2) / 4
			guy.jumpForce -= 1
		else:
			guy.jumpForce = guy.maxJump
			guy.isJump = False


	drawFrame()

pygame.quit()

# pygame.Surface.set_at(win, (10,10), (255,255,255))