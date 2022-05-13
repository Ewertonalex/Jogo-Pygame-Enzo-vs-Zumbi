import pygame
import math
import random

class zumbi(pygame.sprite.Sprite):
    def __init__(self, *groups):

        super().__init__(*groups)
        self.image = pygame.image.load("data/zumbiazul.png")  # 16x16s
        self.image = pygame.transform.scale(self.image, [80, 80])
        self.rect = pygame.Rect(50, 50, 100, 100)



        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(1, 400)

        self.timer = 0

        self.speed = 1 + random.random() * 2

    def update(self, *args):
        if self.rect.right < 0:
            self.kill()
        #LOGICA

        self.rect.x -= self.speed