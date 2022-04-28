# my first game

import random
import pygame
import os


game = True #Флаг бесконечного цикла игры

''' Настройки экрана'''
class Window_settings:
    WIDTH = 800  # ширина игрового окна
    HEIGHT = 600  # высота игрового окна
    FPS = 30  # частота кадров в секунду


''' Доступные цвета '''
colors = {"BLACK": [0, 0, 0], "WHITE": [255, 255, 255]}


''' Класс создаваемого объекта игрока'''
class Player(pygame.sprite.Sprite):

    #флаги движения < >
    left = False
    right = False 

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [] = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (100, 500)
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8

        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx   

        #Ушли за правый край
        if self.rect.left > Window_settings.WIDTH:
            self.rect.right = 0

        if self.rect.right < 0: 
            self.rect.left = Window_settings.WIDTH    



""" START """

pygame.init()        # Инит драйвера
pygame.mixer.init()  # для звука

window = pygame.display.set_mode((Window_settings.WIDTH, Window_settings.HEIGHT))  # Разрешение

''' Папки '''
#TODO: Сделать правильные пути
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

# Нулевые координаты для фоновой картинки
background_position = [0, 0]


#TODO: Загрузи все картинки RAZBERI KLASSI
player_img = pygame.image.load(os.path.join(img_folder, 'mario.png')).convert() #Игрок
background_image = pygame.image.load(os.path.join(img_folder, 'bg.png')).convert() #задний фон


pygame.display.set_caption("Run Gary! RUN!") # Заголовок окна

clock = pygame.time.Clock()
window.fill(colors["WHITE"])


# Спрайты
sprites = pygame.sprite.Group()
hero = Player()
sprites.add(hero)

while game:
    # Обновление
    sprites.update()
    
    # Рендеринг
    window.blit(background_image, background_position)
    #window.fill(colors["WHITE"])
    sprites.draw(window)

    clock.tick(Window_settings.FPS)

    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.speedx = -8
            if event.key == pygame.K_RIGHT:
                hero.speedx = 8    

    pygame.display.update()

