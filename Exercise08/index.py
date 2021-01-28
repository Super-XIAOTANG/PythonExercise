"""  python中的正则表达式  """

"""
    正则表达式：高效率处理字符串、爬虫等。用于检索符合某个模式的文本
    python中的正则表达式通过 re 模块实现正则表达式
"""

import re

"""
    re.match(pattern, str, flags = 0) 从字符串起始位置匹配一个规则，成功就返回match对象，否则返回None，可使用group()获取匹配成功的字符串（多匹配结果则返回元组）,flag控制是否区分大小写、多行匹配等。
        flag规则：re.I 对大小写不敏感
                 re.L 做本地化识别匹配
                 re.M 多行匹配，影响^和$
                 re.S 使.匹配包括换行在内的所有字符
                 re.U 根据Unicode字符集解析字符，影响\w, \W, \b, \B
                 re.X 提供更灵活的格式将正则表达式写的更易于理解
"""

data = "Python is the best language in the world!"
res = re.match('python', data, re.I|re.M)  # 精确匹配， 只匹配以P开头
if res:
    print(type(res))
    print(res)  # 匹配成功，返回一个P,说明数据是以P开头
    print(res.group())
else:
    print('匹配失败...')

res = re.match('(.*) is (.*?).*', data)
print(res.groups())


"""
    正则表达式匹配规则：
    .      匹配任意一个字符，出了换行符\n
    [abc]  匹配abc中的任意一个字符
    \d     匹配任意一个数字，即0-9
    \D     匹配非数字
    \s     匹配空白，即空格，tab键
    \S     匹配非空白
    \w     匹配单词字符，即a-z，A-Z，0-9，_
    \W     匹配非单词字符
"""

# .的匹配
data = 'aaaa'
pattern = '.'
res = re.match(pattern, data)
print(res.group())  # 匹配到一个a

names = '李达', '李明', '小王', '小李', '阿瓜'
for name in names:
    pattern = '李.'
    res = re.match(pattern, name)
    if res:
        print(res.group())  # 匹配到李达，李明

# [abc]的匹配
data = 'hello'
res = re.match('[he]', data)  # 匹配[he]中的任意一个字符
print(res.group())
# 更值观的例子：
datas = 'a', 'b', 'c','d','add'
for data in datas:
    res = re.match('[abc]', data)
    if res:
        print('匹配成功： ' + res.group())

# \d \D的匹配
data = '123456abcde'
print(re.match('\d', data).group())  # 匹配到1，一个\d只匹配一个数字
print(re.match('\D', 'a'+data).group())  # 匹配到a

# \s \S的匹配
data = '    hello'
print(re.match('\s\s\s\s.', data).group())  # 一个\s匹配一个空格，也就是说tab需要四个\s才匹配结束

# \w \W的匹配
data = '$#abc'
# print(re.match('\w', data).group())  # 匹配失败
print(re.match('\w', 'a'+data).group())  # 匹配成功
print(re.match('\W', data).group())  # 匹配成功$


"""
    匹配字符串数量：
    *       匹配前一个字符出现0次或无限次，即可有可无  
    +       匹配前一个字符出现1次或者无限次，即至少有一次
    ?       匹配前一个字符出现1次或0次，即要么1次，要么没有
    {m}     匹配前一个字符出现m次
    {m,}    匹配前一个字符至少出现m次
    {n,m}   皮皮额前一个字符出现n到m次
"""

# * 匹配规则
print(re.match('[A-Z][A-Z]*', 'My').group())  # 匹配到一个M
print(re.match('[A-Z][a-z]*', 'Any').group())  # 匹配到Any，即*可以匹配0到无限次

# + 匹配规则
# print(re.match('[A-Z][a-z]+', 'ANy').group())  # 匹配失败，即+要求[a-z]必须出现一次
print(re.match('[A-Z]+', 'MYNAMEasdas').group())  # 匹配到MYNAME

# 练习：匹配符合命名规范的变量名
print(re.match('[a-zA-Z_]+[\w]*', '_name').group())  # 匹配成功

# ? 匹配规则
print(re.match('[a-zA-Z]+[0-9]?', 'AA999').group())

# {min,max}的使用,告诉引擎至少出现min次，最多max次，两参数都必须是非负整数
result = re.match('\d{4}', '1234')
if result:
    print(result.group())  # {4}代表精确匹配4位，匹配到1234
    pass

# 练习：匹配163邮箱  格式xxxxxx@163.com
regexMail = re.match('[a-zA-Z0-9_]{6,15}@163.com', 'jiayang_zhao@163.com')
print(regexMail.group())  # 匹配成功


