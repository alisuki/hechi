#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-18


#示例一：
def show1(arg):
    print arg
show1('Kevien')


#示例二：
def show2(*list):
    for item in list:
        print item
        
list = range(23)
show2(*list)


#示例三：
def show3(**dict):
    for item in dict.items():
        print item
        
dict = {'name':'Kevien','age':'28','sex':'man','job':'Boss'}
show3(**dict)        
