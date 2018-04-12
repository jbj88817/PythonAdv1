# coding=utf-8
# 如何统计序列中元素出现的频度

from random import randint

data = [randint(0, 20) for _ in xrange(30)]  # 创建0-20之间随机整数30个

c = dict.fromkeys(data, 0)  # 用每个整数为key生成一个dict, value初始值是0

for x in data:
    c[x] += 1

print c
