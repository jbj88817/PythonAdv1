# coding=utf-8
# 使用多进程
from multiprocessing import Process


def f(s):
    print s


p = Process(target=f, args=('hello',))
p.start()
