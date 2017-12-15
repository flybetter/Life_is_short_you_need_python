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


