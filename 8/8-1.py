# coding=utf-8
# 如何使用多线程

from threading import Thread


class MyThread(Thread):
    def __init__(self, sid):
        Thread.__init__(self)
        self.sid = sid

    def run(self):
        pass
