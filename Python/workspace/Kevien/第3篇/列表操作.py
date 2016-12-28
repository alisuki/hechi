#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-20


print "\n",'#创建列表'
lists = ['name','age','sex','job',99]
print lists

print "\n",'#统计列表元素的个数'
print len(lists)

print "\n",'#访问列表中的值,按序列'
print lists[2]

print "\n",'#截取列表中的值'
print lists[1:3]

print "\n",'#更新列表'
lists[4] = 'fdsafdas'
print lists[4]

print "\n",'删除列表元素'
del lists[4]
print lists

print "\n",'新增元素'
lists.append('new_str')
print lists

print "\n",'在列表末尾一次性追加另一个序列中的多个值'
seq = ['fdas','dd','cc']
lists.extend(seq)
print lists

print "\n",'#对原列表进行排序'
lists.sort()
print lists

print "\n",'#将元组转换为列表,注意括号'
tuples = ('Kevien','susse','phoene')
print tuples
print list(tuples)






















