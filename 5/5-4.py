# coding=utf-8
import mmap

f = open('demo.bin', 'r+b')
print f.fileno()
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
m[0] = '\x88'
m[4:8] = '\xff' * 4

m = mmap.mmap(f.fileno(), mmap.PAGESIZE * 8, access=mmap.ACCESS_WRITE, offset=mmap.PAGESIZE * 4)
m[:0x1000] = '\xaa' * 0x1000

# 用 od -x demo.bin 查看
