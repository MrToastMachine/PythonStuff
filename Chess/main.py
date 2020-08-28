""" NECESSARY MODULES """
import pygame

pygame.init()
RES = (600, 400)
win = pygame.display.set_mode(RES)
pygame.display.set_caption("Chess")

TILE_WIDTH = 50

# TILE POSITION STORED IN TUPLE WITH TWO VALUES STARTING WITH (0,0) AS TOP LEFT TILE

class Piece():      #BASE CLASS FOR ALL PIECES
    pieces = []
    activeTile = [-1, -1]
    targetTile = [-1, -1]
    pieceSelected = [-1, -1]
    isOccupied = False
    moves = 0
    whiteTurn = True
    blackPoints = 0
    whitePoints = 0

    def __init__(self, name, initPos, sprite, isWhite):   #INITIAL SETUP OF PIECE
        self.name = name
        self.isWhite = isWhite
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
        Piece.whiteTurn = not Piece.whiteTurn
        reset()

    def giveMePoints(self):
        if self.isWhite:
            Piece.blackPoints += self.value
        else:
            Piece.whitePoints += self.value


    @classmethod
    def drawPiece(cls):
        for piece in Piece.pieces:
            position = [x*TILE_WIDTH for x in piece.tile]
            win.blit(piece.img, (position))

#  and (piece_on_target_tile == None or piece_on_target_tile.isWhite != piece.isWhite)

    @classmethod
    def checkValid(cls, piece):
        piece_on_target_tile = Piece.getPieceOnTile(Piece.targetTile)
        if (Piece.targetTile != piece.tile): # and not Piece.getPieceOnTile(Piece.targetTile)
            dX = abs(Piece.targetTile[0] - piece.tile[0])
            dY = abs(Piece.targetTile[1] - piece.tile[1])
            if piece.name == "King":
                if (dX <= 1) and (dY <= 1):
                    if piece_on_target_tile != None and piece_on_target_tile.isWhite != piece.isWhite:
                        Piece.pieces.pop(Piece.pieces.index(piece_on_target_tile))
                        Piece.giveMePoints(piece_on_target_tile)
                        del(piece_on_target_tile)
                        piece.movePiece()
                    elif not piece_on_target_tile:
                        piece.movePiece()
            elif piece.name == "Rook":
                if (dX == 0 or dY == 0):
                    if piece_on_target_tile != None and piece_on_target_tile.isWhite != piece.isWhite:
                        Piece.pieces.pop(Piece.pieces.index(piece_on_target_tile))
                        Piece.giveMePoints(piece_on_target_tile)
                        del(piece_on_target_tile)
                        piece.movePiece()
                    elif not piece_on_target_tile:
                        piece.movePiece()
            elif piece.name == "Bishop":
                if dX == dY:
                    if piece_on_target_tile != None and piece_on_target_tile.isWhite != piece.isWhite:
                        Piece.pieces.pop(Piece.pieces.index(piece_on_target_tile))
                        Piece.giveMePoints(piece_on_target_tile)
                        del(piece_on_target_tile)
                        piece.movePiece()
                    elif not piece_on_target_tile:
                        piece.movePiece()
            elif piece.name == "Queen":
                if (dX == dY) or (dX == 0 or dY == 0):
                    if piece_on_target_tile != None and piece_on_target_tile.isWhite != piece.isWhite:
                        Piece.pieces.pop(Piece.pieces.index(piece_on_target_tile))
                        Piece.giveMePoints(piece_on_target_tile)
                        del(piece_on_target_tile)
                        piece.movePiece()
                    elif not piece_on_target_tile:
                        piece.movePiece()
            elif piece.name == "Knight":
                if (dX == 2 and dY == 1) or (dX == 1 and dY == 2):
                    if piece_on_target_tile != None and piece_on_target_tile.isWhite != piece.isWhite:
                        Piece.pieces.pop(Piece.pieces.index(piece_on_target_tile))
                        Piece.giveMePoints(piece_on_target_tile)
                        del(piece_on_target_tile)
                        piece.movePiece()
                    elif not piece_on_target_tile:
                        piece.movePiece()
            elif piece.name == "Pawn":
                if (dX == 0) and not piece_on_target_tile:
                    if piece.isWhite:
                        if Piece.targetTile[1] - piece.tile[1] == -1:
                            piece.movePiece()
                        elif Piece.targetTile[1] - piece.tile[1] == -2 and piece.tile == piece.origin:
                            piece.movePiece()
                    else:
                        if Piece.targetTile[1] - piece.tile[1] == 1:
                            piece.movePiece()
                        elif Piece.targetTile[1] - piece.tile[1] == 2 and piece.tile == piece.origin:
                            piece.movePiece()
                elif dX == dY == 1:
                    if piece.isWhite and Piece.targetTile[1] - piece.tile[1] < 0:
                        if piece_on_target_tile and (not piece_on_target_tile.isWhite):
                            Piece.pieces.pop(Piece.pieces.index(piece_on_target_tile))
                            Piece.giveMePoints(piece_on_target_tile)
                            del(piece_on_target_tile)
                            piece.movePiece()
                    elif not piece.isWhite and Piece.targetTile[1] - piece.tile[1] > 0:
                        if piece_on_target_tile and piece_on_target_tile.isWhite:
                            Piece.pieces.pop(Piece.pieces.index(piece_on_target_tile))
                            Piece.giveMePoints(piece_on_target_tile)
                            del(piece_on_target_tile)
                            piece.movePiece()
                    else:
                        print("NO PIECE THERE")



    @classmethod
    def getPieceOnTile(cls, tile):
        for piece in Piece.pieces:
            if (tile == piece.tile):
                return piece
        return None

    @classmethod
    def returnToOrigin(cls):
        Piece.moves = 0
        Piece.whitePoints = 0
        Piece.blackPoints = 0
        reset()
        Piece.whiteTurn = True
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
MAIN_FILE_PATH = "Chess/" # Yoga Laptop
#MAIN_FILE_PATH = "PythonStuff/Chess/" # Y70 Laptop

board = pygame.image.load(MAIN_FILE_PATH + 'background.jpg')
parchment = pygame.image.load(MAIN_FILE_PATH + 'Worn-Paper-Texture.jpg')


#PIECES
BKing = Piece("King", [3,0], pygame.image.load(MAIN_FILE_PATH + 'BKing.png'), False)
BQueen = Piece("Queen", [4,0], pygame.image.load(MAIN_FILE_PATH + 'BQueen.png'), False)
BRookL = Piece("Rook", [7,0], pygame.image.load(MAIN_FILE_PATH + 'BRook.png'), False)
BRookR = Piece("Rook", [0,0], pygame.image.load(MAIN_FILE_PATH + 'BRook.png'), False)
BBishopL = Piece("Bishop", [2,0], pygame.image.load(MAIN_FILE_PATH + 'BBishop.png'), False)
BBishopR = Piece("Bishop", [5,0], pygame.image.load(MAIN_FILE_PATH + 'BBishop.png'), False)
BKnightL = Piece("Knight", [6,0], pygame.image.load(MAIN_FILE_PATH + 'BKnight.png'), False)
BKnightR = Piece("Knight", [1,0], pygame.image.load(MAIN_FILE_PATH + 'BKnight.png'), False)
BPawn1 = Piece("Pawn", [0,1], pygame.image.load(MAIN_FILE_PATH + 'BPawn.png'), False)
BPawn2 = Piece("Pawn", [1,1], pygame.image.load(MAIN_FILE_PATH + 'BPawn.png'), False)
BPawn3 = Piece("Pawn", [2,1], pygame.image.load(MAIN_FILE_PATH + 'BPawn.png'), False)
BPawn4 = Piece("Pawn", [3,1], pygame.image.load(MAIN_FILE_PATH + 'BPawn.png'), False)
BPawn5 = Piece("Pawn", [4,1], pygame.image.load(MAIN_FILE_PATH + 'BPawn.png'), False)
BPawn6 = Piece("Pawn", [5,1], pygame.image.load(MAIN_FILE_PATH + 'BPawn.png'), False)
BPawn7 = Piece("Pawn", [6,1], pygame.image.load(MAIN_FILE_PATH + 'BPawn.png'), False)
BPawn8 = Piece("Pawn", [7,1], pygame.image.load(MAIN_FILE_PATH + 'BPawn.png'), False)

WKing = Piece("King", [3,7], pygame.image.load(MAIN_FILE_PATH + 'WKing.png'), True)
WQueen = Piece("Queen", [4,7], pygame.image.load(MAIN_FILE_PATH + 'WQueen.png'), True)
WRookL = Piece("Rook", [0,7], pygame.image.load(MAIN_FILE_PATH + 'WRook.png'), True)
WRookR = Piece("Rook", [7,7], pygame.image.load(MAIN_FILE_PATH + 'WRook.png'), True)
WBishopL = Piece("Bishop", [5,7], pygame.image.load(MAIN_FILE_PATH + 'WBishop.png'), True)
WBishopR = Piece("Bishop", [2,7], pygame.image.load(MAIN_FILE_PATH + 'WBishop.png'), True)
WKnightL = Piece("Knight", [1,7], pygame.image.load(MAIN_FILE_PATH + 'WKnight.png'), True)
WKnightR = Piece("Knight", [6,7], pygame.image.load(MAIN_FILE_PATH + 'WKnight.png'), True)
WPawn1 = Piece("Pawn", [0,6], pygame.image.load(MAIN_FILE_PATH + 'WPawn.png'), True)
WPawn2 = Piece("Pawn", [1,6], pygame.image.load(MAIN_FILE_PATH + 'WPawn.png'), True)
WPawn3 = Piece("Pawn", [2,6], pygame.image.load(MAIN_FILE_PATH + 'WPawn.png'), True)
WPawn4 = Piece("Pawn", [3,6], pygame.image.load(MAIN_FILE_PATH + 'WPawn.png'), True)
WPawn5 = Piece("Pawn", [4,6], pygame.image.load(MAIN_FILE_PATH + 'WPawn.png'), True)
WPawn6 = Piece("Pawn", [5,6], pygame.image.load(MAIN_FILE_PATH + 'WPawn.png'), True)
WPawn7 = Piece("Pawn", [6,6], pygame.image.load(MAIN_FILE_PATH + 'WPawn.png'), True)
WPawn8 = Piece("Pawn", [7,6], pygame.image.load(MAIN_FILE_PATH + 'WPawn.png'), True)

def infoBox():
    # pygame.draw.rect(win, (255,255,205), (400,0,200,400))
    win.blit(parchment, (400, 0))

    text = font.render("Moves: " +str(Piece.moves), 1, black)
    win.blit(text, (410, 10))

    turnMessage = "Turn: " + ("White" if Piece.whiteTurn else "Black")
    turnText = font.render(turnMessage, 1, black)
    win.blit(turnText, (410, 35))

    blackPoints = font.render("Black: " + str(Piece.blackPoints), 1, black)
    win.blit(blackPoints, (410, 70))
    whitePoints = font.render("White: " + str(Piece.whitePoints), 1, black)
    win.blit(whitePoints, (410, 85))
    
    pygame.draw.rect(win, black, (420, 325, 160, 50))
    resetText = resetFont.render("RESET", 1, white)
    win.blit(resetText, (460,330))


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

font = pygame.font.SysFont('bradleyhanditc', 20, True)
resetFont = pygame.font.SysFont('Arial', 30, True)
running = True
update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # GETS ANY MOUSE CLICK
            if 420 < pygame.mouse.get_pos()[0] < 580 and 325 < pygame.mouse.get_pos()[1] < 375:
                Piece.returnToOrigin()

            if pygame.mouse.get_pressed()[0]:       # CHECKS IF ITS LEFT CLICK
                if Piece.activeTile:
                    if Piece.isOccupied: # IF TILE CLICKED AND TILE ALREADY SELECTED HAS PIECE
                        # print("Trying to move")
                        Piece.targetTile = getClickedTile(pygame.mouse.get_pos())
                        Piece.checkValid(Piece.pieceSelected) # <----------------------------------------------
                    else:
                        Piece.activeTile = getClickedTile(pygame.mouse.get_pos())
                        inhabitant = Piece.getPieceOnTile(Piece.activeTile)
                        if inhabitant and inhabitant.isWhite == Piece.whiteTurn:
                            Piece.pieceSelected = inhabitant
                            Piece.isOccupied = True
                        else:
                            Piece.pieceSelected = None
                            Piece.isOccupied = False
                else:
                    Piece.activeTile = getClickedTile(pygame.mouse.get_pos())
                    inhabitant = Piece.getPieceOnTile(Piece.activeTile)
                    if inhabitant and inhabitant.isWhite == Piece.whiteTurn:
                        Piece.pieceSelected = inhabitant
                        Piece.isOccupied = True
                    else:
                        Piece.pieceSelected = None
                        Piece.isOccupied = False
            else:   #RESETS ACTIVETILE TO NONE IF RIGHT OR MIDDLE CLICK -- DESELECTS TILE
                reset()
            update()

    # update()


# TO ADD
#  + Check if king is in check
#  + Castling
#  + Allow pawn to take pieces