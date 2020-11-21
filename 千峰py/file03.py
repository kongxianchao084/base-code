# coding:utf-8

'''
with结合open使用，可以帮我们自动释放资源，不需要手动调close()
文件夹不能open，会报权限问题，需要引入os模块实现
'''
# 文件的复制(读写模式)
with open(r'C:\Users\kongxianchao\Desktop\python工程\base-code\千峰py\aa.txt','r') as stream_r:
    container = stream_r.read()
    with open(r'C:\Users\kongxianchao\Desktop\python工程\base-code\千峰py\aa_copy.txt','w') as stream_w:
        stream_w.write(container)
print("复制文件成功.")