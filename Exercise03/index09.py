"""  Python与面向对象OOP 下 """

"""
    动态语言：运行时可以改变器结构的语言，python可以在程序中运行中添加属性和方法
    
    
"""
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def __str__(self):
        return '{}今年{}岁了'.format(self.name, self.age)

    def printII(self):

        pass

    pass

AG = Student('阿瓜', 12)
AG.weight = 92  # 动态添加体重属性 实例属性
Student.school = '大工'  # 动态添加类属性
print(AG)
print(AG.school)

# 动态添加实例方法
import types  # 导入第三方库，实现动态添加方法

def dymicMethod(self):
    print('{}目前就读于{}'.format(self.name, self.school))
    pass

AG.printInfo = types.MethodType(dymicMethod, AG)  # 给类对象绑定方法动态的绑定方法
AG.printInfo()  # 调用绑定的方法

@classmethod
def classTest(cls):
    print('这是一个类方法')
    pass

@staticmethod
def staticMethod():
    print('这是一个静态方法')
    pass

Student.TestMethod = classTest  # 动态绑定类方法，更加简便
AG.TestMethod()

Student.StaticTestMethod = staticMethod  # 动态绑定类方法，更加简便
AG.StaticTestMethod()
