"""  Python中的文件操作  """

"""
    文件操作的一般步骤：
    1、打开文件
    2、读写文件
    3、保存文件
    4、关闭文件
"""

"""
    打开文件 open('文件名称','打开方式')
    打开方式：r 只读，这是默认模式
            w 只写，每次都会覆盖原文件
            a 用于追加内容
            rb/wb/ab 以二进制格式完成上述功能
            r+ 读写，文件指针会放在文件开头
            w+ 读写，若文件已存在则覆盖
            a+ 读写，文件指针放在文件结尾
            rb+/wb+/ab+ 以二进制格式完成上述功能
"""
# # 打开文件
# fobj = open('./Test.txt', 'w', encoding='UTF-8')
#
# # 开始读/写操作， 默认是GBK编码，最好修改为UTF-8
# # fobj.write('在苍茫的大海上')
# fobj.write('狂风卷积着乌云')
# fobj.close()  # 保存＋关闭
#
# # 以二进制格式读写
#
# fobj2 = open('./Test2.txt', 'wb')  # str-->bytes
# fobj2.write('在乌云和大海之间'.encode('utf-8'))
# fobj2.close()

# 读文件函数
fobj3 = open('./Test.txt', 'r', encoding='utf-8')
# print(fobj3.read())  # 读取全部
# print(fobj3.read(10))  # 读取10个字符 换行符也算一个
# print(fobj3.readline())  # 从文件指针当前位置读取一行
print(fobj3.readlines())  # 返回的是一个列表对象
fobj3.close()

# with 上下文管理，自动关闭文件句柄
with open('Text.txt', 'r') as f:
    f.readlines()
    # 在with语句下可以自动关闭
