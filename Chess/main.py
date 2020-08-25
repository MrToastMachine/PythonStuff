""" NECESSARY MODULES """
import pygame

pygame.init()
RES = (600, 400)
win = pygame.display.set_mode(RES)

TILE_WIDTH = 50

# TILE POSITION STORED IN TUPLE WITH TWO VALUES STARTING WITH (0,0) AS TOP LEFT TILE

class Piece():      #BASE CLASS FOR ALL PIECES
    pieces = []
    activeTile = [-1, -1]
    targetTile = [-1, -1]
    pieceSelected = [-1, -1]
    isOccupied = False
    moves = 0
    turn = 'w'

    def __init__(self, name, initPos, sprite, colour='b'):   #INITIAL SETUP OF PIECE
        self.name = name
        self.colour = colour
        self.origin = initPos
        self.tile = initPos
        self.img = sprite
        Piece.pieces.append(self)
        if name == "Queen":
            self.value = 9
        elif name == "Rook":
            self.value = 5
        elif name == "Bishop":
            self.value = 3
        elif name == "Knight":
            self.value = 3
        else:
            self.value = 1

    def movePiece(self):
        self.tile = Piece.targetTile
        Piece.moves += 1
        if Piece.turn == 'w':
            Piece.turn = 'b'
        elif Piece.turn == 'b':
            Piece.turn = 'w'
        reset()

    @classmethod
    def drawPiece(cls):
        for piece in Piece.pieces:
            position = [x*TILE_WIDTH for x in piece.tile]
            win.blit(piece.img, (position))

    @classmethod
    def checkValid(cls, piece):
        if (Piece.targetTile != piece.tile) and not Piece.getPieceOnTile(Piece.targetTile):
            dX = abs(Piece.targetTile[0] - piece.tile[0])
            dY = abs(Piece.targetTile[1] - piece.tile[1])
            if piece.name == "King":
                if (dX <= 1) and (dY <= 1):
                    piece.movePiece()
            elif piece.name == "Rook":
                if (dX == 0 or dY == 0):
                    piece.movePiece()
            elif piece.name == "Bishop":
                if dX == dY:
                    piece.movePiece()
            elif piece.name == "Queen":
                if (dX == dY) or (dX == 0 or dY == 0):
                    piece.movePiece()
            elif piece.name == "Knight":
                if (dX == 2 and dY == 1) or (dX == 1 and dY == 2):
                    piece.movePiece()
            elif piece.name == "Pawn":
                if (dX == 0):
                    if piece.colour == 'b':
                        if Piece.targetTile[1] - piece.tile[1] == 1:
                            piece.movePiece()
                        elif Piece.targetTile[1] - piece.tile[1] == 2 and piece.tile == piece.origin:
                            piece.movePiece()
                    else:
                        if Piece.targetTile[1] - piece.tile[1] == -1:
                            piece.movePiece()
                        elif Piece.targetTile[1] - piece.tile[1] == -2 and piece.tile == piece.origin:
                            piece.movePiece()

    @classmethod
    def getPieceOnTile(cls, tile):
        for piece in Piece.pieces:
            if (tile == piece.tile):
                return piece
                break
        return None

    @classmethod
    def returnToOrigin(cls):
        Piece.moves = 0
        reset()
        Piece.turn = 'w'
        for piece in Piece.pieces:
            piece.tile = piece.origin

def getClickedTile(mPos):
    return list(x//50 for x in mPos)

def reset(): #DESELECTS ALL AND SETS ALL TO EMPTY
    Piece.activeTile = None
    Piece.targetTile = None
    Piece.pieceSelected = None
    Piece.isOccupied = False


#COLOURS
red = (240, 30, 30)
green = (30, 240, 30)
black = (0, 0, 0)
white = (255, 255, 255)

#SPRITES
board = pygame.image.load('PythonStuff/Chess/background.jpg')

#PIECES
BKing = Piece("King", [3,0], pygame.image.load('PythonStuff/Chess/BKing.png'), 'b')
BQueen = Piece("Queen", [4,0], pygame.image.load('PythonStuff/Chess/BQueen.png'), 'b')
BRookL = Piece("Rook", [7,0], pygame.image.load('PythonStuff/Chess/BRook.png'), 'b')
BRookR = Piece("Rook", [0,0], pygame.image.load('PythonStuff/Chess/BRook.png'), 'b')
BBishopL = Piece("Bishop", [2,0], pygame.image.load('PythonStuff/Chess/BBishop.png'), 'b')
BBishopR = Piece("Bishop", [5,0], pygame.image.load('PythonStuff/Chess/BBishop.png'), 'b')
BKnightL = Piece("Knight", [6,0], pygame.image.load('PythonStuff/Chess/BKnight.png'), 'b')
BKnightR = Piece("Knight", [1,0], pygame.image.load('PythonStuff/Chess/BKnight.png'), 'b')
BPawn1 = Piece("Pawn", [0,1], pygame.image.load('PythonStuff/Chess/BPawn.png'), 'b')
BPawn2 = Piece("Pawn", [1,1], pygame.image.load('PythonStuff/Chess/BPawn.png'), 'b')
BPawn3 = Piece("Pawn", [2,1], pygame.image.load('PythonStuff/Chess/BPawn.png'), 'b')
BPawn4 = Piece("Pawn", [3,1], pygame.image.load('PythonStuff/Chess/BPawn.png'), 'b')
BPawn5 = Piece("Pawn", [4,1], pygame.image.load('PythonStuff/Chess/BPawn.png'), 'b')
BPawn6 = Piece("Pawn", [5,1], pygame.image.load('PythonStuff/Chess/BPawn.png'), 'b')
BPawn7 = Piece("Pawn", [6,1], pygame.image.load('PythonStuff/Chess/BPawn.png'), 'b')
BPawn8 = Piece("Pawn", [7,1], pygame.image.load('PythonStuff/Chess/BPawn.png'), 'b')

WKing = Piece("King", [3,7], pygame.image.load('PythonStuff/Chess/WKing.png'), 'w')
WQueen = Piece("Queen", [4,7], pygame.image.load('PythonStuff/Chess/WQueen.png'), 'w')
WRookL = Piece("Rook", [0,7], pygame.image.load('PythonStuff/Chess/WRook.png'), 'w')
WRookR = Piece("Rook", [7,7], pygame.image.load('PythonStuff/Chess/WRook.png'), 'w')
WBishopL = Piece("Bishop", [5,7], pygame.image.load('PythonStuff/Chess/WBishop.png'), 'w')
WBishopR = Piece("Bishop", [2,7], pygame.image.load('PythonStuff/Chess/WBishop.png'), 'w')
WKnightL = Piece("Knight", [1,7], pygame.image.load('PythonStuff/Chess/WKnight.png'), 'w')
WKnightR = Piece("Knight", [6,7], pygame.image.load('PythonStuff/Chess/WKnight.png'), 'w')
WPawn1 = Piece("Pawn", [0,6], pygame.image.load('PythonStuff/Chess/WPawn.png'), 'w')
WPawn2 = Piece("Pawn", [1,6], pygame.image.load('PythonStuff/Chess/WPawn.png'), 'w')
WPawn3 = Piece("Pawn", [2,6], pygame.image.load('PythonStuff/Chess/WPawn.png'), 'w')
WPawn4 = Piece("Pawn", [3,6], pygame.image.load('PythonStuff/Chess/WPawn.png'), 'w')
WPawn5 = Piece("Pawn", [4,6], pygame.image.load('PythonStuff/Chess/WPawn.png'), 'w')
WPawn6 = Piece("Pawn", [5,6], pygame.image.load('PythonStuff/Chess/WPawn.png'), 'w')
WPawn7 = Piece("Pawn", [6,6], pygame.image.load('PythonStuff/Chess/WPawn.png'), 'w')
WPawn8 = Piece("Pawn", [7,6], pygame.image.load('PythonStuff/Chess/WPawn.png'), 'w')

def infoBox():
    pygame.draw.rect(win, (255,255,205), (400,0,200,400))
    text = font.render("Moves: " +str(Piece.moves), 1, black)
    win.blit(text, (410, 10))
    turnText = font.render("Turn: " + Piece.turn, 1, black)
    win.blit(turnText, (410,35))
    
    pygame.draw.rect(win, black, (420, 325, 160, 50))
    resetText = font.render("RESET", 1, white)
    win.blit(resetText, (440,330))


def update():
    win.blit(board, (0, 0))
    Piece.drawPiece()
    

    if Piece.activeTile:
        posX = Piece.activeTile[0]*TILE_WIDTH
        posY = Piece.activeTile[1]*TILE_WIDTH
        if Piece.isOccupied:
            pygame.draw.rect(win, green, (posX, posY, TILE_WIDTH, TILE_WIDTH), 2)
        else:
            pygame.draw.rect(win, red, (posX, posY, TILE_WIDTH, TILE_WIDTH), 2)

    infoBox()
    
    pygame.display.update()

font = pygame.font.SysFont('bradleyhanditc', 30, True)
resetFont = pygame.font.SysFont('Arial', 30, True)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # GETS ANY MOUSE CLICK
            if 420 < pygame.mouse.get_pos()[0] < 580 and 325 < pygame.mouse.get_pos()[1] < 375:
                Piece.returnToOrigin()

            if pygame.mouse.get_pressed()[0]:       # CHECKS IF ITS LEFT CLICK
                if Piece.activeTile:
                    if Piece.isOccupied:
                        # print("Trying to move")
                        Piece.targetTile = getClickedTile(pygame.mouse.get_pos())
                        Piece.checkValid(Piece.pieceSelected)
                    else:
                        Piece.activeTile = getClickedTile(pygame.mouse.get_pos())
                        inhabitant = Piece.getPieceOnTile(Piece.activeTile)
                        if inhabitant and inhabitant.colour == Piece.turn:
                            Piece.pieceSelected = inhabitant
                            Piece.isOccupied = True
                        else:
                            Piece.pieceSelected = None
                            Piece.isOccupied = False
                else:
                    Piece.activeTile = getClickedTile(pygame.mouse.get_pos())
                    inhabitant = Piece.getPieceOnTile(Piece.activeTile)
                    if inhabitant and inhabitant.colour == Piece.turn:
                        Piece.pieceSelected = inhabitant
                        Piece.isOccupied = True
                    else:
                        Piece.pieceSelected = None
                        Piece.isOccupied = False
            else:   #RESETS ACTIVETILE TO NONE IF RIGHT OR MIDDLE CLICK -- DESELECTS TILE
                reset()

    update()