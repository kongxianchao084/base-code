# coding: utf-8


name = "孔小宝"


def func1():
    # 此处name是全局变量，要修改必须加global
    global name
    print(name)                       # 孔小宝
    name = "牛小宝"                    # local variable 'name' referenced before assignment
    print(name)                       # 牛小宝


def func2():
    # 局部变量
    name = "牛小宝"
    print(name)                       # 牛小宝
    name = "牛小宝1"
    print(name)


func1()
func2()
# 全局变量已经被修改
print(name)                           # 牛小宝


name_list = ['孔小宝','李晓敏','李雷']


def func3():
    print(name_list)
    name_list.append('克里斯')
    print(name_list)


func3()
print(name_list)