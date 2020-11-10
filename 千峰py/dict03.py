# coding:utf-8

'''
	考试分数大于90分的人
'''

score_dict = {'张三':100,'李四':90,'王五':89,'赵六':99}

for name,score in score_dict.items():
	if score > 90:
		print("{}分数是{}，大于90分。".format(name,score))

# 几种遍历字典方式
print(score_dict.keys())                   # dict_keys(['张三', '李四', '王五', '赵六'])
print(score_dict.values())                 # dict_values([100, 90, 89, 99])
print(score_dict.items())                  # dict_items([('张三', 100), ('李四', 90), ('王五', 89), ('赵六', 99)])

# 其他操作函数
print('王五' in score_dict)                # True,判断是否在key里面
print(score_dict.get('王五'))              # 89(错误处理)
print(score_dict.get('王五1'))             # None(错误处理)