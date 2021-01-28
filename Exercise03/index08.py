"""  Python与面向对象OOP 下 """

"""
    python中的异常处理:
    语法格式：
        try:
            可能出现错误的代码块
        except:
            出现错误后执行的代码块
        else:
            没有出现错误执行的代码块
        finally:
            不管是否出错都要执行的代码块
"""

try:
    # print(b)  # 捕获逻辑的代码
    li = [1, 2, 3]
    print(li[10])
    pass
except NameError as msg:
    #  捕获到错误，下面的代码才会执行
    print(msg)
    pass
except IndexError as msg:
    # except代码块可以有多个去处理不同类型的错误
    print(msg)
    pass

def A(s):
    return 10/int(s)
    pass

def B(s):
    return A(s)*2

def main():
    try:  # 可以在调用最后统一处理异常
        A('0')
    except Exception as e:
        print(e)
        pass
    pass

main()

# try-except-else-finally

try:
    print(aa)
    pass
except Exception as msg:
    print(msg)
    pass
else:
    print("没错误的情况下，我会执行")
finally:
    print("不管有没有错误，我都会执行")

# 自定义异常：直接或间接继承Error或者Exception
# 使用raise关键字抛出异常

class LenException(Exception):
    def __init__(self, len):
        """
        初始化函数
        :param len:长度
        """
        self.length = len
        pass

    def __str__(self):
        return '您输入的长度是{}'.format(self.length)+'超过长度了'

    pass

def name_Test():
    name = input('请输入姓名：')
    try:
        if len(name) > 4:
            raise LenException(len(name))
            pass
        else:
            print(name)
            pass
        pass
    except LenException as e:
        print(e)
        pass
    finally:
        print('执行完毕')

name_Test()



