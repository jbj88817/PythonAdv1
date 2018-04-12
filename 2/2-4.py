# coding=utf-8
from random import randint

d = {x: randint(60, 100) for x in 'xyzabc'}
print d
print list(iter(d))  # 字典的可迭代对象其实是key

# 元组比大小是一个值一个值比较
print (97, 'a') > (69, 'b')
print (97, 'a') > (97, 'b')

res = zip(d.itervalues(), d.iterkeys())
print res
print sorted(res)

# 第二种方法
print sorted(d.items(), key=lambda x: x[1])
