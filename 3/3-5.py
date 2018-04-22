# coding=utf-8
# 对迭代器做切片操作


from itertools import islice

f = open('django-coding-style.txt')

# lists = f.readlines()
# print lists

# for line in islice(f, 100, 300):  # 100行-300行
#     print line

# for line in islice(f, 200):  # 前200行
#     print line

for line in islice(f, 100, None):  # 前100行到最后
    print line
