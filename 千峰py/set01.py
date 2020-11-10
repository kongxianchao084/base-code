# coding:utf-8

list1 = [3,5,8,9,1,8,4,2,5,8,9]

s1 = set()
s2 = {1,2,3}
print(type(s1),type(s2))              # <class 'set'> <class 'set'>

s3 = set(list1)
print(s3)                             # {1, 2, 3, 4, 5, 8, 9}


# 添加
s1.add('hello')
s1.add('小猪佩奇')
print(s1)                             # {'hello', '小猪佩奇'}

t1 = ('林志林','言承旭')
s1.update(t1)
s1.add(t1)
print(s1)                             # {'言承旭', ('林志林', '言承旭'), '小猪佩奇', '林志林', 'hello'}


# 删除
# s1.remove('言承旭1')                  # KeyError: '言承旭1'
s1.pop()                               
s1.clear()