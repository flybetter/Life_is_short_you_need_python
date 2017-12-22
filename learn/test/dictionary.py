#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= dictionary
@author= wubingyu
@create_time= 2017/12/22 上午11:55
"""

def merge_dicts(*kwargs):
    """
    Given any number of dicts
    """
    result={}
    for dictionary in kwargs:
        result.update(dictionary)
    return result

print merge_dicts({1:"232"},{2:"2323"})