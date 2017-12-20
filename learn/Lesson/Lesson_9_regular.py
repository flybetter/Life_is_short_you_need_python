#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= Lesson_9_regular
@author= wubingyu
@create_time= 2017/12/19 下午4:25
"""
import re

# re.match 函数
# re.match尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
# re.match(pattern,string,flags=0)
# pattern 匹配的正则表达式
# String 要匹配的字符串
# flags 标示位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等

print re.match('www', 'www.runoob.com').span()
print re.match('com', 'www.runoob.com')
print re.match('www', 'www.runoob.com')
print re.match('www', 'www.runoob.com', re.I)

# 匹配成功re.match方法会返回一个匹配的对象，否则返回None
# 我们可以使用group(num)或者groups()匹配对象函数来获取匹配表达式

line = "Cats are smarter than dogs"

# 贪婪模式：默认情况下，正则表达式会匹配最大的符合条件的字符串, *、+和?限定符都是贪婪的，因为它们会尽可能多的匹配文字，只有在它们的后面加上一个?就可以实现非贪婪或最小匹配。
# 贪婪模式原因：(.*) (.+)
# 懒惰模式：正则表达式仅匹配最小的符合规则的字符串
matchObject = re.match(r'(.*) are (.*?) ', line, re.M | re.I)

if matchObject:
    print "matchObj.group():", matchObject.group()
    print "matchObj.group(1):", matchObject.group(1)
    print "matchObj.group(2):", matchObject.group(2)
else:
    print "No match!!"

# re.search方法
# re.search(pattern,string,flags=0)
# 匹配成功re.search方法返回一个匹配的对象，否则返回None
print re.search('www', 'www.runoob.com').span()
print re.search('com', 'www.runoob.com').span()

searchObject = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
if searchObject:
    print "searchObj.group():", searchObject.group()
    print "searchObj.group(1):", searchObject.group(1)
    print "searchObj.group(2):", searchObject.group(2)
else:
    print 'Nothing found!'

# re.match 与re.search的区别
# re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串
# 直到找到一个匹配

# re.sub
# re.sub(pattern,repl,string,count=0,flags)
# pattern 正则中的模式字符串
# repl 替换的字符串，也可为一个函数
# string 要被找替换的原始字符串
# count 模式匹配后替换的最大次数，默认0表示替换所有的匹配

phone = "2004-959-559 # 这就是一个国外的电话"
num = re.sub('#.*$', '', phone)

print '电话号码是：', num

num = re.sub(r'\D', '', phone)
print '电话号码是：', num


# repl参数是一个函数
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print re.sub('(?P<value>\d+)', double, s)
