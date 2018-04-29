# coding=utf-8
import os
import stat
import time

s = os.stat('demo.txt')
print s.st_mode

print stat.S_ISDIR(s.st_mode)  # 是否是文件夹
print stat.S_ISREG(s.st_mode)  # 是否是普通文件

# 文件权限
print s.st_mode & stat.S_IRUSR  # 读权限，只要大于0 都是True
print s.st_mode & stat.S_IXUSR  # 执行权限

# 文件的三个时间
print s
print time.localtime(s.st_atime)  # 修改时间

# 普通文件的大小
print s.st_size

# OS path 方法
print os.path.isfile('demo.txt')
print os.path.isdir('demo.txt')
print os.path.getatime('demo.txt')
print os.path.getsize('demo.txt')

