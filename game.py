# The mushrooms

from pickle import FALSE
import random
import pygame
import os

''' CONST '''
WIDTH = 800  # ширина игрового окна
HIGHT = 600  # высота игрового окна
FPS = 30  # частота кадров в секунду



game = True #Флаг бесконечного цикла игры

''' Настройки экрана'''
class Window_settings:
    # Конструктор
    def __init__(self, width, hight, fps):
        self.width = width# ширина игрового окна
        self.hight = hight  # высота игрового окна
        self.fps = fps # частота кадров в секунду


''' Доступные цвета '''
colors = {"BLACK": [0, 0, 0], "WHITE": [255, 255, 255]}


''' Класс создаваемого игрока'''
class Player(pygame.sprite.Sprite): #Родительский класс Sprite

    # флаги движения
    left = False
    right = False 
    up = False
    down = False

    # Конструктор
    def __init__(self, image_name):
        pygame.sprite.Sprite.__init__(self)
        '''установив методом convert_alpha необходимую прозрачность '''
        self.index = 0
        self.images = []
        self.images.append(pygame.image.load(os.path.join(img_folder, "mush_stay.png")).convert_alpha())  #Игрок
        self.images.append(pygame.image.load(os.path.join(img_folder, "mush_l1.png")).convert_alpha())
        self.images.append(pygame.image.load(os.path.join(img_folder, "mush_l2.png")).convert_alpha())

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 500)
        self.speedx = 0

    # Обновление движения
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.speedx = -8
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx   

        #Ушли за правый край
        if self.rect.left > settings.width:
            self.rect.right = 0

        if self.rect.right < 0: 
            self.rect.left = settings.width    



""" START """
settings = Window_settings(WIDTH, HIGHT, FPS) # Настройки экрана

pygame.init()        # Инит драйвера
pygame.mixer.init()  # для звука


window = pygame.display.set_mode((settings.width, settings.hight))  # Создать окно с разр. X x Y

''' Папки '''
#TODO: Сделать правильные пути
game_folder = os.path.dirname(__file__)
bg_folder = os.path.join(game_folder, 'img')
img_folder = os.path.join(game_folder, 'img/mush_left')

# Нулевые координаты для фоновой картинки
background_position = [0, 0]


#TODO: Загрузи все картинки
background_image = pygame.image.load(os.path.join(bg_folder, 'bg.png')).convert() #задний фон


pygame.display.set_caption("MUSHROOMS") # Заголовок окна

clock = pygame.time.Clock()
window.fill(colors["WHITE"])


# Спрайты
sprites = pygame.sprite.Group()
hero = Player('mush_stay.png')
sprites.add(hero)

while game:
    # Обновление
    sprites.update()
    
    # Рендеринг
    window.blit(background_image, background_position)
    sprites.draw(window)

    clock.tick(settings.fps)

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

