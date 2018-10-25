# -*- coding = -utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_surface, enemy_init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = enemy_init_pos
        self.speed = 2
        #爆炸动画索引
        self.down_index = 0

    def update(self):
        self.rect.top += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_surface, bullet_init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = bullet_init_pos
        self.speed = 8
    #控制子弹移动
    def update(self):
        self.rect.top -= self.speed
        if self.rect.top < -self.rect.height:
            self.kill()


class Hero(pygame.sprite.Sprite):
    def __init__(self, hero_surface, hero_init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = hero_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = hero_init_pos
        self.speed = 6
        self.bullets1 = pygame.sprite.Group()

    def single_shoot(self,bullet1_surface):
        bullet1 = Bullet(bullet1_surface, self.rect.midtop)
        self.bullets1.add(bullet1)


    def move(self,offset):
        x = self.rect.left + offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
        y = self.rect.top + offset[pygame.K_DOWN] - offset[pygame.K_UP]
        if x < 0:
            self.rect.left = 0
        elif x > SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left = x

        if y < 0:
            self.rect.top = 0
        elif y > SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top = y




#定义窗口分辨率
SCREEN_WIDTH = 390
SCREEN_HEIGHT = 520

#定义画面帧率
FRAME_RATE = 60

#定义动画周期（帧数）
ANIMATE_CYCLE = 30

#周期变量
ticks = 0
#dict


clock = pygame.time.Clock()
offset = {pygame.K_LEFT:0, pygame.K_RIGHT:0, pygame.K_UP:0, pygame.K_DOWN:0}

#初始化游戏
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])#初始化窗口
pygame.display.set_caption('gamedemo')#设置标题
#载入背景
background = pygame.image.load('resources/image/background.PNG')

#游戏结束图
gameover = pygame.image.load('resources/image/sunqian.JPG')

#载入飞机图片
shoot_img = pygame.image.load('resources/image/shoot.png')
#使用subsurface剪切载入的图片
hero_surface = []
hero_surface.append(shoot_img.subsurface(pygame.Rect(10,100,99,126)))
hero_surface.append(shoot_img.subsurface(pygame.Rect(40,100,99,126)))
'''
hero1_rect = pygame.Rect(10,100,99,126)
hero2_rect = pygame.Rect(40,100,99,126)
hero1 = shoot_img.subsurface(hero1_rect)
hero2 = shoot_img.subsurface(hero2_rect)
'''
hero_pos = [200 ,500]


#创建玩家
hero = Hero(hero_surface[0],hero_pos)

#创建敌人组
enemy1_group = pygame.sprite.Group()

#敌人坠毁组
enemy1_down_group = pygame.sprite.Group()


#bullet1子弹图片
bullet1_surface = shoot_img.subsurface(pygame.Rect(12,234,9,21))

#敌人类图片
enemy1_surface = shoot_img.subsurface(pygame.Rect(32,34,45,34))
enemy1_down_surface = []
enemy1_down_surface.append(shoot_img.subsurface(pygame.Rect(67,47,57,43)))
enemy1_down_surface.append(shoot_img.subsurface(pygame.Rect(73,97,57,43)))
enemy1_down_surface.append(shoot_img.subsurface(pygame.Rect(67,96,57,43)))
enemy1_down_surface.append(shoot_img.subsurface(pygame.Rect(30,97,57,43)))






#事件循环
while True:
    #clock.tick(60)
    #控制游戏最大帧率
    clock.tick(FRAME_RATE)
    #绘制背景
    screen.blit(background, (0,0))
    #改变飞机动画
    if ticks >=ANIMATE_CYCLE:
        ticks = 0
    hero.image = hero_surface[ticks//(ANIMATE_CYCLE//2)]

    #绘制飞机
    screen.blit(hero.image,hero.rect)
    ticks += 1


    #射击
    if ticks % 10 == 0:
        hero.single_shoot(bullet1_surface)
    #控制子弹
    hero.bullets1.update()
    #绘制子弹
    hero.bullets1.draw(screen)

    #产生敌机
    if ticks % 30 == 0:
        enemy = Enemy(enemy1_surface,[randint(0,SCREEN_WIDTH - enemy1_surface.get_width()), -enemy1_surface.get_height()])
        enemy1_group.add(enemy)
    #控制敌机
    enemy1_group.update()
    #绘制敌机
    enemy1_group.draw(screen)

    #检测敌机与子弹碰撞
    enemy1_down_group.add(pygame.sprite.groupcollide(enemy1_group, hero.bullets1, True,True))
    for enemy1_down in enemy1_down_group:
        screen.blit(enemy1_down_surface[enemy1_down.down_index], enemy1_down.rect)
        if ticks % (ANIMATE_CYCLE//2) ==0:
            if enemy1_down.down_index < 3:
                enemy1_down.down_index += 1
            else:
                enemy1_down_group.remove(enemy1_down)

    enemy1_down_list = pygame.sprite.spritecollide(hero, enemy1_group, True)
    if len(enemy1_down_list) > 0:
        enemy1_down_group.add(enemy1_down_list)
        hero.is_hit = True





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


    hero.move(offset)

screen.blit(gameover,(0,0))

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()