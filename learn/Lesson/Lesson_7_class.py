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

for key in {'haha': 123, 'tony': 232}:
    print key


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse('spam')

for char in rev:
    print char

s = "test"
it = iter(s)
print next(it)
print next(it)
print next(it)

print "----------"

def reverse(data):
    for index in "spam":
        yield index


for char in reverse("spam"):
    print char