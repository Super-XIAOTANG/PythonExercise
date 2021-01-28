"""  Python与面向对象OOP 中 """

"""
    类属性：就是类对象所拥有的属性，可以被所有的类对象（即通过类名访问）和实例对象访问
    实例属性：实例对象所拥有的属性，只能通过实例对象（即对象的实例）访问
    访问时，实例对象会现在自身寻找，然后再去类对象中寻找。
"""

class Student:

    name = '阿瓜'  # 属于类属性

    def __init__(self, age):
        self.age = age  # 属于实例属性
        # self.name = '崽崽'
        pass
    pass

AG = Student(12)
print(AG.name)  # 若实例对象自身就有name 那么根据访问顺序输出自身的属性值，而‘阿瓜’被覆盖
AG.name = '阿瓜瓜'  # 这相当于是AG这个实例对象自己申请了一个name新的实例属性，并没有修改共有的类属性
ZZ = Student(12)
JY = Student(12)
print(AG.name)
print(ZZ.name)
print(id(AG.name))
print(id(ZZ.name))
print(id(JY.name))  # 可以看到类对象为所有实例对象共有的，且只有一份。
# 通过Student 去访问属性
print(Student.name)
Student.name = '阿瓜瓜'  # 要想修改类类属性就要用类对象进行修改
# print(Student.age)  # 这里会报错

