# coding:utf-8

def outer(a):            # 第一层  负责接收装饰器参数
    def decorate(func):         # 第二层  负责接收函数
        def wrapper(*args, **kwargs):   # 第三层  负责接收函数的实参
            func(*args, **kwargs)
            print("铺地砖", a)
        return wrapper
    return decorate


@outer(10)
def house(time):
    print("我{}拿到房子钥匙,是毛坯房...".format(time))


@outer(100)
def street():
    print("新修的路是黑泉路.")


house('20101010')
street()

"""
我20101010拿到房子钥匙,是毛坯房...
铺地砖 10
新修的路是黑泉路.
铺地砖 100
"""