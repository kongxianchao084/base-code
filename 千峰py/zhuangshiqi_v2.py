# coding:utf-8

import time


def decorate(func):
    def wrapper():
        print("正在校验中...")
        print("校验结束...")
        func()

    return wrapper


@decorate
def f1():
    print("------f1---------")


f1()


print("《《带参数装饰器》》")


def decorate(func):
    def wrapper(n):
        print("正在校验中")
        print("校验结束")
        func(n)
    return wrapper


@decorate
def f2(n):
    print("--------f2--------", n)


f2(2)


print("《《带参数装饰器(list)》》")


def decorate(func):
    def wrapper(*args, **kwargs):
        print("正在校验中")
        print("args", args)
        print("kwargs", kwargs)
        print("校验结束")
        func(*args, **kwargs)
    return wrapper


@decorate
def f3(*args, **kwargs):
    for stu in args:
        print(stu)
    for k,v in kwargs.items():
        print(k,"-->",v)


f3(*['孔小宝', '牛小敏'],a=10,b=20,c=30)
f3()

"""
正在校验中
args ('孔小宝', '牛小敏')
kwargs {'a': 10, 'b': 20, 'c': 30}
校验结束
孔小宝
牛小敏
a --> 10
b --> 20
c --> 30
"""