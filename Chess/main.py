import pygame
import os

pygame.init()
print(os.getcwd())
RES = (400,400)
win = pygame.display.set_mode(RES)

tileWidth = 50
activeTile = None
targetTile = None
pieceSelected = None
isOccupied = False

# TILE POSITION STORED IN TUPLE WITH TWO VALUES STARTING WITH (0,0) AS TOP LEFT TILE

class Piece():
    pieces = []
    def __init__(self, name):
        self.name = name
        self.tile = [0,0]
        self.img = pygame.image.load('PythonStuff/Chess/BKing.png')
        Piece.pieces.append(self)

    def drawPiece(self):
        position = [x*tileWidth for x in self.tile]
        win.blit(self.img, (position))
    
    @classmethod
    def movePiece(cls, piece, targetTile):
        
        if ((abs(targetTile[0]-piece.tile[0]) <= 1) and (abs(targetTile[1]-piece.tile[1]) <= 1)):
            print("I can move there")
            piece.tile = targetTile
            reset()
        else:
            print("I can't move there")


    @classmethod
    def getPieceOnTile(cls, tile):
        global isOccupied
        global pieceSelected
        for piece in Piece.pieces:
            if (tile == piece.tile):
                pieceSelected = piece
                isOccupied = True
                print(f"Piece Selected: {piece.name}")
                break
                # return True
            pieceSelected = None
            isOccupied = False

def getClickedTile(mPos):
    return list(x//50 for x in mPos)

def reset():
    global activeTile
    global targetTile
    global pieceSelected
    global isOccupied
    activeTile = None
    targetTile = None
    pieceSelected = None
    isOccupied = False

king = Piece("King")


#COLOURS
red = (240,30,30)
green = (30,240,30)

#SPRITES
board = pygame.image.load('PythonStuff/Chess/background.jpg')

def update():
    win.blit(board,(0,0))
    king.drawPiece()

    if(activeTile):
        posX = activeTile[0]*tileWidth
        posY = activeTile[1]*tileWidth
        if isOccupied:
            pygame.draw.rect(win, green, (posX, posY, tileWidth, tileWidth), 2)
        else:
            pygame.draw.rect(win, red, (posX, posY, tileWidth, tileWidth), 2)

    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # GETS ANY MOUSE CLICK
            if pygame.mouse.get_pressed()[0]:       # CHECKS IF ITS LEFT CLICK
                if activeTile:
                    if isOccupied:
                        # print("Trying to move")
                        targetTile = getClickedTile(pygame.mouse.get_pos())
                        Piece.movePiece(pieceSelected, targetTile)
                    else:
                        activeTile = getClickedTile(pygame.mouse.get_pos())
                        Piece.getPieceOnTile(activeTile)
                else:
                    activeTile = getClickedTile(pygame.mouse.get_pos())
                    Piece.getPieceOnTile(activeTile)
            else:   #RESETS ACTIVETILE TO NONE IF RIGHT OR MIDDLE CLICK -- DESELECTS TILE
                activeTile = None

    update()