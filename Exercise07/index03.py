"""  Python中的垃圾回收机制：引用计数机制为主，标记清除和分代收集两种机制为辅  """

"""
    内存优化：
    
    1、小整数与大整数对象池：为避免频繁的申请和销毁内存空间，提前建立好相应的对象。
        python中的小整数是[-5, 256]，python会提前创建好这些数值
        
"""


a = 100
b = 100
print(id(a))
print(id(b))  # a 与 b的地址是一样的
del a
del b
c = 100
print(id(c))   # 发现即使删除了a、b地址还是没有变化 说明100的地址已经是固定的，提前创建好的


bigA = 10000
bigB = 10000
print(id(bigA))
print(id(bigB))
del bigA
del bigB

bigC = 10000
print(id(bigC))  # 发现此时big(A、B、C)的地址仍然是一样的 但是每次执行的地址会变化 也就是说大整数没有提前创建

