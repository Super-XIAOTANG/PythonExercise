from distutils.core import setup
# name 模块名称
# version 版本号
# description  描述
# author 作者
# py_modules 要发布的内容

setup(name='myModule', version='1.0', description='myModule', author='崽崽', py_modules=['myModule'])

# 创建模块 python setup.py build
# 生成压缩包 python setup.py sdist
# 把dist文件夹下的压缩包发送即可
# 在另一台电脑，直接在终端pip install 压缩包 就可以使用了