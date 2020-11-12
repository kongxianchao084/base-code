# coding:utf-8

'''
语法:
    lambda 参数:返回值
'''


# 匿名函数作为参数
def add(x, y, func):
    print(x)
    print(y)
    print(func)
    s = func(x, y)
    print(s)


add(1, 2, lambda x, y: x + y)

# lambda判断语句
print(list(map(lambda x: x if x % 2 == 0 else x + 1, [1, 2, 3, 4])))  # [2, 2, 4, 4]

# 内置函数+lambda函数
# max比较 key=lambda 此处lambda作为参数传递
list2 = [{'a': 10, 'b': 21}, {'a': 13, 'b': 22}, {'a': 9, 'b': 24}, {'a': 29, 'b': 20}]
print(max(list2, key=lambda x: x['a']))  # {'a': 29, 'b': 20}
print(max(list2, key=lambda x: x['b']))  # {'a': 9, 'b': 24}

# 迭代列表
# map(func, *iterable)
print(list(map(lambda x: x * 2, [1, 2, 3, 4])))  # [2, 4, 6, 8]

# reduce(func,sequence序列,initial=None)
from functools import reduce

tuple1 = (3, 5, 7, 8, 9, 1)
tuple2 = (3,)
print(reduce(lambda a, b: a + b, tuple1))  # 33
print(reduce(lambda a, b: a if a > b else b, tuple1))  # 9 和max效果一样
print(reduce(lambda x, y: x if x['a'] > y['a'] else y, list2))  # {'a': 29, 'b': 20}
print(reduce(lambda x, y: x + y, tuple2))  # 3

# 过滤
# filter(func, iterable)
print(list(filter(lambda x: x < 10, list(range(50)))))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 案例：求student age大于20岁的
students = [
    {'name': 'tom', 'age': 20},
    {'name': 'lucy', 'age': 19},
    {'name': 'lily', 'age': 13},
    {'name': 'mark', 'age': 21},
    {'name': 'jack', 'age': 23}
]

# print(list(map(lambda x: x['age'] > 20, students)))    # [False, False, False, True, True]
# print(list(map(lambda x: x if x['age'] > 20 else x.clear(),students)))  # [None, None, None, {'name': 'mark', 'age': 21}, {'name': 'jack', 'age': 23}]
print(students)
result = filter(lambda x: x['age'] > 20, students)
print(list(result))
print(students)

# 按照年龄最小到大排序
result = sorted(students, key=lambda x: x['age'])
print(result)

