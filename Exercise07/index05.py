"""  python中的命令行参数"""

"""
    python可以使用sys模块中的sys.argv来获取命令行参数,在脚本开发的时候可以更加方便的交互
    命令行参数-argparse模块，可以轻松编写用户友好的命令行界面
    参数说明：parents：由ArgumentParse对象组成的列表，他们的arguments选项会被包含到新的ArgumentPaeser对象中
            formatter_class：help信息输出的格式，为了美观
            prefix_chars:参数前缀，默认为-
            fromfileprefixchars：前缀字符，放在文件名之前
            add_help:增加-h/-help选项,默认为True
            argument_default:设置一个全局的选项的缺省值，一般每个选项单独设置，基本没用。
    
"""

# import sys
# print('参数个数为', len(sys.argv), '个参数')
# print('参数个数列表', str(sys.argv[1:]))
# 需要在terminal中，用命令行启动

import argparse

# 创建一个解析器对象
parse = argparse.ArgumentParser(prog='my program', usage='%(prog)s [options] usage',
                                description='my description', epilog='my epilog')
"""
    prog 文件名，默认为sys.argv[0]，用于在help信息中描述程序的名称
    usage：描述程序用途的字符串
    description：help信息前显示的信息
    epilog：Help信息之后显示的信息
"""


# 添加参数选项 add_argument() 参数为可选参数和位置参数（必须上传）
parse.add_argument('name', type=str, help='我自己的名字')
parse.add_argument('age', type=str, help='我的年龄')

# parse.add_argument('-s', '--sex', action='append', type=str)  # 可选参数， append可以设置参数由多个值
parse.add_argument('-s', '-sex', default='男', choices=['男', '女'], type=str, help='我的性别')  # 设置默认值，和参数可选范围


result = parse.parse_args()  # 开始解析参数
print(result.name, result.age)



# print(parse.print_help())






