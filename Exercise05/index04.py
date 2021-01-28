"""  python-os模块  """

"""
    python-os:提供系统级别的操作命令
    
"""

import os

# os.rename('Test.txt', 'ReTest.txt')  # 修改文件名称
# os.rename('index01.py', 'index.py')

# os.remove('Test2.txt')  # 删除文件 前提文件必须存在

# os.mkdir('file')  # 创建文件夹 不可以级联创建
# os.mkdirs('Path') 可以创建多级目录
# os.rmdir('file')  # 删除文件夹 同样要求文件必须存在 不可以级联删除，不能删除非空文件夹， 可用shutil模块rmtree函数

print(os.getcwd())  # 打印当前目录
print(os.path)  # 打印模块位置

listRs = os.listdir('d:/')
print(listRs)
# scandir 和 with 一起使用，这样可以在迭代器遍历后自动释放
with os.scandir('d:/') as entries:
    for entry in entries:
        print(entry.name)
        pass




