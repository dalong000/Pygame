import pygame
from pygame.locals import *
from sys import exit

#定义窗口分辨率
SCREEN_WIDTH = 390
SCREEN_HEIGHT = 520
#初始化游戏
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])#初始化窗口
pygame.display.set_caption('gamedemo')#设置标题
#载入背景
background = pygame.image.load('resources/image/background.PNG')


while True:
    #绘制背景
    screen.blit(background, (0,0))
    #更新屏幕
    pygame.display.update()
    #处理游戏退出
    #从消息队列中读取消息
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()