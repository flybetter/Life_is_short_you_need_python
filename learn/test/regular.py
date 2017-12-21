#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= regular
@author= wubingyu
@create_time= 2017/12/21 下午3:17
"""
import re

print re.match('^[a-zA-Z0-9-_]{3,16}$', 'Foo') is not None
print re.match('^\w[-_]{3,16}$','Foo') is not None
