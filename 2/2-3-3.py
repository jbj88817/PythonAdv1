# coding=utf-8
# 统计词频
import re
from collections import Counter

txt = open('django-coding-style.txt').read()
# print txt

c3 = Counter(re.split('\W+', txt))  # 用非字母做分割

print c3.most_common(10)