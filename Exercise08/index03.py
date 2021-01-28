"""  python中的正则表达式  """

"""
    常用匹配规则-分组匹配
    |           匹配左右任意一个表达式
    (ab)        将括号中的字符作为一个分组
    \num        引用分组num匹配到的字符串
    (?P)        分组起别名
    (?P=name)   引用别名为name分组匹配到的字符串
"""
import re

# | 匹配规则
print(re.match('[1-9]?\d', '0').group())  # 匹配0-99
print(re.match('[1-9]?\d$|100', '100').group())  # 匹配0-100，加入$符限制10导致无法识别100

# (ab) 匹配规则 匹配电话号码xxxx-xxxxxxxx
print(re.match('([0-9]*)-(\d+)','0416-7878071').group(0))  # 指全部
print(re.match('([0-9]*)-(\d+)','0416-7878071').group(1))  # 指第一组即([1-9]*)
print(re.match('([0-9]*)-(\d+)','0416-7878071').group(2))  # 指第二组即(\d+)

# \num匹配规则
htmlTag = '<html><h1>测试数据</h1></html>'
print(re.match(r'<(.+)><(.+)>(.+)</\2></\1>', htmlTag).group())  # </\2> 指引用前面的第二组
print(re.match(r'<(.+)><(.+)>(.+)</\2></\1>', htmlTag).group(1))
print(re.match(r'<(.+)><(.+)>(.+)</\2></\1>', htmlTag).group(2))
print(re.match(r'<(.+)><(.+)>(.+)</\2></\1>', htmlTag).group(3))

# (?P)起别名 (?P=name)引用
# 样例：<?P<Name>>  引用<?P=引用的名字>
data = '<div><h1>www.baidu.com</h1></div>'
print(re.match(r'<(?P<DIV>\w*)><(?P<h1>\w*)>(.+)</(?P=h1)></(?P=DIV)>', data).group())
print(re.match(r'<(?P<DIV>\w*)><(?P<h1>\w*)>(.+)</(?P=h1)></(?P=DIV)>', data).group(1))
print(re.match(r'<(?P<DIV>\w*)><(?P<h1>\w*)>(.+)</(?P=h1)></(?P=DIV)>', data).group(2))
print(re.match(r'<(?P<DIV>\w*)><(?P<h1>\w*)>(.+)</(?P=h1)></(?P=DIV)>', data).group(3))  # 后面引用的部分，不算新的分组，即分组index只是1-3


