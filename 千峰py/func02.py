# coding:utf-8

'''
定义登陆函数，参数 username,password
函数体:
    判断username、password是否正确，正确登陆成功，失败打印登陆失败
'''


def login(username, password):
    uname = "孔小宝"
    pwd = 19931118
    if username == uname and password == pwd:
        print("登陆成功!")
    else:
        print("登陆失败!")


login("孔小宝", 19931118)