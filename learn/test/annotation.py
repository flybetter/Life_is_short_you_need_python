#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= annotation
@author= wubingyu
@create_time= 2017/12/21 下午3:45
"""


class Example(object):
    def __init__(self, value):
        self._val = value

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected int")
        self._val = value

    @val.deleter
    def val(self):
        del self.val

    @property
    def square3(self):
        return 2 ** 3


ex = Example(123)
print ex.val
print ex.square3


class example(object):
    @classmethod
    def clsmethod(self):
        print 'I am classmethod'

    @staticmethod
    def stmethod():
        print 'I am staticmethod'

    def instmethod(self):
        print 'I am instancemethod'


ex = example()
print ex.clsmethod()
print ex.stmethod()
print ex.instmethod()

print example.clsmethod()
print example.stmethod()
print example.instmethod()
