# coding:utf-8

def func(a, *args):
    print(a, args)


func(2, 3, 4, 5)  # 2 (3, 4, 5)
func(2, [1, 2, 3, 4])  # 2 ([1, 2, 3, 4],)
func(2, 3, [1, 2, 3, 4, 5])  # 2 (3, [1, 2, 3, 4, 5])
func(6, 6, (4, 5, 7), 9)  # 6 (6, (4, 5, 7), 9)


def func2(a, b=10, c=3, **kwargs):
    print(a, b, c, kwargs)


func2(1)  # 1 10 3 {}
func2(2, b=10)  # 2 10 3 {}
func2(1, 5, 7, d=1, e=2)  # 1 5 7 {'d': 1, 'e': 2}


def func3(a, *args, **kwargs):
    print(a, args, kwargs)


func3(1, 2, 3, 4)                                # 1 (2, 3, 4) {}
func3(1, [2, 5, 8], b=9, c=6)                    # 1 ([2, 5, 8],) {'b': 9, 'c': 6}