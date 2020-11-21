# coding:utf-8


stream = open(r'C:\Users\kongxianchao\Desktop\python工程\base-code\千峰py\aa.txt', 'w')
s = '''
你好!
    欢迎来到英雄联盟!
        提姆队长正在待命...
'''
stream.write(s)
stream.write('龙五')
stream.close()  # 释放管道资源
'''

你好!
    欢迎来到英雄联盟!
        提姆队长正在待命...
龙五
'''

# 管道关闭，再次写报错
# ValueError: I/O operation on closed file.
# stream.write('龙五2')

'''
写操作：
    write(内容) 每次都会清空原来内容，再次写入
'''
stream = open(r'C:\Users\kongxianchao\Desktop\python工程\base-code\千峰py\aa.txt', 'w')
stream.write('龙五4')
stream.close()
'''
龙五4
'''

# writelines(Iterable) 没有换行的动作，需要换行的话需要自己加换行实现
stream = open(r'C:\Users\kongxianchao\Desktop\python工程\base-code\千峰py\aa.txt', 'w')
print(stream.writable())
stream.writelines(["赌神高进\n", "赌侠\n", "赌圣"])
stream.close()
'''
True
赌神高进
赌侠
赌圣
'''
# a模式：追加
stream = open(r'C:\Users\kongxianchao\Desktop\python工程\base-code\千峰py\aa.txt', 'a')
stream.write("\n周星星")
stream.close()
'''
赌神高进
赌侠
赌圣
周星星
'''
