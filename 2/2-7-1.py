# coding=utf-8
from collections import deque
from random import randint
import pickle

N = randint(0, 100)
history = deque([], 5)


# history = pickle.load(open('history'))

def guess(k):
    if k == N:
        print 'right'
        return True
    if k < N:
        print '%s is less than N' % k
    else:
        print '%s is greater than N' % k
    return False


while True:
    line = raw_input('Please input a number: ')
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print list(history)  

pickle.dump(history, open('history', 'w'))  # 把队列存入文件
