# coding:utf-8

'''
    加入购物车
    判断用户是否登陆，如果登陆，成功加入购物车，否则提示登陆之后再添加
'''


islogin = False


def add_shop(goods_name):
    global islogin
    if islogin and goods_name:
        # 登陆的
        print("成功将{}加入到购物车".format(goods_name))
    else:
        # 没有登陆的
        print("用户没有登陆! 或者没有参加任何商品.")
        answer = input("用户没有登陆!是否登陆用户? (yes/no)")
        if answer == "yes":
            username = input("请输入用户名:")
            password = input("请输入登陆密码:")

            # 调用login(嵌套调用)
            islogin = login(username, password)
            print("是否登陆:", islogin)
        else:
            print("很遗憾!不能添加任何商品.")


def login(username, password):
    if username == '孔小宝' and password == "19931118":
        islogin = True
        print("用户登陆成功")
    else:
        islogin = False
        print("用户登陆失败")
    return islogin


username = input("请输入用户名:")
password = input("请输入登陆密码:")


islogin = login(username, password)                  # islogin：全局变量
add_shop("macBook Pro")
