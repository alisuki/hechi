#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-20


'''
有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
即： {'k1': 小于66的所有值, 'k2': 大于66的所有值}
'''


list = [11,22,33,44,55,66,77,88,99,90]

Valus1 = []
Valus2 = []

for str in list:
    if str < 66:
        Valus1.append(str)
    if str > 66:
        Valus2.append(str)
print Valus1
print Valus2

dict = {"k1":Valus1,"k2":Valus2}
print dict
