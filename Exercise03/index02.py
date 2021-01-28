"""  Python与面向对象OOP 中 """

"""
    面向对象的三大特征：封装、继承、多态
    封装：指把内容封装到某个地方，以便于后面的使用。
    继承：即子类可以继承父类的内容【属性和行为】。
    多态：同一个行为，对不同的子类对象，有不同的行为表现。
"""

#
# class Animal:
#     """
#     各种动物的父类
#     """
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         """
#         吃
#         :return:
#         """
#         pass
#
#     def drink(self):
#         """
#         喝
#         :return:
#         """
#         pass
#
#     # def sajiao(self):
#     #     print("Animal撒娇")
#     #     pass
# """
#     继承语法：1、class 类名(父类名):
#             2、任何类都默认继承Object，即class 类名(Object):
#             3、通过继承，子类可以继承父类公共的属性和方法
#             4、多继承中，若出现同名函数的查找顺序为：在本类中查找 → 按继承顺序在父类中查找 → 在父类的父类中查找
#             5、继承的传递性：在Python中，理论上可以无限的传递
#             6、函数的重写：子类中可以重写父类中的方法，即按照4中的搜索顺寻可以覆盖掉父类的方法，以满足新的功能。
#             7、可通过类名、super关键字两种方式去调用父类的方法。
#
# """
#
# class Pet:
#     pass
#     def sajiao(self):
#         """
#         撒娇
#         :return:
#         """
#         print("Pet撒娇")
#         pass
#
#
# class Dog(Animal):  # 单继承举例
#     def __init__(self, name, age):
#         # 调用父类的构造函数
#         Animal.__init__(self, name, age)
#         # 另一种方法 super
#         super.__init__(name, age)
#         pass
#
#
#     def wwj(self):
#         print('小狗汪汪叫')
#     pass
#
# class Cat(Animal, Pet):  # 多继承举例
#     def mmj(self):
#         print('小猫喵喵叫')
#     pass
#
#     # def sajiao(self):
#     #     """
#     #     撒娇
#     #     :return:
#     #     """
#     #     print("Cat撒娇")
#     #     pass
#
#
# dog = Dog()
# dog.eat()  # 通过继承，Dog类已经具备eat行为
#
# cat = Cat()
# cat.sajiao()
# print(Cat.__mro__)  # 打印类的依次继承关系，根据结果可知为 Cat-Pet-BasePet-Animal-BaseAnimal-Object


"""
    多态语法：Python的多态崇尚【鸭子类型】。Python本身是弱类型语言，天生支持多态
    两个前提：1、继承：多态必须发生在父类和子类之间
            2、重写：子类重写父类的方法
    特点：灵活性、扩展性。个人感觉Python通过搜索顺序实现了多态。
    【鸭子类型】：是一种动态类型的风格，关注的不是对象的类型本身，而是关注对象是如何使用的。
"""

class Animal:
    """
    动物父类
    """
    def say_who(self):
        print("我是一个动物!")
        pass

    pass

class Duck(Animal):
    """
    鸭子子类
    """
    def say_who(self):
        super(Duck, self).say_who()  # 这样可以调用父类的实例方法
        print("我是一个漂亮的鸭子!")
        pass

    pass

class Dog(Animal):
    """

    """
    def say_who(self):
        super(Dog, self).say_who()  # 这样可以调用父类的实例方法
        print("我是一个漂亮的小狗!")
        pass

    pass



# duck = Duck()
# duck.say_who()
#
# dog = Dog()
# dog.say_who()

# 完整的多态
def commonInvoke(obj):
    """
    统一调用方法
    :param obj:
    :return:
    """
    obj.say_who()
    pass

listObj = [Duck(), Dog()]
for item in listObj:
    commonInvoke(item)
    pass
