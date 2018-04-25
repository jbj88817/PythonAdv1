# coding=utf-8
f = open('py2.txt', 'w')

s = u'你好'
f.write(s.encode('gbk'))
f.close()

f = open('py2.txt', 'r')
t = f.read()
print t
print t.decode('gbk')

# Python3 看视频5-1