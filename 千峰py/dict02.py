# coding: utf-8

import json

'''
案例：
用户注册功能

username
password
email
phone
'''

print('----------------欢迎来到智联招聘用户注册----------------------')
register_user = []
while True:
	username = input("请输入用户名:")
	password = input("请输入密码:")
	repassword = input("请在输入密码:")
	email = input("请输入邮箱:")
	iphone = input("请输入电话:")

	# 定义字典
	user = {}
	# 保存信息到字典中
	user['username'] = username
	if password == repassword:
		user['password'] = password
	else:
		print('两者密码不一致.')
		continue
	user['email'] = email
	user['iphone'] = iphone

	# 保存到数据库
	register_user.append(user)

	answer = input("是否继续注册用户?yes/no")
	if answer != 'yes':
		break
print()
register_user = json.dumps(register_user,indent=4,ensure_ascii=False)
print("注册的用户信息:\n%s" % register_user)