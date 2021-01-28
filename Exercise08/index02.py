"""  python中的正则表达式  """

"""
    常用匹配规则-原生字符串：python用\作为转移字符开头 
    常用匹配规则=匹配开头、结尾：
    ^   匹配字符串开头
    $   匹配字符串结尾
"""
import re

print(re.match('c:\\\\a.txt', 'c:\\a.txt').group())  # \\代表一个\，即需要\\\\来匹配\\
print(re.match(r'c:\\a.txt', 'c:\\a.txt').group())  # 用r取消转义，保留原生含义

# ^匹配规则
print(re.match('^P.*','Python is language').group())  # 全部都匹配到了

# $匹配规则
print(re.match('[a-zA-Z0-9_]{6,15}@163.com','jiayang_zhao@163.com123').group())  # 没有$时，虽然不符合规范邮箱，但是匹配成功了
print(re.match('[a-zA-Z0-9_]{6,15}@163.com$','jiayang_zhao@163.com').group())  # 加了$对结果进行了限制，可以进行限制