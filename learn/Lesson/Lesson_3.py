#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= Lession3
@author= wubingyu
@create_time= 2017/12/15 下午4:37
"""
# 5 数据结构
# 5.1 关于列表更多的内容

myList = ["cat", "dog", "fish", "dog"]
print "you and me"
myList.append("me")
print myList

temp = ["temp", "object", "myself"]
myList.extend(temp)
print myList

myList.insert(0, "boss")
print myList

myList.remove("boss")
print myList

print myList.pop(4)
print myList

print myList.index("dog")

print myList.count("dog")

# cmp 自定升降序
# .sort(cmp,key,reverse)
myList.sort(key=lambda x: len(x), reverse=True)

print myList

myList.reverse()
print myList

# 5.1.1 把链表当作堆栈使用
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print stack.pop()
print stack.pop()
print stack

# 5.1.2 把链表当作队列使用
from collections import deque

queue = deque(["Eric", "john", "Michael"])
queue.append("Terry")
queue.append("Graham")
print queue.popleft()
print queue.popleft()
print queue


# 5.1.3 函数式编程工具
# filter（），map()以及reduce（）

def f(x): return x % 3 == 0 or x % 5 == 0


"""
如果该序列是一个str,unicode或者tuple,返回值必定是同一个类型，否则，它总是list。
"""
print filter(f, range(2, 25))

# map（function,sequence）为每一个元素一次调用function

print map(lambda x: x * x * x, range(1, 11))

print map(lambda x, y: x + y, range(8), range(8))

# reduce 返回一个单值，它是这样构造的：首先以序列的前两个元素调用函数function，再以返回值和第三个参数调用，依次执行下去。
# 可以传入第三个参数作为初始值
print reduce(lambda x, y: x + y, range(1, 11))
print reduce(lambda x, y: x + y, [], 0)

# 5.1.4 列表推导式
squares = []
for x in range(10):
    squares.append(x ** 2)
print squares

squares = [x ** 2 for x in range(10)]
# squares=map(lambda x:x**2,range(10))
print squares

# 列表推导式由一个表达式的括号组成，表达式后面跟随一个for子句，之后可以有零或多个for或if子句。结果是一个列表，由表达式
# 依据其后面的for和if子句上下文计算而来的结果构成
# 如下的列表推导式结合两个列表的元素，如果元素之间不相等的话
doubleSquare = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print doubleSquare

from math import pi

print [str(round(pi, i)) for i in range(0, 6)]

# 5.1.4.1 嵌套的列表推导式
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print [[row[i] for row in matrix] for i in range(4)]

# zip 主要是用元组
print list(zip(*matrix))
print zip(*matrix)

d = {"voltage": "four million", "state": "bleedin demised", "action": "VOOM"}


def parrot(voltage, state='a stiff', action='voom'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it.",
    print "E's", state, "!"


parrot(**d)

# 5.2 del语句
# 有个方法可以从列表中按给定的索引而不是值来删除一个子项：del语句
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print a

# 5.3元组和序列
# 我们知道连边和字符串有很多通用的属性，例如索引和切割操作。它们是序列类型(Sequence Types-str,unicode,list
# ,tuple,bytearray,buffer,xrange)中的两种。因为python是一个在不断进化的语言，也可能会加入其它的序列类型，这里介绍另外
# 另外一种标准序列类型：元组
t = 12345, 54321, "hello!"
print t[0]
u = t, (1, 2, 3, 4)
print u

# 元组是不可变的,列表是可变的
singleton = "hello",
print singleton

# 还可以逆向操作
t = 1234, 4321, "hello!"
print 1234 in t
x, y, z = t
print x, y, z

# 5.4 集合
# python 还包含了一个数据类型set，基本功能包括关系测试和校服重复元素.集合对象还支持union,intersection,difference
# sysmmetric difference等数学运算
basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
fruit = set(basket)
print fruit

print "orange" in fruit

# 这个很重要
a = set("abracadabra")
b = set("alacazam")
print a
print a - b
print a | b
print a & b
print a ^ b

# 5.5 字典
# 理解字典的最佳方式是把它看做无序的键：值对集合，键必须是互不相同的。一对大括号创建一个空的字典：。初始化链表时，
# 在大括号内放置一组逗号分隔的键：值对，这也是字典输出的方式。

tel = {"jack": 4098, "sape": 4139}
tel["guido"] = 4127
print tel["jack"]

del tel["sape"]

print tel

print tel.keys()

print "guido" in tel

print dict([("sape", "4139"), ("guido", "4127"), ("jack", "4098")])

# 5.6 循环技巧

for i, v in enumerate(["tic", "tac", "toe"]):
    print (i, v)

questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]

for q, a in zip(questions, answers):
    print "what is your {0}? It is {1}".format(q, a)

for i, v in enumerate(["tic", "tac", "toe"]):
    print i, v

for i in reversed(xrange(1, 10, 2)):
    print (i)

knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.iteritems():
    print k, v

# 5.7 深入条件控制
# while和if语句使用的条件不仅可以使用比较，而且可以包含任意的操作。
# 比较操作符in和not in 用来判断值是否在一个区间之内。
# 操作符is和is not比较两个对象是否相同；
# 这只和诸如链表这样的可变对象有关。
# 所有的比较操作具有先沟通呢的优先级，低于所有的数值操作。
# 比较操作可以传递。例如a<b==c判断a小于b并且b等于c
# 比较操作可以通过逻辑操作符and和or组合，比较的结果可以用not来取反义。
# 浙西操作符的优先级又低于比较操作符，在它们之中，not具有最高的优先级，or优先级最低，所以
# A and not b or 等于（A and （notB）or C ）。当然，括号也可以用于比较表达式。

# 逻辑操作符and和or也称作短路操作符：它们的参数从左向右解析，一旦结果可以确定就停止。
# 例如：如果A和C为真而B为加，AandBandC 不会解析C。
# 作用于一个普通的非逻辑值时，短路操作符的返回值通常是最后一个变量

# 5.8 比较序列和其它类型
#注意比较不同类型的对象也是合法的。比较的结果已经确定但是不一定合理：类型按其名称进行排序。因此，列表始终小鱼字符串，
#字符串总是小于元组，等等。
