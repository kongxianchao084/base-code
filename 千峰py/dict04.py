# coding:utf-8

score_dict = {'张三':100,'李四':90,'王五':89,'赵六':99}

del score_dict['王五']
print(score_dict)                                 # {'张三': 100, '李四': 90, '赵六': 99}
# del score_dict['哈哈']
# print(score_dict)                               KeyError: '哈哈'

# pop(k[,defaultValue])
value = score_dict.pop('张三',None)               # 弹出的是value
print("删除的key为:张三,值为:{}".format(value))    # 删除的key为:张三,值为:100

#popitem()  一般从末尾删除元素，逐个删除元素
print("*"*30)
print(score_dict)                                 # {'李四': 90, '赵六': 99}
value = score_dict.popitem()
print(value)                                      # ('赵六', 99)
print(score_dict)                                 # {'李四': 90}

# clear() 同list的clear 清空字典
score_dict.clear()
print(score_dict)                                 # {}