#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Life_is_short_you_need_python
@file= Lesson_7_class
@author= wubingyu
@create_time= 2017/12/17 上午10:49
"""


class Employee:
    pass


john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000


print john.salary

for key,value in {'haha':123,'tony':232}:
    print key,value