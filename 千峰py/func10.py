# coding:utf-8

def func(a,b):
    c = 10

    def inner_func():
        s = a + b + c
        print(s)

    return inner_func


ifunc = func(6, 9)
ifunc1 = func(2, 8)

ifunc()         # 25
ifunc1()        # 20