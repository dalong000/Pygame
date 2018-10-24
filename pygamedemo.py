import pygame
from pygame.locals import *
from sys import exit

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


while True:
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


    offset_x = offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
    offset_y = offset[pygame.K_DOWN] - offset[pygame.K_UP]
    hero_pos = [hero_pos[0] + offset_x, hero_pos[1] + offset_y]

