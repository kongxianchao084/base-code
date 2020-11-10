# coding:utf-8


'''
可变参数：结合关键字参数一起使用
'''


# 定义方式
# 知识点2: 赋值
def add(name, *args):                  # 知识点1: 装包
    print(args)
    print(*args)                 # 1 2 3   知识点3：拆包
    sum = 0
    if len(args) > 0:
        for i in args:
            sum += i
    print('{}计算的总和:{}'.format(name, sum))


add('孔小宝',1,2,3)                 # 孔小宝计算的总和:6
add('孔小宝',*(4,5,6))              # 孔小宝计算的总和:15
# add((1,2,3))                     # ((1, 2, 3),)


# 知识点4-2：字典装包
def func(**kwargs):
    print(kwargs)                  # {'a': 1, 'b': 2, 'c': 3}
    # print(**kwargs)              报错


func(a=1,b=2,c=3)
a = {'001':111,'002':222,'003':333}
func(**a)                         # 知识点4-1：字典拆包  001=111,002=222,003=333

print("*"*30)


def add2(name,a,b=20,c=20):
    sum = a + b + c
    print("{}计算的总和是:{}".format(name,sum))


add2('孔小宝',2,c=30)