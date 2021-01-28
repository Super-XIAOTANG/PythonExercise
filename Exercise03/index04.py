"""  Python与面向对象OOP 中 """

"""
    类方法：类对象所拥有的方法。
    特点：1、需要用装饰器 @classmethod来标识
         2、对于类方法，第一个参数必须是类对象cls
         3、类方法可以通过类对象、实例对象调用
         4、在类方法中可以修改类属性
         
    静态方法：类对象所拥有的方法。
    
    使用目的：1、用于静态方法一般存放逻辑性的代码，本身与类及实例对象没有交互。也就是说，一般不会涉及到类中方法和属性的操作。
            2、数字资源能够得到有效的充分利用。
            
    特点：1、需要用@staticmethod来声明
         2、静态方法不需要任何参数
         3、一般情况下，不会通过实例对象访问静态方法。
    
         
"""

class People:

    country = 'china'

    # 类方法声明
    @classmethod
    def get_country(cls):

        return cls.country  # 通过类对象访问类属性
        pass
    pass

    @classmethod
    def change_country(cls):
        cls.country = 'China'

    @staticmethod
    def get_Data():
        return People.country
        pass

    @staticmethod
    def add(x, y):  # 带有参数的静态方法
        return x + y

    def __init__(self, name='阿瓜'):
        self.name = name


AG = People()
# print(People.get_country())
# print(AG.get_country())
# AG.change_country()
# print(AG.country)

print(AG.get_Data())
print(People.get_Data())
print(People.add(2, 5))

# 显示实践demo
import time
class TimeTest:
    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S", time.localtime())
        pass
    pass

print(TimeTest.showTime())
