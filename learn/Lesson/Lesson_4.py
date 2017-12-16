#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= Lesson_4
@author= wubingyu
@create_time= 2017/12/16 下午3:49
"""
import sys
#6.模块
#出于性能考虑，每个模块在每个解释器回话中只导入一遍。因此，如果你修改了你的模块
#需要重启解释器或者如果你就是想交互式的测试这么一个模块，可以用reload()重新加载

# if __name__ == '__main__':
#     import sys
#     print int(sys.argv[1])



#6.1.2 模块的搜索路径
#导入一个叫spam的模块是，解释器先在当前目录中搜索名为spam.py的文件。如果没有找到的话，接着会到sys.path变量中给出的
#  目标列表中查找.

#6.1.3编译的python文件
#-O 会生成优化代码并保持在.pyo文件中。现在的优化器没有太多帮助
#-OO 会执行完全优化的二进制优化编译，这偶尔会生成错误的程序。


#6.2标准模块
print sys.path

#6.3 dir()函数
#内置函数dir()用于按模块名搜索模块定义，它返回一个排好序的字符串类型的存储列表
print dir(sys)

#6.4包
# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...

#6.4.1 从*导入包

#6.4.2 包内引用
#如果报中使用了子包结构，你可以用这样的形式from module import name来写显示的相对位置导入

#6.4.3 多重目录中的包
#包支持一个更为特殊的特性，_path_。在包的__init__.py文件代码执行之前，该变量初始化一个目录名列表。
#