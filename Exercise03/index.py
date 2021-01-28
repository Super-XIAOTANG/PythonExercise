"""  Python与面向对象OOP 上 """

# 类和对象
"""
    类的组成：1、类的名称
            2、类的属性：一组数据
            3、类的方法：允许对数据进行的操作、行为
    
    定义类：
        class 类名:
            属性
            方法
    定义对象：
        对象名 = 类名（）        
"""

class Person:   # 类名一般采用大骆驼的命名方法，更加规范
    # 属性
    name = '阿瓜'
    age = 12

    # 方法
    def eat(self):
        print('大口大口的吃饭')
        pass

    def run(self):
        print('慢慢的跑')
        pass

AG = Person()
AG.eat()
AG.run()  # 可以像C++一样调用类函数
print("{}的年龄是：{}".format(AG.name, AG.age))

"""
    类的实例方法：1、在类内部，使用def关键字可以定义一个实例方法。与一般函数定义不同，类方法必须包含参数self，且为第一个参数。
               2、实例方法是归属于类的实例所有。
    
    类属性：在类中定义的，但不是在类方法中定义的属性为类属性
    
    实例属性：在实例方法中定义的属性成为实例属性
    
    __init__方法：1、python自带的内置函数，具有特殊的函数 是用双下划线包起来的【魔术方法】
                 2、是一个初始化的方法，用来定义实例属性和初始化数据，在创建对象的时候自动调用
                 3、利用传参的机制可以让我们定义功能更加强大、方便
                 
"""

class People:

    # __init__初始化方法
    def __init__(self, name='阿瓜', age=12):  # 此处的赋值为默认初始值, 类似于C++构造函数
        self.name = name
        self.age = age
        print('self的地址为%d' % id(self))

    def eat(self):
        print('喜欢吃榴莲')
    pass

AG = People()
AG.name = '阿瓜'
AG.sex = '小仙女'  # 个人感觉不太规范的实例属性添加方法，这样添加应该只属于AG，其他类对象需要继续添加

ZZ = People()
print(ZZ.name)
ZZ.name = '崽崽'
print(ZZ.name)

"""
    self: 个人感觉类似于C++中的 this。 可以认为self就是对象的引用。
          1）self只有在定义实例方法是才有意义，在调用的时候不需传入相应的参数
          2）self的名称可以更改，只是约定俗成定义为self
          3）self指的是类对象本身，相当于C++、Java中的this  
"""
print(id(ZZ))  # 可以看到self的地址和类对象的地址是一样的


"""
    python中的【魔术方法】，一般具有特殊的含义，不需要手动调用。常用【魔术方法】如下：
    __init__:初始化一个类，在创建对象时赋值使用
    __str__:在将对象转化为字符串str测试的时候使用，打印对象的信息
    __new__:创建并返回一个实例对象，调用一次就会得到一个对象
    __class__:获得已知对象的类
    __del__:对象在程序运行结束后进行销毁的时候调用的方法，用于释放资源，类似于析构函数。

    个人感觉像是约定了特定功能的函数，比如init就是初始化，str就是自定义输出格式
"""

class Animal:
    # 初始化
    def __init__(self, name='小黄', colour='黄色'):
        self.name = name
        self.colour = colour
        print('-----init执行-----')

    def __str__(self):
        """
        打印对象，自定义对象输出的格式
        :return: 返回输出格式字符串
        """
        return '我的名字是%s，我的颜色为%s' % (self.name, self.colour)

    def __new__(cls, *args, **kwargs):
        """
        创建对象实例的方法，每调用一次，就生成一个新对象。 cls是class的缩写
        使用场景：可以控制创建对象的一些属性限定，在涉及单例模式的时候来使用
        :param args:
        :param kwargs:
        """
        print('-----new执行-----')
        return object.__new__(cls)  # 在这里是创建对象实例
        # 根据结果发现，先执行new函数，new函数返回后才会再执行init函数。

    def __del__(self):
        print("------析构函数方法调用------")
        pass

Dog = Animal()
print(Dog)   # 可以发现定义了str后，print输出的内容更改为自定义的格式
