import pygame
from const import *
from map import room_set

def mapping(a, b):
    return (a//TILE)*TILE, (b//TILE)*TILE

def ray_casting(screen, player_pos, player_angle):
    x0, y0 = player_pos
    xm, ym = mapping(x0, y0)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE):
            depth_v = (x - x0) / cos_a
            y = y0 + depth_v * sin_a
            if mapping(x + dx, y) in room_set:
                break
            x += dx * TILE

        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - y0) / sin_a
            x = x0 + depth_h * cos_a
            if mapping(x, y + dy) in room_set:
                break
            y += dy * TILE

        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(PROJ_COEFF / depth),2*HEIGHT)
        c = 255 / (1 + depth * depth * 0.0001)
        color = (c, c, c)
        pygame.draw.rect(screen, color, (ray * SCALE, HEIGHT // 2 - proj_height // 2, SCALE, proj_height))
        cur_angle += DELTA_ANGLE
