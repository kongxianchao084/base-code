# coding:utf-8

import random

'''
用户登陆
输入用户名
输入密码
输入验证码  --- 封装成一个函数
'''


# 验证码函数
def generate_checkpoint(n):
    s = '0987654321abcdefghigklmnopQJSPWJLKJEOJOESKJOWPJPSDLJSOIJWOJLAJLKSLPWMLCMOJOWJS'
    # 随机数长度
    code = ''
    for i in range(n):
        ran = random.randint(0, len(s) - 1)
        code += s[ran]
    return code


def login():
    username = input("请输入你的名字:")
    password = input("请输入你的密码:")
    code = generate_checkpoint(5)
    print("验证码是:", code)
    code_tmp = input("请输入验证码:")
    # 验证
    if code.lower() == code_tmp.lower():
        if username == "孔小宝" and password == "19931118":
            print("用户登陆成功.")
        else:
            print("用户名和密码有误.")
    else:
        print("验证码输入有误.")


# 调用
login()