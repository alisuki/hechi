#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-20

num = 1
sumnum = 0
while num <=99:
    if num%2 == False:
        #print '-',num
        sumnum -= num
        print  '-',num,'=',sumnum
    else:
        #print '+',num
        sumnum += num
        print '+',num,'=',sumnum
    num += 1

print '计算结果为：',sumnum