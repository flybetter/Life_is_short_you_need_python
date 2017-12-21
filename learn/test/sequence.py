#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= sequence
@author= wubingyu
@create_time= 2017/12/21 下午1:36
"""


def order(attr):
    if len(attr) <= 1:
        return attr
    point = attr[len(attr) / 2]
    before = [x for x in attr if x < point]
    middle = [x for x in attr if x == point]
    after = [x for x in attr if x > point]
    return order(before) + middle + order(after)


data = [1, 2, 3, 23, 3, 4, 5, 6, 7]

print order(data)

