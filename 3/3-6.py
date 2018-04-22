# coding=utf-8
# 同时迭代多个对象

from random import randint

chinese = [randint(60, 100) for _ in xrange(40)]
math = [randint(60, 100) for _ in xrange(40)]
english = [randint(60, 100) for _ in xrange(40)]

# 并行
total = []
for c, m, e in zip(chinese, math, english):
    total.append(c + m + e)

print total

from itertools import chain

e1 = [randint(60, 100) for _ in xrange(40)]
e2 = [randint(60, 100) for _ in xrange(42)]
e3 = [randint(60, 100) for _ in xrange(42)]
e4 = [randint(60, 100) for _ in xrange(39)]

count = 0
for s in chain(e1, e2, e3, e4):
    if s > 90:
        count += 1

print count
