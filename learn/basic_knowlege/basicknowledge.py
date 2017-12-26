#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= basicknowledge
@author= wubingyu
@create_time= 2017/12/26 上午9:38
"""
import re
import os
import glob

fileList = []
rootdir = os.path
print os.path

for file in os.walk(rootdir):
    fileList.append(file)

print fileList
