#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= demo
@author= wubingyu
@create_time= 2017/12/22 下午1:49
"""
# ca*t将匹配ct、cat、caaat等等
import re
import os

print re.match('a[bdc]*b', 'abcbweqweqd').group()
print re.findall('a[bdc]*b', 'abcbd')

print re.match('home-?work', 'homework').group()

# match 从一开始就匹配
# search 不必要从一开始就匹配
# findall 查找所有返回一个列表
# finditer 返回一个迭代器

p = re.compile('...')
match = p.match('...')
if match:
    print "Match found:", match.group()
else:
    print "None"

# 组是通过"("和")"元字符来标识的。"（"和"）"有很多在数学表达式中相同的意思;它们一起把在它们里面的
# 表达式组成一组。
p = re.compile('(a(b)c)d')
m = p.match('abcd')
print m.groups()
print m.group(0)


def check_result(m):
    if m:
        print "the result:", m
    else:
        print "None"


# 模式中的逆向引用允许你指定先前捕获组的内容，该组也必须在字符串当前的位置被找到。
# 举个例子，如果组1的内容能够在当前位置找到的话，\1就成功否则失败。
# 记住Python字符串也是用反斜杠加数据允许字符串中包含任意字符的。

# 直接这样  但是如果还有别的正则表达式的话 要注意括号的编号 ([a-zA-Z])(\1){2,}
p = re.compile(r'((\b\w+)\s+)\1')  # \1 指的是组  这个组就是group(1) 也就是说出现之前的参数，为什么不是Pair,因为他不符合定义的正则失败了
m = p.search('Pairs in the the the spring').group()
print "1的详细用法",m

p = re.compile(r'(\b\w+)\s+')
m = p.findall('Pairs in the the the spring')
check_result(m)

# （？P<name>...）定义一个命名组，(?P=name)则是对命名组的逆向引用
p = re.compile(r'(?P<word>\b\w+\b)')
m = p.search('((( Lots of punctuation)))')
print "*****",m.group(1)
print m.groups()

# 因为逆向引用的语法，像（...）\1这样的表达式所表示的是组好，这时用组名代替组好自然会有差别。还有一个python扩展
# (?P=name).

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print p.search('Pairs in the the the spring').group()

# 前向界定符
# (?=...)
# 前向肯定界定符。如果所含正则表达式，以...表示，在当前位置成功匹配时成功，否则失败。但一旦所含
# 表达式已经尝试，匹配引擎没有提高；模式的剩余部分还要尝试界定符的右边

# (?!...)
# 前向否定界定符。与肯定界定符相反；当所含表达式不能再字符串当前位置匹配时成功

# print re.match(r'.*[.](?!bat$|exe$).*$', os.path)


# split() 将字符串在RE匹配的地方分片并生成一个列表
# sub() 找到RE匹配的所有子串，并将其用一个不同的字符串替换
# subn() 与sub()相同，返回新的字符串和替换次数

p = re.compile(r'\W+')
print p.split('This is a test,short and sweet, of split().', 3)

# 搜索和替换
# sub(replacement,String[,count=0])
p = re.compile('(blue|white|red)')
print p.sub('color', 'blue socks and red shoes')

# subn 返回的是包含新字符和替换执行次数的两元组
print p.subn('color', 'blue socks and red shoes')

p = re.compile('x*')
print p.sub('-', 'abxd')

p = re.compile('section{([^}]*)}', re.VERBOSE)
print p.search('section{First} section{second}').groups()
print p.sub(r'subsection{\1}', 'section{First} section{second}')
print p.sub(r'subsection{\g<1>}', 'section{First} section{second}')



p = re.compile('section{(.*?)}', re.VERBOSE)
print p.search('section{First} section{second}').groups()
print p.sub(r'subsection{\1}', 'section{First} section{second}')
print p.sub(r'subsection{\g<1>}', 'section{First} section{second}')


