# coding=utf-8
s = 'abc'

print s.ljust(20)
print s.rjust(20)
print s.center(20, '=')

print format(s, '<20')
print format(s, '>20')
print format(s, '^20')

d = {'adb': 12, 'ad': 93, 'da': 93, 'ffdss': 324, 'slll': 8934}

print 'Example'.center(25, '=')

w = max(map(len, d.keys()))  # 取出字典中的最大值

for k in d:
    print k.ljust(w), ':', d[k]
