#!/usr/bin/env python
# coding=utf-8
# Kevien：vianus@qq.com  CreatDate:2016-12-20


print "\n",'#创建字典'
dicts = {'name':'Kevien','age':'23','sex':'男'}
print dicts

print "\n",'#新增项'
dicts['news']='news'
print dicts

print "\n",'#将dicts2合并更新到dicts，如键重复，则覆盖值'
dicts2 = {'ddd':'this ddd'}
dicts.update(dicts2)
print dicts

print "\n",'#如果key不存在，则创建，如果存在则返回key的值'
test = dicts.setdefault('test','Value')
print dicts
print test


print "\n",'#修改key的值'
dicts['news']='This is new Value'
print dicts

print "\n",'#获取Key的值'
print dicts.get('news')

print "\n",'#删除项(方法一)'
dicts.pop('news')
print dicts

print "\n",'#删除项(方法二)'
del dicts['age']
print dicts

print "\n",'#检查键是否存在'
print dicts.has_key('news')

print "\n",'#以列表的方式一次性输出所有项'
print dicts.items()

print "\n",'#循环读取每一项的键和值'
for i in dicts.iteritems():
    print i[0],i[1]

print "\n",'#列出字典内所有项的key'
print dicts.keys()

print "\n",'#列出字典内所有项的值'
print dicts.values()

print "\n",'#字典的浅拷贝'
dicts2 = {"c" : "orange", "d" : "banana"}
dicts2 = dicts.copy()
print dicts2

print "\n",'为可迭代的对象添加序号:enumrate'
li = [11,22,33]
for k,v in enumerate(li, 1):
    print(k,v)






















