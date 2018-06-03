# coding=utf-8
# 定义带参数的装饰器
# 提取函数签名 inspect.signature()


def type_assert(*ty_args, **ty_kargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator
