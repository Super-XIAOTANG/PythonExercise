"""  Python与面向对象OOP 下 """

"""
    __new__方法：创建并返回一个实例对象
    特点：1、该方法时实例化一个对象时调用的第一个方法
         2、至少有一个参数cls，代表要实例化的类，其他参数用来直接传递给init
         3、new方法可以决定是否使用该init，它可以调用其他类的构造方法。如果new没有返回实例对象，则init不会被调用
         4、在new方法中，不能调用自己的new方法，即return cls.__new__(cls)，会报错
    
"""

class Animal:
    def __init__(self):
        self.color = 'red'
        pass

    # 若不重写，默认的__new__函数如下：
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

# 单例模式练习，指某个类在整个系统中只有一个实例对象存在，如回收站、资源管理器。
class DataBaseClass(object):

    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, '_instance'):  # 如果不存在，才进行创建，保证只有一个实例对象
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

    pass

db1 = DataBaseClass()
print(id(db1))
db2 = DataBaseClass()
print(id(db2))  # 发现此时所有实例对象的地址都一样，实现了单例要求

