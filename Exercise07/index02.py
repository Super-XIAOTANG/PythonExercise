"""  Python中的垃圾回收机制：引用计数机制为主，标记清除和分代收集两种机制为辅  """

"""
    GC负责的主要任务：1、为新生成的对象分配内存
                   2、识别那些垃圾对象
                   3、从垃圾对象那里回收内存
    
    触发垃圾回收的三种情况：1、gc模块的计数器达到阀值的时候，自动回收垃圾
                       2、调用gc。collect(),手动回收垃圾
                       3、程序退出的时候，python解释器来回收垃圾
                                      
"""

"""
    标记-清除机制：首先标记对象（垃圾检测），然后清除垃圾（垃圾回收）  
"""

"""
    分带回收：将对象分为0，1，2三代，随后采取一定的逻辑进行删除垃圾对象    
"""


import os
import gc
import psutil

def showMemSize(tag):
    pid = os.getpid()  # 进程id
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss/1024/1024
    print('{} memory used:{} MB'.format(tag, memory))
    pass


# 验证循环引用的情况
def func():
    showMemSize('初始化')
    a = [i for i in range(100000)]
    b = [i for i in range(100000)]

    # 关联引用
    a.append(b)
    b.append(a)
    showMemSize('创建了a、b之后')
    # del a
    # del b  # 发现即使用了del 也无法释放
    pass


if __name__ == '__main__':
    func()
    print(gc.get_threshold())
    gc.collect() # 手动释放，发现a、b被释放
    showMemSize('函数执行完成之后')  # 发现函数func()内的局部变量并没有被释放
