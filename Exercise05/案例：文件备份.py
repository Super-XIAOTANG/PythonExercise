"""  文件备份  """

def copyFile():
    # 接受用户输入的文件名
    old_file = input("请输入要备份的文件名：")
    fileList = old_file.split('.')
    new_file = fileList[0]+'_备份.'+fileList[1]
    try:
        # 监视文件处理逻辑
        with open(old_file, 'r', encoding='utf-8') as old_f, open(new_file, 'w') as new_f:
            while True:
                content = old_f.read(1024)
                new_f.write(content)
                if len(content) < 1024:
                    break
        pass
    except Exception as msg:
        print(msg)
        pass
    pass


if __name__ == '__main__':
    copyFile()