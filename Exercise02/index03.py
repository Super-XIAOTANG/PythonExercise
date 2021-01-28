"""  匿名函数lambda表达式 与 递归函数  """
"""
    lambda 参数1，参数2，参数3:执行代码语句
    特点：1）类似于一条指令的函数
         2）没有名字
         3）匿名函数冒号后面的表达式有且只有一个，注意是表达式，不是语句
         4）匿名函数自带return， 其结果为表达式计算的结果
    缺点：1）只能是单个表达式，封装有限的逻辑
         2）
"""

# lambda的简单样例
M = lambda x, y: x+y  # 这是声明，需要一个变量来接收 此时M为函数对象
print(M('阿瓜','是憨憨~'))  # 通过M可以调用匿名函数

# 上述lambda表达式等价于：
def test(x, y):
    return x+y

# lambda实现双分支
age = 17
print('可以参军' if age > 18 else '继续上学')
Compare = lambda x, y:x if x>y else y
print(Compare(5, 7))

# 直接调用lambda
rs = (lambda x, y:x if x>y else y)(12, 16)  # 直接调用lambda表达式
print(rs)



# 递归函数
"""
    递归函数：与C语言一致，必须设置结束条件，否则将无限递归
"""
# 用递归函数求阶乘
def Factorial(x):
    if x == 1:
        return 1
    return x * Factorial(x - 1)

print(Factorial(5))



