# coding:utf-8

'''
加入购物车,付款，修改收获地址......
判断用户登陆状态
'''


# 地址引用
# def test():
#     print("-------test-----------")
#
#
# t = test
# t()
# print(id(t), id(test))  # 1756837630432 1756837630432


# 定义装饰器
def decorate(func):
    a = 100
    print("wrapper外层打印测试.")

    def wrapper():
        func()
        print("刷漆")
        print("铺地板", a)
        print("装门")

    print("wrapper外层打印结束.")
    print("wrapper地址:", id(wrapper))
    return wrapper


@decorate
def house():
    print("我是毛坯房")


print("house地址:", id(house))
house()

"""
输出结果:
    wrapper外层打印测试.
    wrapper外层打印结束. 
    我是毛坯房
    刷漆
    铺地板 100
    装门
分析:
    @decorate 等同于 houce = decorate(houce)，此时houce = wrapper，内部函数已经被返回. 
因此，打印出前两行(此时wrapper还没有被调用).
    houce() 调用wrapper函数，因此，打印出内部函数的内容，进行装饰. 
"""
