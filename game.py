#my first game

game = True

import pygame
import random


class window_settings:
    WIDTH = 800  # ширина игрового окна
    HEIGHT = 600 # высота игрового окна
    FPS = 30 # частота кадров в секунду
    colors = { "BLACK" : [0, 0, 0], "WHITE" : [255, 255, 255] }


pygame.init()
pygame.mixer.init()  # для звука

window = pygame.display.set_mode((window_settings.WIDTH, window_settings.HEIGHT)) #resolution
pygame.display.set_caption("Run Gary! RUN!")
clock = pygame.time.Clock()
window.fill(window_settings.colors["WHITE"])

while game:
    game = True
    pygame.display.update()
    #pygame.display.
