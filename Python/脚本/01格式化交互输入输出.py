#!/usr/bin/python
#_*_coding:utf8_*_

name=raw_input('姓名：')
sex=raw_input('姓别：')
age=raw_input('年龄：')

print '''
-------------------------
以下是 %s 的个人信息：
	姓名：%s
	姓别：%s
	年龄：%d
-------------------------
''' % (name,name,sex,age)
