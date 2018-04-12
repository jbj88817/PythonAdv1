# coding=utf-8
# 如何为元组中每个元素命名，提高程序可读性

from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])

s = Student('Jim', 16, 'male', 'jim@gmail.com')
print s

print s.name
print s.age
print s.sex

print isinstance(s, tuple)
