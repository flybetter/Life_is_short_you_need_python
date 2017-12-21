#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= direction
@author= wubingyu
@create_time= 2017/12/21 下午11:36
"""
from os import listdir
from os.path import isfile, join

mypath = r"/Users/wubingyu/Downloads"
onlyfiles = [f for f in listdir(mypath)]
print onlyfiles


from os import walk
f=[]
for (dirpath,dirnames,filenames)in walk(mypath):
    f.extend(filenames)
    break
print f