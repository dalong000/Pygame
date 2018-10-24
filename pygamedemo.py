# -*- coding = -utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit

class Hero(pygame.sprite.Sprite):
    def __init__(self, hero_surface, hero_init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = hero_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = hero_init_pos
        self.speed = 6

    def move(self,offset):




#定义窗口分辨率
SCREEN_WIDTH = 390
SCREEN_HEIGHT = 520

#周期变量
ticks = 0
#dict
offset = {pygame.K_LEFT:0, pygame.K_RIGHT:0, pygame.K_UP:0, pygame.K_DOWN:0}

#初始化游戏
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])#初始化窗口
pygame.display.set_caption('gamedemo')#设置标题
#载入背景
background = pygame.image.load('resources/image/background.PNG')

#载入资源图片
shoot_img = pygame.image.load('resources/image/shoot.png')
#使用subsurface剪切载入的图片
hero1_rect = pygame.Rect(10,100,99,126)
hero2_rect = pygame.Rect(40,100,99,126)
hero1 = shoot_img.subsurface(hero1_rect)
hero2 = shoot_img.subsurface(hero2_rect)
hero_pos = [200 ,500]

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    #绘制背景
    screen.blit(background, (0,0))

    if ticks % 50 < 25:
        screen.blit(hero1,hero_pos)
    else:
        screen.blit(hero2,hero_pos)
    ticks += 1

    #更新屏幕
    pygame.display.update()
    #处理游戏退出
    #从消息队列中读取消息
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
            #控制方向
        if event.type == pygame.KEYDOWN:
            if event.key in offset:
                offset[event.key] = 3
        elif event.type == pygame.KEYUP:
            if event.key in offset:
                offset[event.key] = 0


    hero_x = hero_pos[0] + offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
    hero_y = hero_pos[1] + offset[pygame.K_DOWN] - offset[pygame.K_UP]
    if hero_pos[0] < 0:
        hero_pos[0] = 0
    elif hero_x > SCREEN_WIDTH - hero1_rect.width:
        hero_pos[0] = SCREEN_WIDTH - hero1_rect.width
    else:
        hero_pos[0] = hero_x

    if hero_y < 0:
        hero_pos[1] = 0
    elif hero_y > SCREEN_HEIGHT - hero1_rect.height:
        hero_pos[1] = SCREEN_HEIGHT - hero1_rect.height
    else:
        hero_pos[1] = hero_y

