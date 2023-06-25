RES = (900,700)

grid_size = (4,3)

xJump = RES[0]/grid_size[0]

grid_resolution = [(x[0]/x[1]) for x in zip(RES,grid_size)]

print(grid_resolution)