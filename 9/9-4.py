# coding=utf-8
# 9-4 如何实现属性可修改的函数装饰器

from functools import wraps
import time
import logging


def warn(timeout):
    timeout = [timeout]

    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            used = time.time() - start
            if used > timeout[0]:
                msg = '"%s" : %s > %s' % (func.__name__, used, timeout[0])
                logging.warn(msg)
            return res

        def setTimeout(k):
            timeout[0] = k

        wrapper.setTimeout = setTimeout

        return wrapper

    return decorator


from random import randint


@warn(1.5)
def test():
    print('In test')
    while randint(0, 1):
        time.sleep(0.5)


for _ in range(30):
    test()

test.setTimeout(1)
for _ in range(30):
    test()
