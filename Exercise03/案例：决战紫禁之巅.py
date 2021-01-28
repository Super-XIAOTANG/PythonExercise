class Player:

    def __init__(self, name, blood=100):
        """
        初始化函数
        :param name: 玩家姓名
        :param blood: 玩家剩余血量
        """
        self.name = name
        self.blood = blood

    def __str__(self):
        return '【%s】的剩余血量为%s' % (self.name, self.blood)

    def tong(self, enemy):
        """
        捅了对方一刀
        :param enemy:敌人
        :return: null
        """
        enemy.blood -= 10
        info = '【%s】捅了【%s】一刀' % (self.name, enemy.name)
        print(info)
        pass

    def kanren(self, enemy):
        """
        砍了对方一刀
        :param enemy: 敌人
        :return: null
        """
        enemy.blood -= 15
        info = '【%s】砍了【%s】一刀' % (self.name, enemy.name)
        print(info)
        pass

    def chiyao(self):
        self.blood += 10
        info = '【%s】吃了补血药，增加10滴血' % self.name
        print(info)
        pass

p1 = Player('西门吹雪')
p2 = Player('叶孤城')

p1.tong(p2)
print(p2)
p2.kanren(p1)
print(p1)
