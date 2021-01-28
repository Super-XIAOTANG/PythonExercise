"""  内置函数与序列操作  """
# 内置函数就是Python已经定义好的函数
"""
    内置函数-数学运算
    abs():绝对值
    round():对浮点数取近似值
    pow():幂运算
    divmod():求商和余
    max():最大值
    min():最小值
    sum():求和
    eval(): 动态执行一个字符串表达式，并返回值
"""
a, b, c = 1, 2, 3
print(eval('a + b + c'),)


"""
    内置函数-类型转换
    int() float()
    str() ord()：将字符转化为对应整数
    chr()：字符 bool()
    bin() ：整数转为二进制字符串 hex()：整数转为十六进制字符串oct()：整数转为八进制字符串 
    list()  tuple() 
    dict() bytes()
"""

print(bin(10))  # 二进制
print(oct(10))  # 八进制
print(hex(10))  # 十六进制

# 元组操作
tup = (1,)
print(type(tup))
li = list(tup)
print(type(li))
li.append('强制转换成功')
print(li)

# 字典操作
dic = dict(name='阿瓜', age=12)
print(dic)

# 字节操作
print(bytes('我喜欢Python', encoding='utf-8'))

"""
    内置函数-序列操作
    all()：判定用于给定可迭代参数中的所有项是否为True，除了0、空、False外都是True。但是空元组、空列表为True
    any()：判定用于给定可迭代参数中的所有项是否均为False，有一个为True就返回True
    sorted()：对可迭代对象进行排序操作。注意：sort是列表上的函数，而sorted是对所有可迭代对象。
    range(start = 0, stop, step = 1)：可创建一个整数列表，一般用于for循环。 为左闭右开区间
    zip()：将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回这些元组组成的列表,用于打包。
    enumerate(sequence, [start = 0])：将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标。一般用于for循环中 返回枚举对象
"""

print(all([1, 2, 3, [1]]))
print(all([1, 2, 3, [1], 0]))  # 因为多了一个0，因此变为False
print(all(''))
print(all([]))
print(all(()))  # 单个空列表、空元组、空字符串会视为True，但是作为元素时会被认为是False

print(any([1, 0, False]))

print(sorted([1, 2, 3, 4, 1, 6, 4, 9]))  # 默认为升序
print(sorted("1asd 3", reverse=True))  # 通过设置reverse改为降序
print(sorted((1, 4, 2, 5 ,9), reverse=True))  # sorted函数的返回值为一个列表
li = [1, 2, 3, 2, 3]
print(sorted(li))  # 可以看到排序已经生效，但不会对原来的对象造成改变，而是返回一个新的列表
print(li)


for i in range(5):  # 等价于range(0, 5, 1) 生成0，1，2，3，4
    print(i)
    pass

a = zip([1, 2, 3], ['a', 'b', 'c'], ['A', 'B', 'C'])  # 压缩,若各迭代器长度不一致则返回最短长度
print(list(a))  # 通过list转化为一个列表即可查看其内容


# 小样例练习
def printBookInfo():
    books = []  # 用于存储图书信息
    bookId = input('请输入图书编号，用空格分隔')
    bookName = input('请输入图书名称， 用空格分割')
    bookPos = input('请输入图书位置，用空格分割')

    IdList = bookId.split(' ')
    NameList = bookName.split(' ')
    PosList = bookPos.split(' ')

    bookInfo = zip(IdList, NameList, PosList)
    for bookItem in bookInfo:
        '''
        遍历图书信息
        '''
        dictInfo = {'编号':bookItem[0], '名称':bookItem[1], '位置':bookItem[2]}
        books.append(dictInfo)
        pass

    for item in books:
        print(item)
        pass

# printBookInfo()

listObj = ['a', 'b', 'c', 'd']
for index, item in enumerate(listObj):
    print(index, item)  # 从结果可以看出每个元素都加了一个索引

dictObj = {}
dictObj['name'] = '阿瓜'
dictObj['age'] = 12

for index, item in enumerate(dictObj):
    print(index, item)  # 从结果可以看出每个元素都加了一个索引


"""
    内置函数-set 集合
    set(集合)也是python中的一种数据类型，是一个无序且不重复的元素集合，不支持索引切片
    add()：添加
    clear()：清空
    difference()：差集
    intersection()：交集
    union()：并集
    pop()：从集合中随机删除某个元素并返回
    discard()：移除指定数据
    update()：更新操作
"""
# 创建一个集合
set1 = {'1', '2'}  # 方法一：直接创建
list1 = ['1', '2', '3', 4]
set2 = set(list1)  # 方法二：通过强制类型转换
print(type(set1))
print(len(set2))
print(set2)

set3 = {}  # 这样会默认为一个字典

# 添加、删除操作
set1.add((1, 2, 3))
set1.add('python')  # 经过检验，可增加元组、字符串 但不可以添加字典、列表
print(set1)
set1.clear()
print(set1)

# 集合操作
a = {32, 12, 34}
b = {12, 43, 23}
print(a.difference(b))
print(a-b)  # 两种都是取差集的方式

print(a.intersection(b))
print(a & b)  # 两种都是取交集的方式

print(a.union(b))
print(a | b)  # 两种都是取并集的方式

# 其他集合操作
c = a.pop()  # 类似于弹栈操作，但是是随机的
print(a)
print(c)

a.discard(12)
print(a)

a.update(b)  # 有点类似于并集操作
print(a)
