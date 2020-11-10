# coding: utf-8


def func():
    n = 100
    list1 = [3, 6, 9, 4]

    def inner_func():
        nonlocal n
        n = 50
        for i, v in enumerate(list1):
            list1[i] = v + n
        list1.sort()
    # 内部函数
    inner_func()
    print(list1)
    print(n)      # n=100
    print(locals())   # {'inner_func': <function func.<locals>.inner_func at 0x0000023B6FF41A60>, 'list1': [53, 54, 56, 59], 'n': 50}


func()            # [8, 9, 11, 14]
