"""  Python中的垃圾回收机制：引用计数机制为主，标记清除和分代收集两种机制为辅  """

"""
    引用计数机制：python里的每个东西都是对象，它们的核心就是一个结构体：PyObject
    PyObject是每个对象必有的内容，其中ob_refcnt就是引用计数，当一个对象有新的引用时，它的ob_refcnt就会增加，反之减少，当其为0是，对象的生命周期就结束了
    特点：1、简单、实时性
         2、维护引用计数会消耗资源
         3、循环引用导致计数为1，无法删除
"""

import sys


a = []
print(sys.getrefcount(a))  # 结果为2，代表有两次引用：创建一次，getrefcount调用一次

b = a
print(sys.getrefcount(a))  # 结果为3, 这种函数运行完之后自动就减下去了
c = b
d = b
e = c
f = e
g = d  # 这些赋值也与a有关，也算是a的引用。
print(sys.getrefcount(a))  # a的引用次数为8