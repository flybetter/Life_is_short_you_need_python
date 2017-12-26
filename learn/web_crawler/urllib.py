#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= urllib
@author= wubingyu
@create_time= 2017/12/23 上午8:51
"""
import urllib2

response = urllib2.urlopen("http://www.baidu.com")
print response.read()