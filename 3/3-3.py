# coding=utf-8
# 使用生成器函数实现可迭代对象


class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @staticmethod
    def is_prime_num(k):
        if k < 2:
            return False

        for i in xrange(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in xrange(self.start, self.end + 1):
            if self.is_prime_num(k):
                yield k


for x in PrimeNumbers(1, 100):
    print x
