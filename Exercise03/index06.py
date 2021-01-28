"""  Python与面向对象OOP 下 """

"""
    方法一：
    property(属性函数):为解决只能通过方法来访问私有属性的问题
    特点：若get、set函数只是简单的返回、赋值，那设置私有属性的意义就消失了。一般要在get、set中设置相关逻辑，实现有条件的修改
    
    方法二（更好用一些）：
    装饰器来设置： @property
    语法：1、get、set函数名一致，为映射的对象名，分别用@property、@映射对象名.setter进行修饰。
         2、注意get、set的参数设置固定为：映射对象名（self）、映射对象名（self, parms）
"""

class Person:
    def __init__(self):
        self.__age = 12
        pass
    #
    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, age):
    #     if age < 0:
    #         print('年龄错误!')
    #     else:
    #         self.__age = age
    #         pass
    #     pass
    #
    # # 定义一个类属性映射实现通过直接访问属性的形式去访问私有属性
    # age = property(get_age, set_age)

    @property  # 用装饰器修饰，这里是提供一个getter方法。
    def age(self):
        return self.__age

    @age.setter  # 用age开头，提供一个setter方法。
    def age(self, parms):
        if parms < 0:
            print('年龄错误!')
        else:
            self.__age = parms
            pass
        pass

    pass


AG = Person()
print(AG.age)
AG.age = 18
print(AG.age)
# print(AG.get_age())  # 可以发现，私有属性也发生了变化

