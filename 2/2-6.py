# coding=utf-8
# 如何让字典保持有序

d = {'Jim': (1, 35), 'Leo': (2, 37), 'Bob': (3, 40)}
print d  # 无序

from collections import OrderedDict

d2 = OrderedDict()  # 有序
d2['Jim'] = (1, 35)
d2['Leo'] = (2, 37)
d2['Bob'] = (3, 39)
print d2

for k in d2: print k
