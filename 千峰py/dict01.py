# dictionary 字典
"""
字典
	特点：
	1.符号{}
	2.关键字 dict
	3. 保存的元素是 key:value
"""
# 定义

dict1 = {}        # 空字典  开发中建议使用该方法
dict2 = dict()    # 空字典
dict3 = {'ID':'929929393488494','name':'lucky','age':18}
dict4 = dict((('name','lucky'),('age',18)))
print(dict4)      # {'name': 'lucky', 'age': 18}
dict5 = dict(((1,2),(4,5),(6,8),(9,0)))
print(dict5)
dict6 = dict((('name','luck'),))             # 传给dict的元素要"成对存在",不加,表示传了两个元祖元素进去，会报错
print(dict6)      # {'name': 'luck'}

# 字典的增删改查

# 增加 dict[key] = value
# 特点：如果字典存在同名key，则发生值覆盖；如果字典不存在同名key，则增加(key,value)
dict6 = {}

dict6['brand'] = 'HuaWei'           
print(dict6)                       # {'brand': 'HuaWei'}  

dict6['brand'] = 'IphoneXR'        
print(dict6)                       # {'brand': 'IphoneXR'}

dict6['type'] = 'p30 pro'
dict6['price'] = 9000
dict6['color'] = '黑色'
print(dict6)                       # {'brand': 'IphoneXR', 'type': 'p30 pro', 'price': 9000, 'color': '黑色'}