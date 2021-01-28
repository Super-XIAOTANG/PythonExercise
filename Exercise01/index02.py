"""  Python的流程控制结构  """

a, b = 1, 10
# if-elif-else语句与if语句的嵌套
if a>b:
    print("a>b")
elif a==b:
    pass  # pass关键字不做任何事情，一般用作占位语句保持程序结构的完整性
else:
    print("a<b")

# while循环
"""
    1、语法结构
    while 条件表达式:
        代码指令
        代码指令
        ......
    
    2、语法特点
        1）有初始值、条件表达式
        2）变量【循环体内计数变量】的自增自减    
        3）一般用于循环次数不确定、依靠循环条件来结束的情况
"""
# 打印九九乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("{}*{}={}".format(row, col, row*col), end=" ")  # 通过修改end调整输出结尾，默认为换行
        col += 1
        pass
    print()
    row += 1
    pass


# for循环
"""
    1、语法结构
    for 临时变量 in 迭代字符串、列表等:
        代码指令
        代码指令
        ......
   
    2、语法特点
        1）遍历集合容器中的每个值  
        2）break 直接结束本层循环
        3）continue 结束本次循环，继续进行下次循环 
"""
tags = "我是一个中国人"
for item in tags:
    print(item)
    pass

# range 此函数可以生成一个数据集合列表
# range(起始值：结束值：步长) 其中步长默认为1
print(type(range(1, 100)))
for data in range(1, 101):  # 括号为左闭右开区间
    print(data, end=" ")

print()

# for--else 结构，用于寻找某一特殊结构
for item in range(1, 11):
    print(item, end=" ")
    if item > 5:
        break
    pass
else:
    print("在上述循环中，如果出现了break，那么else代码将不再执行")


# while--else 结构
index = 1
while index <= 5:
    print(index)
    if index == 6:
        break
    index += 1
    pass
else:
    print("在上述循环中，如果出现了break，那么else代码将不再执行")