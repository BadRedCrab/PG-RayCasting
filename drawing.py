import pygame
from const import *
from ray_casting import ray_casting
from map import room_set
class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24, bold = True)
    def SCENE(self, player_pos, player_angle, clock):
        self.background()
        self.word(player_pos, player_angle)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            pass
        self.fps(clock)

    def background(self):
        pygame.draw.rect(self.screen, (15,15,15), (0, 0, WIDTH, HEIGHT // 2))
        CSTEP = 50
        STEP = (HEIGHT - HEIGHT // 2) / CSTEP
        for i in range(1, CSTEP):
            color = math.sin(i/16-math.pi/2)*40+40
            pygame.draw.rect(self.screen, (color, color, color),
                             (0, HEIGHT // 2 + STEP*(i-1), WIDTH, HEIGHT // 2 + STEP*i))

    def word(self, player_pos, player_angle):
        ray_casting(self.screen,player_pos, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, DBLUE)
        self.screen.blit(render, (12, 5))
