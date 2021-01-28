"""  python模块的制作  """

"""
    python模块：1、python文件都可以做一个模块，模块的名字就是文件的名字
               2、不同模块可以定义相同的变量名，但是其作用域只是在本模块中
               3、可分为：内置模块、自定义模块、第三方模块
"""

# 在from ... import * 时，只有列表内的函数才能被引用
# 但是import 模块名 这样不影响
__all__ = ['add', 'diff']

def add(x, y):
    """
    普通的相加函数
    :param x: 加数
    :param y: 加数
    :return: 返回结果
    """
    return x + y

def diff(x, y):
    """
    普通的相加函数
    :param x: 被减数
    :param y: 减数
    :return: 返回结果
    """
    return x - y

def printInfo():
    print('这是我自定义模块中的方法')
    pass


if __name__ == '__main__':
    # 测试: 这样在别的文件引用该模块时，下面的代码页会被输出，所以通过__name__魔术变量来解决
    print('模块测试:{}'.format(add(2, 5)))
    # print('模块__name__变量=%s' % __name__) 只有在本文件执行时，__name__才是__main__，在其他文件引用的时候就不是了
