import pygame
import time
import random

# 导入按键的检测
from pygame.locals import *


class Plane(object):
    def __init__(self, screen, name):
        self.screen = screen
        self.name = name
        self.heroimage = pygame.image.load(self.imageName).convert()
        self.bulletList = []

    def display(self):
        # 更新飞机的位置
        self.screen.blit(self.heroimage, (self.x, self.y))

        # 更新所有发射出去的子弹的位置
        # 虽然这里子弹循环无限性，但都是在同一点上
        # 这里当子弹飞出窗口的时候，就可以remove掉子弹了，但是在python中列表删除的漏洞，相邻元素的删除并不彻底，所以
        # 想法是首先去判断子弹是否越界，然后把越界的子弹放到一个列表中，最后直接把列表中的元素删除掉
        # 对象中的属性能不直接取，就不直接取，写一个方法取

        # 存放需要删除的对象信息
        needDelItemList = []

        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)

        for i in needDelItemList:
            self.bulletList.remove(i)

        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def shootbullet(self):
        newbullet = PublicBullet(self.x, self.y, self.screen, self.name)
        self.bulletList.append(newbullet)


class HeroPlane(Plane):
    def __init__(self, screen, name):
        self.x = 240
        self.y = 600
        self.imageName = './feiji/hero.gif'
        super().__init__(screen, name)

    def moveleft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10


class EnemyPlane(Plane):
    def __init__(self, screen, name):
        self.x = 0
        self.y = 0
        self.imageName = './feiji/enemy-1.gif'
        super().__init__(screen, name)
        self.direction = "right"

    def move(self):
        if self.direction == 'left':
            self.x -= 2
        elif self.direction == 'right':
            self.x += 2

        if self.x == 480 - 50:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

    def shootbullet(self):
        num = random.randint(1, 100)
        if num == 88:
            super().shootbullet()


# class Bullet(object):
#     def __init__(self, x, y, screen):
#         self.x = x + 40
#         self.y = y - 20
#         self.screen = screen
#         self.imageName = './feiji/bullet-3.gif'
#         self.heroimage = pygame.image.load(self.imageName).convert()
#
#     def display(self):
#         self.screen.blit(self.heroimage, (self.x, self.y))
#
#     def move(self):
#         self.y -= 2
#
#     def judge(self):
#         if self.y <0:
#             return True
#         else:
#             return False

# class EnenyBullet(object):
#     def __init__(self, x, y, screen):
#         self.x = x + 15
#         self.y = y + 20
#         self.screen = screen
#         self.imageName = './feiji/bullet-1.gif'
#         self.heroimage = pygame.image.load(self.imageName).convert()
#
#     def display(self):
#         self.screen.blit(self.heroimage, (self.x, self.y))
#
#     def move(self):
#         self.y += 2
#
#     def judge(self):
#         if self.y >800:
#             return True
#         else:
#             return False

class PublicBullet(object):
    def __init__(self, x, y, screen, planeName):
        self.planeName = planeName
        self.screen = screen

        if planeName == 'hero':
            self.x = x + 40
            self.y = y - 20
            imageName = './feiji/bullet-3.gif'

        elif planeName == 'enemy':
            self.x = x + 15
            self.y = y + 20
            imageName = './feiji/bullet-1.gif'

        self.heroimage = pygame.image.load(imageName).convert()

    def display(self):
        self.screen.blit(self.heroimage, (self.x, self.y))

    def move(self):
        if self.planeName == 'enemy':
            self.y += 2
        elif self.planeName == 'hero':
            self.y -= 2

    def judge(self):
        if self.y > 800 or self.y < 0:
            return True
        else:
            return False


if __name__ == "__main__":
    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 800), 0, 32)

    # 2.创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load('./feiji/background.png').convert()

    # 3.创建一个飞机对象
    heroplane = HeroPlane(screen, 'hero')

    # 4.创建一个敌人飞机对象
    enemyplane = EnemyPlane(screen, 'enemy')

    # 3.把背景图片放到窗口中显示
    while True:
        screen.blit(background, (0, 0))

        # 将飞机对象添加到屏幕中去
        heroplane.display()
        enemyplane.display()
        enemyplane.move()
        enemyplane.shootbullet()

        # 判断是否点击了退出按钮
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    heroplane.moveleft()
                    print('left')
                elif event.key == K_d or event.key == K_RIGHT:
                    heroplane.moveRight()
                    print('right')
                elif event.key == K_SPACE:
                    heroplane.shootbullet()
                    print('space')

        time.sleep(0.01)

        pygame.display.update()
