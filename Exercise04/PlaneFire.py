"""  优化：飞机大战  """

import random
import pygame
import os
from pygame.locals import *

# Plane基类
class Plane:
    def __init__(self, screen, imagePath):
        """
        飞机基类的初始化函数
        :param screen: 主窗体对象
        :param imagePath: 加载的图片
        """
        self.screen = screen
        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image, (30,40))
        self.bulletList = []  # 存储所有子弹
        pass

    def display(self):
        """
                飞机在主窗口显示
                :return: 无返回值
        """
        self.screen.blit(self.image, (self.x, self.y))
        # 完善子弹的展示逻辑
        needDelItemList = []
        for item in self.bulletList:
            if item.judge():
                needDelItemList.append(item)
                pass
            pass
        # 重新遍历
        for i in needDelItemList:
            self.bulletList.remove(i)

        for bullet in self.bulletList:
            bullet.display()  # 显示子弹的位置
            bullet.move(type=self.type)  # 显示子弹的移动
        pass

    pass

class HeroPlane(Plane):

    def __init__(self, screen):
        super().__init__(screen, './figure/hero.png')
        self.type = 'hero'
        self.x = 150
        self.y = 440
        pass

    def moveLeft(self):
        """
        左移动
        :return:
        """
        if self.x > 0:
            self.x -= 10
        pass

    def moveRight(self):
        """
        右移动
        :return:
        """
        if self.x < 300:
            self.x += 10
        pass

    def shoot(self):
        bullet = Bullet(self.x, self.y, self.screen, type='hero')
        self.bulletList.append(bullet)
        pass

    pass

class EnemyPlane(Plane):

    def __init__(self, screen):
        super().__init__(screen, './figure/enemy.png')
        self.direction = 'right'
        self.type = 'enemy'
        self.x = 0
        self.y = 0
        pass

    def shoot(self):
        num = random.randint(1,50)
        if num == 3:
            bullet = Bullet(self.x, self.y, self.screen, type='enemy')
            self.bulletList.append(bullet)
        pass

    def move(self):
        if self.direction == 'right':
            self.x += 1
            pass
        elif self.direction == 'left':
            self.x -= 1
            pass
        if self.x >330:
            self.direction = 'left'
            pass
        elif self.x < 0:
            self.direction = 'right'
            pass
        pass

    pass

# 子弹类
class Bullet:

    def __init__(self, x, y, screen, **kwargs):
        self.screen = screen
        for key,parameter in kwargs.items():
            if parameter == 'hero':
                self.x = x + 13
                self.y = y - 20
                self.imagePath = './figure/bullet1.png'
                pass
            elif parameter == 'enemy':
                self.x = x
                self.y = y + 10
                self.imagePath = './figure/bullet2.png'
                pass
        self.image = pygame.image.load(self.imagePath)
        self.image = pygame.transform.scale(self.image, (20, 30))
        pass

    def move(self, **kwargs):
        """
        子弹的移动
        :return:
        """
        for key,parameter in kwargs.items():
            if parameter == 'hero':
                self.y -= 2
            elif parameter == 'enemy':
                self.y += 2
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def judge(self):
        """
        判断子弹是否越界
        :return:
        """
        if self.y >500 or self.y < 0:
            return True
        else:
            return False
        pass

    pass

def key_control(HeroObj):
    """
    实现键盘检测的函数
    :param HeroObj:
    :return:
    """
    # 获取键盘事件
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print('退出')
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                HeroObj.moveLeft()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                HeroObj.moveRight()
            elif event.key == K_SPACE:
                print('K_SPACE')
                HeroObj.shoot()

    pass


if __name__ == '__main__':
    try:
        # 创建一个窗口， 用于显示内容
        screen = pygame.display.set_mode((350, 500), depth=32)
        # 创建一个背景图片
        background = pygame.image.load('./figure/background.jpg')
        # 设定一个标题
        pygame.display.set_caption('经典飞机大战')
        # 添加背景音乐
        pygame.mixer.init()
        pygame.mixer.music.load('./figure/background.mp3')
        pygame.mixer.music.set_volume(0.02)  # 设置音量
        pygame.mixer.music.play(-1)  # -1表示无限循环

        # 添加战机
        hero = HeroPlane(screen)
        # 添加敌机
        enemy = EnemyPlane(screen)
        while True:
            # 设定要显示的内容
            screen.blit(background, (0, 0))
            # 载入战机图像
            hero.display()
            enemy.display()
            enemy.move()
            enemy.shoot()
            # 获取键盘事件
            key_control(hero)
            # 更新显示的内容
            pygame.display.update()
            pygame.time.Clock().tick(100)
    finally:
        os.system('pause')
