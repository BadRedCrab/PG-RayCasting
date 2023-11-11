import pygame
from const import *
from player import Player
import math
from map import room_set
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player()
drawing = Drawing(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    screen.fill(BLACK)

    drawing.SCENE(player.pos, player.angle, clock)

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
