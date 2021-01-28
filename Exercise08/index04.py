"""  python中的正则表达式  """

"""
    Re中的编译模式：re.compile方法
    compile：将正则表达式模式编译成一个正则表达式对象，把一个字符串编译成字节码
    优点：1、在使用正则表达式进行 match操作时，python会将字符串转换成正则表达式对象，儿使用compile时，只需要转换一次即可，可以提高效率。
"""
import re
reobj = re.compile('\d{4}')

# 直接使用正则表达式对象进行match
rs = reobj.match('123456')
print(rs.group())  # 成功匹配1234

"""
    re.search(pattern, string, flags=0)方法：
    search:在全文中匹配一次，匹配到就返回
"""
data = 'I love China, China is a great country'
print(re.search('China', data).group())  # 成功匹配到China。
print(re.search('China', data))  # 区间为[7, 12)(左闭右开区间), 可以发现函数从左向右匹配，匹配的是左侧的China



"""
    re.findall(pattern, string, flags = 0) 匹配返回一个列表，返回所有复合条件的非重复结果
"""
data = '华为是华人的骄傲'
print(re.findall('华.', data))  # 返回结果为['华为','华人']


"""
    re.sub(pattern, repl, string, count=0, flags=0):将匹配到的数据进行替换
    count代表替换的最大次数，默认0就是替换所有匹配
    
    re.subn 完成目标的搜索和替换，返回被替换的数量
"""
data = 'hello world'
res = re.sub('h', 'H', data)
print(res)  # 结果为：Hello world
res = re.subn('h', 'H', data)
print(res)
print(data)  # 发现data本身并没有发生变化，而实新建了一个字符串对象返回给res


"""
    re.split(pattern, string, maxsplit=0, flags = 0)：实现字符串分割，并返回一个列表    
"""
data = '百度，腾讯，阿里，华为，360，小米，阿瓜'
res = re.split(',', data)
print(res)  # 根据分割结果返回一个列表
