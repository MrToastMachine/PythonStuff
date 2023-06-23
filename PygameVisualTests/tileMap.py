import pygame

padding = 5 # pixels

class tileMap():
    all_tiles = []
    def __init__(self, win, grid_size, grid_pos_start, grid_pos_end, colour):
        self.win = win
        self.grid_size = grid_size
        self.grid_pos_start = grid_pos_start
        self.grid_pos_end = grid_pos_end
        self.colour = colour
        self.tile_id = len(tileMap.all_tiles)

        tileMap.all_tiles.append(self)

    @classmethod
    def drawTiles(cls):
        for tile in cls.all_tiles:
            print(f"tile: {tile.tile_id}")
            print(tile.win.get_size())