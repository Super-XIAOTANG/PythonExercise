"""  Python与面向对象OOP 下 """

"""
    属性的私有化：为保护属性安全，不希望其他人修改，则可将其设置为私有属性。
    语法：变量名通过两个下划线开头，如  __country 
    使用场景：1、把特定属性隐藏起来，不希望类外部直接调用
            2、保护特定属性，不希望外部可以改变属性的值
            3、保护属性，不希望【派生类】继承
            
    特点：1、私有化的【实例属性】不能在外部访问，可以在类内随意使用 
    
    注意：python中也有protected类型变量，以单下划线开头，但是不常用
"""

class Person:

    __country = 'china'  # 私有化的类属性，通过类对象也无法访问

    def __init__(self, name='阿瓜', age=12):
        self.__name = name
        self.age = age

        pass

    def __str__(self):
        return '{}的年龄是{},国家是{}'.format(self.__name, self.age, self.__country)  # 在类内部可以访问私有属性

    def set_country(self):
        self.__country = 'China'
        Person.__country = "LoveChina"

    def get_country(self):
        return Person.__country

    pass

class Student(Person):
    def printInfo(self):
        # print(self.__name)  # 访问父类中的私有属性，不可以
        print(self.age)  # 访问父类的公有属性则没有问题
        pass

    pass


AG = Person('阿瓜', 12)
# print(Person.name)  # 再次注意类对象不能访问实例属性
# print(AG.__name)  # 此时，name属性变为私有化，实例对象不能访问
print(AG)
ZZ = Student()
# print(ZZ.__name)  # 私有属性不能被子类继承
ZZ.printInfo()

AG.set_country()
print(AG.get_country())

"""
    私有化方法：有些方法不允许外部调用，防止子类意外重写
    语法：同私有化属性，在方法名前加两个下划线
        
"""

class Animal:

    def __eat(self):  # 此时，eat函数则为私有化方法
        print('吃东西')
        pass

    def run(self):
        self.__eat()  # 可以在内部调用
        print('飞快的跑')
        pass

    pass

class Bird(Animal):
    pass

bird = Bird()
# bird.eat()  # 发现报错，无此方法
bird.run()

