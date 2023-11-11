import math
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WBLUE = (123, 102, 230)
PURPLE = (167, 185, 247)
WGREEN = (193, 220, 94)
DBLUE = (124, 73, 108)
ORANGE = (226, 151, 74)

WIDTH = 800
HEIGHT = 640
TILE = 50
FPS = 60
running = True
#player_pos = (MX//2, MY//2)
player_angle = 0
player_speed = 2

FOV = math.pi/3
HALF_FOV = FOV/2
NUM_RAYS = 400
MAX_DEPTH = 800
DELTA_ANGLE = FOV/NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH//NUM_RAYS

