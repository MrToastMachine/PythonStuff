import pygame

padding = 10 # pixels

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
            grid_res = [(x[0]/x[1]) for x in zip(tile.win.get_size(),tile.grid_size)]
            rect_start = [(x[0]*(x[1]-1)) + padding/2 for x in zip(grid_res, tile.grid_pos_start)]
            tile_width = (tile.grid_pos_end[0] - tile.grid_pos_start[0] + 1) * grid_res[0] - padding
            tile_height = (tile.grid_pos_end[1] - tile.grid_pos_start[1] + 1) * grid_res[1] - padding

            pygame.draw.rect(tile.win,tile.colour,(rect_start[0], rect_start[1], tile_width, tile_height), 0, 20)