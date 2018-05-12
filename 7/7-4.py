# coding=utf-8
# 如何创建可管理的对象属性

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, value):
        if not isinstance(value, (int, long, float)):
            raise ValueError('Wrong type: ')
        self.radius = float(value)

    def get_area(self):
        return self.radius ** 2 * 3.14

    R = property(get_radius, set_radius)


c = Circle(3.2)
print c.R
c.R = 5.9
print c.R
