"""  Python中的函数  """

# 函数基础
"""
    函数：有独立功能的代码块
    特点；1)实现代码的复用，最小化冗余代码，保证整体代码结构清晰、问题局部化。
         2）重点包括函数定义、调用、说明文档
         3）调用之前必须先定义
         4）def 函数名(): 后接代码块
         5)Python中的函数对参数和返回值的类型没有限制，比较灵活
"""

def printInfo(name, sNumber):
    """
    这里是函数的说明文档，可对函数功能进行说明
    本函数用来输出：hello function
    """
    print("{}的学号是{}".format(name, sNumber))
    print("%s的学号是%s" % (name, sNumber))
    pass

printInfo('阿瓜', 201992140)

# 函数的参数列表
"""
    函数参数：是函数为了实现某项特定功能，所需要使用的数据
    参数特点：不需要指定类型
    参数分类：1）必选参数
            2）默认参数（缺省参数）
            3）可选参数
            4）关键字参数
"""
# 必选参数（缺省参数）
def mySum(index):
    Sum = 0
    Sum += index
    print(Sum)
    return Sum

# 缺省参数
def mySum2(a=10, b=20):  # 同c语言一样，有默认值的参数要放在右侧
    Sum = a + b
    print(Sum)
    pass

mySum2(1)

# 可选参数（不定长参数）
def getCompute(*args):
    """
    计算累加和
    :param args: 可变长的参数类型,需要循环进行操作
    :return:
    """
    result = 0
    for item in args:
        result += item
    print("result = %d" % result)

getCompute(1, 2, 3, 4, 5, 6)

# 关键字参数: 也是可变的，用**来定义，
# 再函数体内 参数关键字是一个字典类型，且key是一个字符串
def keyFunc(**kwargs):
    print(kwargs)
    pass

# keyFunc(1, 2, 3) 需要字典类型，这样是错误的
dictA={"name":"阿瓜", "age":12}
keyFunc(**dictA)
keyFunc(name='peter', age=26)  # 即关键字参数需要以键值对的方式传递，或像上一行那样在字典变量前加**

# 混合使用
def complexFunc(*args, **kwargs):
    print(args)
    print(kwargs)

# def testFunc(**kwargs, *args): 这样的定义方式是错误的，可选参数必须放到关键字参数之前

complexFunc(1, 2, 3, 4)  # 这样会把这些数据以元组的方式赋值给第一个变量
complexFunc(name='阿瓜')  # 键值对会赋给第二个变量
complexFunc(1, 2, 3, 4, name='阿瓜')  # 后面的键值对会赋给第二个变量

# 函数的返回值
"""
    返回值：函数执行完后会返回一个对象，如果在函数内有return 就可以返回实际值，否则返回None
    类型：可以返回任意类型，取决于return后面的类型
    用途：给调用方返回数据    
    特点：1）在一个函数体内可以出现多个return值，但肯定只能返回一个return
         2）return意味着函数执行完毕，其后边的代码将不再执行
"""

def Sum02(a, b):
    Sum = a + b
    return Sum  # 返回给调用者
    pass

print(Sum02(10, 30))

def returnTuple():
    """
    返回元组类型数据
    :return:
    """
    return [1, 2, 3]  # 返回一个列表
    # return 1, 2, 3  # 返回一个元组
    # return {'name':'测试'}  # 返回一个字典
print(type(returnTuple()))

# 函数的嵌套调用
def func1():
    print("-------------func1 start-------------")
    print("-------------func1 执行  -------------")
    print("-------------func1 end-------------")
    pass

def func2():
    print("-------------func2 start-------------")
    # 调用func1
    func1()
    print("-------------func2 end-------------")
    pass

func2()
