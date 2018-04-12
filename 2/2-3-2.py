# coding=utf-8
# 如何统计序列中元素出现的频度

from collections import Counter

from random import randint

data = [randint(0, 20) for _ in xrange(30)]  # 创建0-20之间随机整数30个
print data

c2 = Counter(data)

print c2.most_common(3)  # 返回频度最高的三个
