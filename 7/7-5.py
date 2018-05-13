from functools import total_ordering
from abc import abstractmethod


@total_ordering
class Shape(object):
    def __lt__(self, other):
        if not isinstance(other, Shape):
            raise TypeError('other is not Shape')
        return self.area() < other.area()

    def __eq__(self, other):
        if not isinstance(other, Shape):
            raise TypeError('other is not Shape')
        return self.area() == other.area()

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.14


r1 = Rectangle(5, 3)
r2 = Rectangle(4, 4)
c1 = Circle(3)

print r1 <= r2  # r1.__lt__(r2)
print c1 <= r1
# print r1 <= 1  # type error
