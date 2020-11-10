# coding:utf-8

import time

is_login = False


def login():
    """
    登陆函数
    """
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username == "孔小宝" and password == "19931118":
        return True
    else:
        return False


def outer(name):
    def login_required(func):
        """
        登陆验证
        """
        def wrapper(*args, **kwargs):
            global is_login
            if is_login:
                func(*args, **kwargs)
            else:
                # 跳转到登陆页面
                is_login = login()
                if is_login:
                    print("{}登陆成功.".format(name))
                    func(*args, **kwargs)
                else:
                    print("{}未登陆.不能付款...".format(name))
        return wrapper
    return login_required


@outer("孔小宝")
def pay(money):
    """
    付款函数
    """
    print("正在付款,付款金额是{}".format(money))
    print("付款中....")
    time.sleep(2)
    print("付款完成.")


pay(10000)
