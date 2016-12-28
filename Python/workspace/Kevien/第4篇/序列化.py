#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-18

#方法一：
list = ['name','age',23,532,12,'sex','job']
import pickle
#将list进行序列化，并存入pickle_out.txt
pickle.dump(list,open('pickle_out.txt','w'))

#将pickle_out.txt文件内容反序列化
result = pickle.load(open('pickle_out.txt','r'))
print result

#方法二：主流
import json
name_dict = {'name':'Kevien','age':'32','sex':'man'}
sult_json = json.dumps(name_dict)
print sult_json
result_json = json.loads(sult_json)
print result_json








