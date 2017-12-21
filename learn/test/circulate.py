#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= circulate
@author= wubingyu
@create_time= 2017/12/21 下午2:43
"""

words = ['words', 'are', 'you', 'me']

for x in words[:]:
    if len(x) == 5:
        words.insert(0, x)

print words

print words[:]
print words


