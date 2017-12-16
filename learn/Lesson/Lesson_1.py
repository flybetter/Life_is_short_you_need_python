#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= Lession_1
@author= wubingyu
@create_time= 2017/12/15 上午10:36
"""

print 2 + 2
print 50 - 5 * 6
print (50 - 5.0 * 6) / 4
print 8 / 5.0

print 17 / 3
print 17 / 3.0
print 17 // 3.0  # 这个还是蛮重要的
print 17 % 3

print 5 ** 2
print 2 ** 7

width = 20
height = 5 * 9
print width * height

# 字符串
print 'spam eggs'
print 'doesn\'t'
print "doesn't"
print '"yes",he said'
print "\"yes\",he said"
print '"Isn\'t",she said '

print 'C:\some\name'
print r'C:\some\name'

print """\
    Usage:thiny [OPITIONS]
        -h
        -H hostname
"""

print 3 * "uni" + "unm"
print 'PY''thon'

text = ('Put serveral strings with parentheses'
        'to have them join together')
print text

word = "Python"
print word[1]
print word[2]
print word[-1]
print word[-2]
print word[0:2]
print word[-4:-1]
print word[2:]
print word[:-2]

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

print  len(word)

print u"Hello world"

# 如果你需要大量输入反斜杠，原始模式非常有用，这在正则表达式中几乎是必须的。

# 关于Unicode

print ur'Hello\u0020World !'
print ur'Hello\\u0020World !'
print u"哈哈".encode('utf-8')

# 列表
squares = [1, 4, 9, 16, 25]
print squares

squares[3] = 22
squares.append(216)  # 这个还是蛮重要的
squares.append(7 ** 3)
print squares
print len(squares)

a, b = 0, 1
while b < 10:
    print b
    a, b = b, a + b
