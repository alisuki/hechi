#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-20


#判断
a=1
b=2
c=3
if a>b:
    print 'a>b'
elif a>c:
    print 'a>c'
else:
    print 'a没有大于b,也没有大于c'
    
#循环一
list = ['fdsa','fdsa','fdasf','iewk','ifwhqj']
for i in list:
    print i
    
for i in range(5):
    print i
    
#循环二
num = 0
while num <= 6:
    print num
    num += 1
    
#跳过本次循环，继续下次循环
#continue

#跳出循环
#break

print "\n",'为可迭代的对象添加序号:enumrate'
li = [11,22,33]
for k,v in enumerate(li, 1):
    print(k,v)


print "\n",'指定范围，生成指定的数字'
print range(1, 10)
print "# 结果：[1, 2, 3, 4, 5, 6, 7, 8, 9]"
 
print range(1, 10, 2)
print "# 结果：[1, 3, 5, 7, 9]"
 
print range(30, 0, -2)














