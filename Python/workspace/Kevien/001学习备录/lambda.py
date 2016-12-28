#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-18

#三元运算
result = '大于' if 1>2 else '小于'		#如果为真则返回前面的值，否则返回后面的值。
print result

#高级技术
test = [x*x for x in range(10)]
print test

#lambda运算，相当于简易函数
temp = lambda x,y,z:x*y+z       #：前部相当于参数，：后部相当于函数内运算
print temp(3,23,5)

test2 = map(lambda x:x*2,range(10))
print test2

















