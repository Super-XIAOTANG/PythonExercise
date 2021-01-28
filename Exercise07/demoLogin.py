import argparse

# 创建一个解析器对象
parse = argparse.ArgumentParser(prog='系统登录', usage='%(prog)s [options] usage',
                                description='系统自定义命令行的文件', epilog='my epilog')
"""
    prog 文件名，默认为sys.argv[0]，用于在help信息中描述程序的名称
    usage：描述程序用途的字符串
    description：help信息前显示的信息
    epilog：Help信息之后显示的信息
"""


# 添加参数选项 add_argument() 参数为可选参数和位置参数（必须上传）
parse.add_argument('loginType', type=str, help='登录用户类型')

parse.add_argument('-u', dest='user', type=str, help='您的用户名')  # 可选参数， append可以设置参数由多个值
parse.add_argument('-p', dest='pwd', type=str, help='您的密码')  # 设置默认值，和参数可选范围


# 定义处理逻辑

result = parse.parse_args()  # 开始解析参数
if result.user == 'root' and result.pwd == '111111':
    print('Successfully login!')
    pass
else:
    print('Failed!')
    pass
