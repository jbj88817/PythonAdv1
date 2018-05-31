from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print 'In wrapper'
        func(*args, **kwargs)

    return wrapper


def example():
    print 'In example'


print example.__name__
print example.__doc__
