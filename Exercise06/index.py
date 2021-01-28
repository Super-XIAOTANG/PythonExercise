"""  模块测试文件  """
# import myModule  # 导入自定义模块
from myModule.myModule import *

# print(myModule.add(0, 0))
# myModule.printInfo()  # 在使用import 模块名 时正常
print(add(4, 6))
print(diff(5, 7))
# printInfo()  # 调用失败,由于__all__的原因
