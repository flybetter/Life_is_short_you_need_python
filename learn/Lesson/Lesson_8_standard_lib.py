#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= Lession_8_standard_lib
@author= wubingyu
@create_time= 2017/12/18 下午2:47
"""
# 10python标准库

# 10.1操作系统接口
import os

print os.getcwd()
# os.chdir("/Users/wubingyu/PycharmProjects/Life_is_short_you_need_python/")
os.system("date")

# 针对日常的文件和目录管理任务，shutil模块提供了一个易于使用的高级接口
# import shutil
#
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')

# 10.2 文件通配符
import glob

print "%s/*.py" % os.getcwd()
print glob.glob("%s/*.py" % os.getcwd())

# 10.3命令行参数
import sys

# 显示环境变量
# 这些命名行参数以连败你形式存储于sys模块的argv变量。
print sys.argv

# 10.4 错误输出重定向和程序终止
# sys还有stdin、stdout和stderr属性，即使在stdout被重定向时，后者也可以用于显示警告和错误信息
sys.stderr.write('Warning,log file not found starting a new one\n')

# 10.5 字符串正则匹配 (不是很懂)
# re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:
import re

print re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the the hat')

# 只需简单的操作是，字符串方法最好用，因为它们易读，又容易调试
print 'tea for too'.replace('too', 'two')

# 10.6 数学
# match 模块为浮点运算提供了对底层
import math

print math.cos(math.pi / 4.0)
print math.log(1024, 2)

import random

print random.choice(['apple', 'pear', 'banan'])
print random.sample(xrange(10), 10)
print random.random
print random.randrange(6)

# 10.7 互联网访问
# 有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理urls接收的数据的urllib2
# 以及发送电子邮件的smtplib
import urllib2

# for line in urllib2.urlopen("http://tycho.usno.navy.mil/cgi-bin/timer.pl"):
#     line = line.decode('utf-8')
#     if 'EST'in line or 'EDT' in line:
#         print line,"aaa"

# 10.8 日期和时间
# datetime 模块为日期和时间处理同时提供了简单和复杂的方法。支持日期和时间算法的同时，实现的重点放在更
# 有效的处理和格式化输出
from datetime import date

now = date.today()
print now

# 10.9 数据压缩
# zlib、gzip、bz2、zipfile以及tarfile

# 10.10 性能度量
# 有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣
# 例如：使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多
from timeit import Timer

print Timer('t=a;a=b;b=t', 'a=1;b=2').timeit()
print Timer('a,b=b,a', 'a=1;b=2').timeit()


# 10.11 质量控制
# 开发高质量的软件的方法之一是为了每个函数开发测试代码
# doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试
# 测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。通过用户提供的例子
# 它发展了文档，允许doctest模块确认代码的结果是否与文档一致

def average(values):
    """
    Computes the arithmetic mean of a list of numbers

    >>> print average([20,30,79])
    40.0
    :param values:[20,30,79]
    :return: 43
    """
    return sum(values, 0.0) / len(values)


print "----------"
def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'bbb'
    """
    return a * b


import doctest

doctest.testmod()
