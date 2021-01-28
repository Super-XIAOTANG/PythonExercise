"""  Python与面向对象OOP 下 """

"""
    __slots__属性：python允许动态的添加属性、方法。如果要限制运行的时候添加，则可定义一个特殊的slots变量来进行限制。
    特点：1、只有在slots中的属性才可以添加，否则添加失败
         2、__slots__不会被继承，只在当前类有效
         3、slots后面是元组类型，内部是字符串4
         4、可通过print（类名.__slots__）展示
         5、没有dict可以节省空间
"""

class Student:
    # 若不做限制，可以添加任何属性、方法

    __slots__ = ('name', 'age')
    pass

AG = Student()
AG.name = '阿瓜'
AG.age = 12
# AG.school = '大工'  # 添加失败，school不在slots的范围内因此添加失败
# print(AG.__slots__)
# print(AG.__dict__)  # 所有可以用的属性都会存储在这里，但是设置了slots时不能访问

# 在继承关系中使用slots
class SubStudent(Student):

    __slots__ = ('gender',)  # 若子类再次声明了slots，则这个slots的范围是子类与父类的并集，注意不要与父类声明同样的限制
    pass

ZZ = SubStudent()
ZZ.name = '崽崽'
ZZ.gender = '男'  # 发现添加成功，即slots属性不会影响派生类
# rint(ZZ.__dict__)
