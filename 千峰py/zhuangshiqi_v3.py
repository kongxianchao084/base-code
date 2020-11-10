# coding:utf-8


def decorate1(func):
    print("decorate1 start")

    def wrapper():
        # 步骤1: func = house
        func()
        print("装修地板")

    print("decorate1 end")
    # 步骤2: wrapper是已经被装饰的func函数，简称wrapper1
    return wrapper


def decorate2(func):
    print("decorate2 start")

    def wrapper():
        # 步骤3: func = wrapper1
        func()
        print("装门")

    print("decorate2 end")
    return wrapper


@decorate2
@decorate1
def house():
    print("我是毛坯房")


house()

"""
输出结果：
    decorate1 start
    decorate1 end
    decorate2 start
    decorate2 end
    我是毛坯房
    装修地板
    装门
分析：
    多层装饰器，谁离得近先装饰谁，这里先装饰decorate1，将装饰后wrapper(wrapper1)在传
给装饰器2装饰.
    调用house时, house = wrapper(wrapper2) --> wrapper2 中func = wrapper1,
因此，先执行wrapper1，输出：
    我是毛坯房
    装修地板
    
    然后回到wrapper2内部执行，输出：
    装门
"""
