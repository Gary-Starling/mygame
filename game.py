# my first game

import random
import pygame
import os



game = True


''' Настройки экрана'''


class window_settings:
    WIDTH = 800  # ширина игрового окна
    HEIGHT = 600  # высота игрового окна
    FPS = 30  # частота кадров в секунду


''' Доступные цвета '''
colors = {"BLACK": [0, 0, 0], "WHITE": [255, 255, 255]}


''' Класс создаваемого объекта '''
class some_obj(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (400, 120)
        self.speedx = 0

    def update(self):
        '''
        #Ушли за левый край
        if self.rect.right < 0:
            self.rect.right = window_settings.WIDTH 
            '''

        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8

        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx   

        #Ушли за правый край
        if self.rect.left > window_settings.WIDTH:
            self.rect.right = 0

        if self.rect.right < 0: 
            self.rect.left = window_settings.WIDTH    



 # настройка папки ассетов

pygame.init()  # Инит драйвера
pygame.mixer.init()  # для звука
window = pygame.display.set_mode((window_settings.WIDTH, window_settings.HEIGHT))  # Разрешение

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'mario.png')).convert()


pygame.display.set_caption("Run Gary! RUN!") # Заголовок окна
clock = pygame.time.Clock()
window.fill(colors["WHITE"])


# Спрайты
sprites = pygame.sprite.Group()
rect = some_obj()
sprites.add(rect)

while game:
    # Обновление
    sprites.update()
    
    # Рендеринг
    window.fill(colors["WHITE"])
    sprites.draw(window)

    clock.tick(window_settings.FPS)

    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.speedx = -8
            if event.key == pygame.K_RIGHT:
                rect.speedx = 8    

    pygame.display.update()

