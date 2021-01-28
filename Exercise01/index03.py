"""  字符串、列表、元组、字典相关操作  """

# 字符串的操作
"""
    序列：在python中，序列就是一组按顺序排列的值【数据集合】，包括字符串、列表、元组。
    特点：1）支持索引和切片的操作。第一个正索引为0，第一个负索引为-1。
         2）切片的语法为[起始下标:结束下标:步长（默认为1）]，且切片范围是左闭右开区间[起始位置，结束位置）        
         3）字符串类型不可更改
"""

# 字符串常用方法
str = "python"
print(type(str))
print(len(str))  # 打印字符串长度，汉字也算作一个字符
print(str.capitalize())  # 首字母变大写
print(str.isalnum())  # 判断是否为数字和字母
print(str.isalpha())  # 判断是否为字母
print(str.isdigit())  # 判断是否为数字
print(str.islower())  # 判断是否为小写
str.lower()  # lower/upper 大小写转换
print(str.swapcase())  # 大写变小写，小写变大写
print(str.endswith('n'))  # endswith/startswith 是否以X开始、结束
str.lstrip()  # lstrip/rstrip/strip 移除空白
str.split()  # 切割字符串
print(str.find('X'))  # 查找字符或字符串 若找到则返回第一个找到的下标,未找到则返回-1
print(str.index('p'))  # 功能与find类似，但查找失败时会报错

str2 = str
print(id(str))
print(id(str2))  # 发现str与str2的地址是一样的，可理解为对同一个地址的引用

# 切片测试
print(str[0])
print(str[0:1])  # 结果与上一行代码一致，可知结果为左闭右开区间
print(str[2:5])  # python
print(str[-1:-3:-1])  # -1代表反向截取，反向输出
print(str[-3:-1])
print(str[:3])
print(str[:-4:-1])
print(str[:])


# 列表常用方法：
"""
    列表：一种有序的数据集合，可以随时添加和删除其中的元素
    特点：1）支持增删改查
         2）列表的数据是可以变化的，但内存地址不会改变
         3）用[]来标识列表类型，数据项之间用逗号来分割,且数据类型不受限制
         4）同样可以使用切片的方法截取
"""
list = [1, 2, 3, 'o', "阿瓜", True]
print(type(list))
print(len(list))  # 打印列表的元素项数
print(list*3)  # 输出多次列表中的数据
print(list[::-1])

list.append(False)  # 追加的参数类型不受限制，也可以是一个列表
list.insert(1, "在1的位置插入")  # 插入操作，在任意位置插入数据
list2 = [7, 8, 9]  # 强制类型转换
list.extend(list2)  # 批量添加，参数为列表

list[0:2] = 6, '0'  # 灵活批量修改
print(list)

del list[0]  # 删除列表中的元素，可使用切片批量删除
list.remove(2)  # 移除指定值的元素
list.pop(1)  # 移除指定位置的元素
print(list)

print(list.index(7))  # 与字符串的index类似，同样的如果查找失败会报错

# 元组常用方法
"""
    元组: 与列表类似，但元组的数据不能修改
    特点：1）是一种不可变的序列，也可以通过切片的方式进行截取
         2）用（）创建元组类型，数据项用逗号分割，不限制类型
         3）当元组中只有一个元素时，也要加上逗号，不然解释器会当作整型来处理
         4）不能进行增加、删除、修改操作
"""

Tuple = (1, 2, 1, 3, 'o', "阿瓜", True, [1, 2, 3])
Tuple02 = (1,)  # 若不加逗号，会默认括号为多余，要设置成元组则需加一个逗号
print(type(Tuple))
print(type(Tuple02))
print(len(Tuple))

Tuple[7][0] = 100  # 注意，可以对其中的列表当中的元素进行修改
print(Tuple[:])
print(Tuple.count(12))  # 统计某指定值元素出现的次数

# 字典常用方法
"""
    字典：以键值对{'key':'value'}的方式存储数据
    特点：1）根据键值对的方式进行查找。不是序列，不能通过切片的方式了
         2）key值不能重复，但是value值可以重复
         3）key值必须是不可变类型，如数字、字符串、元组
         4）支持增、删、改、查操作
         5）用{}来声明字典对象，每个键值对用逗号分割
"""

Dict = {"这是谁":"亲爱滴"}
print(type(Dict))
print(len(Dict))  # 每一项代表一个键值对

Dict['name'] = '阿瓜'
Dict['age'] = 12
Dict['description'] = '憨憨'  # 直接向字典中追加内容
print(Dict)

Dict['name'] = '阿瓜阿瓜'  # 直接修改
Dict.update({'name':'阿瓜'})  # update函数可以进行添加、修改
print(Dict['name'])  # 根据key值打印value值
print(Dict.keys())  # 获取所有的键 返回一个元组
print(Dict.values())  # 获取所有的值 返回一个元组
print(Dict.items())  # 获取所有的键和值 返回一个元组
# 遍历字典的键值对
for key, value in Dict.items():
    print("%s == %s " % (key, value))

del Dict['name']  # 通过Del直接删除
Dict.pop('description')  # 通过pop指定key进行删除
print(Dict.get('name'))
print(Dict)

sorted(Dict.items(), key=lambda d:d[0])  # 按照key值进行排序


# 公用方法
strA = '人生苦短'
strB = '我选Python'
tupleA = (1,)
tupleB = (2,)
# 合并操作 +
print(strA + ", "+strB)  # 同样适用于列表、元组
print(tupleA + tupleB)

# 复制操作 *
print(strA * 3)  # 同样适用于列表、元组
print(tupleA * 3)

# 判断元素是否存在 in
print('生' in strA)  # 同样适用于列表、元组、字典（判断key）
print('name' in Dict)