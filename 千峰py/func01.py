# coding:utf-8

import random


# 定义函数


def generate_random(number):
    for i in range(10):
        ran = random.randint(1, number)
        print(ran)


number = 5
generate_random(number)

print("*" * 30)


# 求加法的函数
def add(a, b):
    sum = a + b
    print(sum)


add(3, 4)
