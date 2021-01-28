"""  飞机大战  """
import random
import pygame

from pygame.locals import *

"""
    搭建主界面：有点类似于Qt，可以设置背景、标题、图标等等        
"""

class HeroPlane:
    """
        飞机类，实现飞机的显示，并且可以控制飞机移动
    """
    def __init__(self, screen, local):
        """
        初始化函数
        """
        self.x = 150
        self.y = 440
        # 设置要显示的窗口
        self.screen = screen
        # 载入飞机的图片
        self.image = pygame.image.load(local)
        self.image = pygame.transform.scale(self.image, (50, 60))
        # 子弹列表
        self.bulletList = []
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
        if self.x <300:
            self.x += 10
        pass

    def display(self):
        """
        飞机在主窗口显示
        :return:
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
            bullet.display() # 显示子弹的位置
            bullet.move()  # 显示子弹的移动
        pass

    # 发射子弹
    def shoot(self):
        bullet = Bullet(self.x, self.y, self.screen, './figure/bullet1.png')
        self.bulletList.append(bullet)
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


class Bullet:
    """
        子弹类， 实现攻击相关功能
    """
    def __init__(self, x, y, screen, local):
        """
        子弹初始化函数
        :param x: 横坐标
        :param y: 纵坐标
        :param screen: 展示的主界面
        """
        self.x = x +13
        self.y = y+ 20
        self.screen = screen
        self.image = pygame.image.load(local)
        self.image = pygame.transform.scale(self.image, (20,30))
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def move(self):
        self.y -= 1
        pass

    def judge(self):
        """
        判断子弹是否越界
        :return:
        """
        if self.y<0:
            return True
        else:
            return False
        pass
    pass

class EnemyPlane:
    """
        敌机，个人感觉重复，不用这个也行
    """
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        # 设置显示窗口
        self.screen = screen
        # 生成飞机图像
        self.image = pygame.image.load('./figure/enemy.png')
        self.image = pygame.transform.scale(self.image, (30,40))
        self.bulletList = []

        # 设置移动方向
        self.direction = 'right'
        pass

    def display(self):
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
            bullet.move()  # 显示子弹的移动
        pass

    def shoot(self):
        num = random.randint(1,50)
        if num == 3:
            bullet = EnemyBullet(self.x, self.y, self.screen)
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

class EnemyBullet:
    def __init__(self, x, y, screen):
        """
        :param x: 横坐标
        :param y: 纵坐标
        :param screen: 显示的主界面
        """
        self.x = x
        self.y = y + 10
        self.screen = screen
        self.image = pygame.image.load('./figure/bullet2.png')
        self.image = pygame.transform.scale(self.image, (20, 30))
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def move(self):
        self.y += 1
        pass

    def judge(self):
        if self.y > 500:
            return True
        else:
            return False
    pass

def main():
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
    hero = HeroPlane(screen, './figure/hero.png')
    # 添加敌机
    enemy = EnemyPlane(screen)
    while True:
        # 设定要显示的内容
        screen.blit(background, (0,0))
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

    pass







# 程序入口的规范写法
if __name__ == '__main__':
    main()


