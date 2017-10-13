import pygame
import time

# 导入按键的检测
from pygame.locals import *


class HeroPlane(object):
    def __init__(self, screen):
        self.x = 240
        self.y = 600
        self.screen = screen
        self.imageName = './feiji/hero.gif'
        self.heroimage = pygame.image.load(self.imageName).convert()
        self.bulletList = []

    def display(self):
        self.screen.blit(self.heroimage, (self.x, self.y))
        # 虽然这里子弹循环无限性，但都是在同一点上
        # 这里当子弹飞出窗口的时候，就可以remove掉子弹了，但是在python中列表删除的漏洞，相邻元素的删除并不彻底，所以
        # 想法是首先去判断子弹是否越界，然后把越界的子弹放到一个列表中，最后直接把列表中的元素删除掉
        # 对象中的属性能不直接取，就不直接取，写一个方法取
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def moveleft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10

    def shootbullet(self):
        newbullet = Bullet(self.x, self.y, self.screen)
        self.bulletList.append(newbullet)

class Bullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen
        self.imageName = './feiji/bullet-3.gif'
        self.heroimage = pygame.image.load(self.imageName).convert()

    def display(self):
        self.screen.blit(self.heroimage, (self.x, self.y))

    def move(self):
        self.y -= 2

if __name__ == "__main__":
    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 800), 0, 32)

    # 2.创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load('./feiji/background.png').convert()

    # 3.创建一个飞机对象
    heroplane = HeroPlane(screen)

    # 3.把背景图片放到窗口中显示
    while True:
        screen.blit(background, (0, 0))

        # 将飞机对象添加到屏幕中去
        heroplane.display()

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
