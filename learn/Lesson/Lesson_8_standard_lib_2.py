#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= Lesson_8_standard_lib_2
@author= wubingyu
@create_time= 2017/12/19 上午9:53
"""
# 11. 标准库浏览
# 11.1输出格式
# repr模块为大型的或深度嵌套的容器缩写显示提供了repr()函数的一个定制版本
import repr

print repr.repr(set('supercalifragilisticexpialidocious'))
print set('supercalifragilisticexpialidocious')

# 美化打印pretty printer
import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
                                                        'yellow'], 'blue']]]

print pprint.pprint(t, width=30)

# textwrap模块格式化文本段落以适应设定的屏宽
import textwrap

doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""

print textwrap.fill(doc, width=40)

# locale模块按访问预定好的国家信息数据库。locale的格式化函数属性集提供了一个直接方式以分组标示
# 格式化数字
# import locale
#
# locale.setlocale(locale.LC_ALL, 'English_United States.1252')

# 11.2模块
from string import Template

t = Template('${village} folk send $$10 to $cause.')
print t.substitute(village='Nottingham', cause='the ditch fund')

# 模块子类可以指定一个自定义分隔符。例如，图像查看器的批量重命名工具可能选择使用百分号作为占位符
# 像当前日期，图片序列号或文件格式
# >>> import time, os.path
# >>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
# >>> class BatchRename(Template):
# ...     delimiter = '%'
# >>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
# Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f
#
# >>> t = BatchRename(fmt)
# >>> date = time.strftime('%d%b%y')
# >>> for i, filename in enumerate(photofiles):
# ...     base, ext = os.path.splitext(filename)
# ...     newname = t.substitute(d=date, n=i, f=ext)
# ...     print('{0} --> {1}'.format(filename, newname))
#
# img_1074.jpg --> Ashley_0.jpg
# img_1076.jpg --> Ashley_1.jpg
# img_1077.jpg --> Ashley_2.jpg

# 11.3使用二进制数据记录布局

# 11.4多线程
import threading, zipfile, os


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print 'Finished background zip of:', self.infile


os.chdir("/Users/wubingyu/Downloads")
background = AsyncZip('text.txt', 'text.zip')
background.start()
print 'The main program continues to run in foreground'

background.join()
print 'Main program waited until background was done'

# 因此，任务协调的首选方法是把一个资源的所有访问几种在一个单独的线程中，然后使用Queue模块用哪个线程服务
# 其他线程的请求。

# 11.5日志
import logging

logging.debug('Debugging information')
logging.info('Information message')
logging.warning("Warning:config file %s not found", 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

# 11.6 弱引用
import weakref, gc

d = weakref.WeakKeyDictionary

# 11.7列表工具
from array import array

a = array('H', [400, 10, 700, 2222, 3330, 444])
print sum(a)
print a[1:3]
# python中的list是python的内置数据类型，list中的数据类不必相同的，而array的中的类型必须全部相同。

# collections模块提供了类似列表的deque()对象，它从左边添加和弹出更快，但是在内部查询更慢。
from collections import deque

d = deque(["task1", "task2", "task3", "task4"])
d.append('task5')
print 'handling', d.popleft()
print 'handling', d.popleft()

import bisect

score = [(100, 'perl'), (200, 'tcl'), (400, 'pthon')]
bisect.insort(score, (300, 'java'))

print score

# heapq提供了基于正规链表的堆实现。最小的值总是保持在0点。这在希望循环访问最小元素但是不想执行完整堆排序的时候非常有用

from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
print data
heappush(data, -5)
print data

# 11.8 十进制浮点数算法
from decimal import *
print round(Decimal('0.70') * Decimal('1.05'), 2)
print round(0.70*1.05,2)