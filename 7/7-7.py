import weakref


class Data(object):
    def __init__(self, value, owner):
        self.value = value
        self.owner = weakref.ref(owner)

    def __str__(self):
        return "%s's data, value is %s" % (self.owner(), self.value)

    def __del__(self):
        print 'in Data.__del__'


class Node(object):
    def __init__(self, value):
        self.data = Data(value, self)

    def __del__(self):
        print 'in Node.__del__'


node = Node(100)
del node
