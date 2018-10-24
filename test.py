import pygame  # 导入pygame库
from pygame.locals import *  # 导入pygame库中的一些常量
from sys import exit  # 导入sys库中的exit函数

# 定义窗口的分辨率
SCREEN_WIDTH = 390
SCREEN_HEIGHT = 520

ticks = 0
# dict == new add ==
offset = {pygame.K_LEFT: 0, pygame.K_RIGHT: 0, pygame.K_UP: 0, pygame.K_DOWN: 0}
# dict == new add ==

# 初始化游戏
pygame.init()  # 初始化pygame
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])  # 初始化窗口
pygame.display.set_caption('This is my first pygame-program')  # 设置窗口标题

# 载入背景图
background = pygame.image.load('resources/image/background.png')

# 载入飞机图片
shoot_img = pygame.image.load('resources/image/shoot.png')
# 用subsurface剪切读入的图片
hero1_rect = pygame.Rect(10, 100, 99, 126)
hero2_rect = pygame.Rect(40, 100, 99, 126)
hero1 = shoot_img.subsurface(hero1_rect)
hero2 = shoot_img.subsurface(hero2_rect)
hero_pos = [200, 500]

# 事件循环(main loop)
while True:

    # 绘制背景
    screen.blit(background, (0, 0))

    # 绘制飞机
    if ticks % 50 < 25:
        screen.blit(hero1, hero_pos)
    else:
        screen.blit(hero2, hero_pos)
    ticks += 1  # python已略去自增运算符

    # 更新屏幕
    pygame.display.update()

    # 处理游戏退出
    # 从消息队列中循环取
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Python中没有switch-case 多用字典类型替代
        # 控制方向 == new add ==
        if event.type == pygame.KEYDOWN:
            if event.key in offset:
                offset[event.key] = 3
        elif event.type == pygame.KEYUP:
            if event.key in offset:
                offset[event.key] = 0

        # part 1
        # offset_x = offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
        # offset_y = offset[pygame.K_DOWN] - offset[pygame.K_UP]
        # hero_pos = [hero_pos[0] + offset_x, hero_pos[1] + offset_y]
    # part 2
    offset_x = offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
    offset_y = offset[pygame.K_DOWN] - offset[pygame.K_UP]
    hero_pos = [hero_pos[0] + offset_x, hero_pos[1] + offset_y]
    # 控制方向 == new add ==
