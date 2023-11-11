from const import *
import pygame
from map import player_pos, room_set
import math

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if (((self.x+player_speed * cos_a)//TILE)*TILE, ((self.y+player_speed * sin_a)//TILE)*TILE) in room_set:
                return
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            if (((self.x-player_speed * cos_a)//TILE)*TILE, ((self.y-player_speed * sin_a)//TILE)*TILE) in room_set:
                return
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            if (((self.x+player_speed * sin_a)//TILE)*TILE, ((self.y-player_speed * cos_a)//TILE)*TILE) in room_set:
                return
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys[pygame.K_d]:
            if (((self.x-player_speed * sin_a)//TILE)*TILE, ((self.y+player_speed * cos_a)//TILE)*TILE) in room_set:
                return
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
