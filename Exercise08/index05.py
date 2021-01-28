"""  python中的正则表达式  """

"""
    贪婪模式与非贪婪模式：
    python的正则化匹配默认是贪婪的，总是尽可能多的匹配字符。非贪婪模式则相反
    在*、？、+、{m,n}后面加上？，使之变成非贪婪模式
"""

import re
data = 'a222222'
print(re.match('.*\d', data).group())  # 结果为a222222
# 转换为非贪婪模式
print(re.match('.*?\d', data).group())  # 结果为a2
