#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= decorador
@author= wubingyu
@create_time= 2017/12/21 下午11:50
"""
from functools import wraps


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print func.__name__ + " was called"
        return func(*args, **kwargs)
    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


##等价于
# def f(x):
#     """does some math"""
#     return x + x * x
#
#
# f = logged(f)

print f.__name__
print f.__doc__

print f(2)
