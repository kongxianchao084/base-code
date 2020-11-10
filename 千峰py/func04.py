# coding:utf-8

# 关键字参数
def add(a, b=10):
    result = a + b
    print(result)


add(2)


def add1(a, b=10, c=2):
    print(a,b,c)
    result = a + b + c
    print(result)


# 知识点1：覆盖已存在参数
add1(2, 3)          # 给b赋值成功，被覆盖
add1(2, c=3)        # 知识点2： 通过关键字参数赋值给指定参数


# 打印每位同学的名字和年龄
students = {'001':('孔小宝',24),'002':('孔大宝',25),'003':('孔大宝宝',26),'004':('易烊千玺',27)}


def print_boy(students):
    if isinstance(students,dict):
        values = students.values()
        for name, age in values:
            print("{}的年龄是{}.".format(name,age))


print_boy(students)