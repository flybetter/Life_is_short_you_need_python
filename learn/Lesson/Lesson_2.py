#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= Lession_2
@author= wubingyu
@create_time= 2017/12/15 下午2:06
"""
# 4 深入python流程控制

# 4.1 if语句
x = 0
if x < 10:
    print "case 1"
elif x == 0:
    print "case 2"
elif x > 0:
    print "case 3"
else:
    print "error"

# 4.2 for语句
words = ["cat", "window", "dog", "differences"]
for w in words:
    print w, len(w)

# 4.3 rang()函数
print range(10)

# 4.4 break和continue 语句，以及循环中的else子句
# 循环可以有一个 else 子句；它在循环迭代完整个列表 (对于 for) 后或执行条件为 false (对于 while) 时执行，
# 但循环被 break 中止的情况下不会执行。以下搜索素数的示例程序演示了这个子句:
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, "equals", x, "*", n / x
            break
    else:
        print n, x, "is a prime number"

# else语句是属于for循环之中，不是if语句

for num in range(2, 10):
    if num % 2 == 0:
        print "Found an even number", num
        continue
    print "Found a number", num


# 4.5 pass语句
def initlog(*args):
    pass


# 4.6定义函数
def fib(n):
    """ Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a
        a, b = b, a + b


fib(10)
print fib(10)


def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


f100 = fib2(100)
print f100


# 4.7 深入python函数定义
# 例子 1 可以看到：这两个函数均能接收 字符串 ，但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。
# 而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，
# 否则它会引发一个 SyntaxError 。

# 例子 2 可以看到：raw_input() 将所有输入作为字符串看待，返回字符串类型。而 input() 在对待纯数字输入时具有自己的特性，
# 它返回所输入的数字的类型（ int, float ）；同时在例子 1 知道，input() 可接受合法的 python 表达式，
# 举例：input( 1 + 3 ) 会返回 int 型的 4 。
# 4.7.1 默认参数值
def ask_ok(prompt, retries=4, complaint='Yes or no ,please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ("y", "ye", "yes"):
            return True
        if ok in ("n", "no", "nop", "nope"):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError("refusenik user")
        print complaint


# ask_ok("Do you really want to quit?")

# ask_ok("Ok to overwrite the file?", 2)

# ask_ok("Ok to overwrite the file?", 2, "come on, only yes or no!")


# 重要警告 默认值只被赋值一次。这使得当默认值是可变对象时会有所不同，比如列表、字典、或者大多数类的实例。
def f(a, L=[]):
    L.append(a)
    return L


print f(1)
print f(2)
print f(3)


def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print f2(1)
print f2(2)
print f2(3)


# 4.7.2关键字参数
def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
    """
    :param voltage:
    :param state:
    :param action:
    :param type:
    :return:
    """
    print "-- This parrot would't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage,the", type
    print "-- It's", state, "!"


parrot(1000)


# 任何参数都不可以多次赋值

# 4.7.3 可变参数列表
# 一个最不常用的选择是可以让函数调用可变个数的参数
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# 4.7.4 参数列表的分拆
# 另外一中相反的情况：当你要传递的参数已经是一个列表，但要调用的函数却接受分开一个个的参数值，
# 这时候你要把已有的列表拆开来。
# 例如内建函数range()需要独立的start，stop参数。你可以在调用函数时加一个*操作来自动把参数拆开
args = [3, 8]
print list(range(*args))


# 4.7.4 Lambda形式
# 通过lamdba关键字，可以创建短小的匿名函数。这里有一个函数返回它的两个参数的

# g=lambda x:x+1
# def g(x):
#   return x+1
#
def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print f(0)
print f(1)

pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair: pair[1])
print pairs


# 4.7.6 文档字符串
def my_function():
    """Do nothing,but document it
    No really,it doesn't do anything.
    :return:
    """
    pass


print my_function.__doc__

# 4.8 插曲 编码风格
# 1.使用4空格
# 2折行确保不会超过79字符
# 3 使用空行分割函数和类，以及函数中的大块代码
# 可能的话，注释独占一行
# 使用文档字符串
# 把空格放到操作符两边，以及逗号后面，但是括号里侧不加空
# 同意函数和类命名:
# 小驼峰法
# 变量一般用小驼峰法标识。驼峰法的意思是：除第一个单词之外，其他单词首字母大写。譬如
# int myStudentCount;
# 变量myStudentCount第一个单词是全部小写，后面的单词首字母大写。
# 大驼峰法
# 相比小驼峰法，大驼峰法（即帕斯卡命名法）把第一个单词的首字母也大写了。常用于类名，命名空间等。譬如
# public class DataBaseUser;

#方法和对象相关；

#函数和对象无关。
#方法和对象相关；

# 函数和方法名用小写_和_下划线。总是用self作为方法的第一个参数
