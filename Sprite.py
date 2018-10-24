# -*- coding = utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit
from random import randint






SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

class Player(pygame.sprite.Sprite):
    def __init__(self, initial_position):
        pygame.sprite.Sprite.__init__(self)#构造父类函数
        self.image = pygame.Surface([10, 10])#精灵图片Surface
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()#精灵大小
        self.rect.topleft = initial_position#精灵图片位置

        self.speed = 6

    def update(self):
        self.rect.left += self.speed
        if self.rect.left > SCREEN_WIDTH:
            self.kill()

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

group = pygame.sprite.Group()

while True:
    clock.tick(10)
    print(len(group.sprites()))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((255,255,255))

    group.add(Player((randint(0,SCREEN_WIDTH),randint(0,SCREEN_HEIGHT))))
    group.update()
    group.draw(screen)
    pygame.display.update()

