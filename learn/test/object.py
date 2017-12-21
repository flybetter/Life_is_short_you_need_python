#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= object
@author= wubingyu
@create_time= 2017/12/21 下午11:25
"""


class A(object):

   @property
   def prop(self):
       return 3

a=A()
print '\'prop\' in a.__dict__=','prop'in a.__dict__
print 'hasattr(a,\'prop\')=',hasattr(a,'prop')
print 'a.prop',a.prop

#建议使用hasatt、getattr、setattr这种方式对于对象属性进行操作：


