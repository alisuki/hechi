#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-21

'''
输出商品列表，用户输入序号，显示用户选中的商品
    商品 li = ["手机", "电脑", '鼠标垫', '游艇']
'''


li = ["手机", "电脑", '鼠标垫', '游艇']
dict = {}
for k,v in enumerate(li):
   print k, dict.setdefault(str(k),v)


while True:
    tmp = str(raw_input("\n请输入商品编号："))
    
    print dict[tmp]















