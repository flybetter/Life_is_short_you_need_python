#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= Lesson_6_exception
@author= wubingyu
@create_time= 2017/12/17 上午9:36
"""
# 8 错误和异常
# 8.1语法错误
# 8.2 异常
# 8.3 异常处理
# while True:
#     try:
#         x=int(raw_input("Please enter a number:"))
#         break
#     except ValueError:
#         print "Oops! That was no valid number.Try again"


# except(RuntimeError,TypeError,NameError)

import sys

try:
    f = open('/Users/wubingyu/Downloads/text.txt')
    s = f.readline()
    i = int(s)
except IOError as e:
    print "I/O error({0}):{1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

for arg in sys.argv[1:]:
    try:
        f = open("/Users/wubingyu/Downloads/text.txt")
    except IOError:
        print 'can\'t open ', arg
    else:
        print arg, 'has', len(f.read(100)), 'lines'
        f.close()

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print type(inst)
    print inst.args
    print inst
    x, y = inst.args
    print 'x=', x
    print 'y=', y

# 8.4 抛出异常
# raise语句允许程序员强制抛出指定异常

raise NameError('HiThere')


# 8.5用户自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as e:
    print 'My exception occurred,value:', e.value


# 异常类中可以定义任何其它类中可以定义的东西，但是通常为了保持简单，只在其中加入
# 几个属性信息，以供异常处理句柄提取。如果一个新创建的模块中需要抛出几种不同的
# 错误是，一个通常的作法是为该模块定义一个异常基类，然后针对不同的错误类型
# 派生对应的异常子类：

class Error(Exception):
    """Base class for exceptions in this module"""
    pass


class InputError(Error):
    """Raised when an operation attemps a state transition that's not allowed

    Attributes:
        prev -- state at beginning of transition
        next -- attempted new state
        msg -- explanation of why the specific transition
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg


class TransitionError(Error):
    """
    Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        prev -- state at beginning of transition
        next -- attempted new state
        msg  -- explanation of why the specific transition is not allowed

    """

    def __init__(self, prev, next, msg):
        self.prev = prev
        self.next = next
        self.msg = msg


# 与标准异常相似，大多数异常的名称都以"Error"结尾

# 8.6 定义清理行为
try:
    raise KeyboardInterrupt
finally:
    print 'Goodbye,world!'

# 8.7预定义清理行为
# 有些对象定义了标准的清理行为，无论对象操作是否成功，不再需要该对象的时候
# 就会起作用。一下示例尝试打开文件并把内容打印到屏幕上：
for line in open('text.txt'):
    print line

#但是大型应用程序就会出问题。with语句使得文件之类的对象可以确保总能及时准确地进行
#清理

with open("text.txt") as f:
    for line in f:
        print line


