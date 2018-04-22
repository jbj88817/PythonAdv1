# coding=utf-8
# 拆分含有多种分隔符的字符串

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'


# Method 1
def mySplit(s, ds):
    res = [s]

    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t
    return [x for x in res if x]  # 过滤掉两个分隔符在一起的情况


print mySplit(s, ';,|\t')

# Method 2
import re

print re.split(r'[,;\t|]+', s)
