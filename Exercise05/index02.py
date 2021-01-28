"""  python中的文件操作  """

"""
    文件定位：指文件指针的位置。
        1、tell() 要想知道文件指针当前位置，可以用tell()函数
        2、truncate() 可以对原文件进行截取操作
        3、seek(offset, from) 可以设置文件指针的位置 0表示开头，1表实当前位置，2表实文件结尾
        
"""
with open('Test.txt', 'r', encoding='utf-8') as f:
    print(f.read())
    # print(f.tell())
    pass

with open('Test.txt', 'r+', encoding='utf-8') as f2:
    f2.truncate(15)  # 保留前15个字符 utf-8每个汉字三个字符
    print(f2.read())

with open('Test_备份.txt', 'rb') as f3:
    data = f3.read(2)
    print(data.decode('gbk'))
    f3.seek(-2,1)  # 相当于光标又移动到了文件开始
    data = f3.read(4)
    print(data.decode('gbk'))
    # 若用r的模式打开文件，只允许在文件开头开始计算相对位置
    pass
