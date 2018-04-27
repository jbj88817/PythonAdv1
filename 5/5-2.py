# coding=utf-8
# 处理二进制文件

f = open('demo.wav', 'rb')
info = f.read(44)
print info

import struct

print struct.unpack('h', '\x01\x02')

print struct.unpack('h', info[22:24])  # h是说小段short
print struct.unpack('i', info[24:28])  # i是说int
print struct.unpack('h', info[34:36])

import array

f.seek(0, 2)  # 移到最尾
print f.tell()
n = (f.tell() - 44) / 2  # 计算出数据的长度

buf = array.array('h', (0 for _ in xrange(n)))
f.seek(44)
f.readinto(buf)

for i in xrange(n):
    buf[i] /= 8

f2 = open('demo2.wav', 'wb')
f2.write(info)
buf.tofile(f2)
f2.close()
