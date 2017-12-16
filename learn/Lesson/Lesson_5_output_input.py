#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= Lesson_5_output_input
@author= wubingyu
@create_time= 2017/12/16 下午4:23
"""
import math

# 7输入和输出
# 7.1格式化输出
# 函数str（）用于将值转化为适于人阅读的形式，而repr()转化为供解析器读取的形式
for x in range(1, 11):
    print "{0:2d}{1:2d}{2:2d}".format(x, x ** 2, x ** 3)

print "We are the {} who say \"{}\"!".format("knights", "Ni")

# '!s'(应用str())和'!r'(应用repr())可以在格式化之前转换值：
# 字段名后允许可选的'：'和格式指令。这允许对值得格式化加以更深入的控制。


print ('The value of PI is approximately {0:.3f}'.format(math.pi))
# python 3已经不是这样的样式了

table = {'Sjoerd': '4127', 'jack': '4098', 'Dcab': '8637678'}
print 'jack:{jack};Sjoerd:{Sjoerd}'.format(**table)

# 7.2文件读写
# 函数open()返回文件对象，通常的用法需要两个参数：open(file,mode)。
# f = open("/Users/wubingyu/Downloads/test.txt", "w")
# print f

# 7.2.1 文件对象方法
# 要读取文件内容，需要调用f.read(size),该方法读取若干数量的数据并以字符串形式返回，
# size是可选的数值.

f = open("/Users/wubingyu/Downloads/text.txt", "r")
print "new input", f.read(100)
f.close()

with open("/Users/wubingyu/Downloads/text.txt") as file:
    for k,v in enumerate(file):
        print k,v

f=open("/Users/wubingyu/Downloads/text.txt","w+")
print f.read(100)
# f.write("\nstupid")
# w w+
# r r+
# a a+ 追加
f.close()

#7.2.2 使用json存储结构化数据
#标准模块json可以接受python数据结构，并将它们转换为字符串表示形式；此过程称为序列化。从字符串表示形式重新
#构建数据结构称为反序列化。
import json
print json.dumps([1,'simple','list'])
# json.dump(x,f)
# x=json.load(f)


