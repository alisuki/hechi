#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-22
'''
模块说明：
    1. 迭代器和生成器
'''

'''
1、迭代器

迭代器是访问集合元素的一种方式。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退，不过这也没什么，因为人们很少在迭代途中往后退。另外，迭代器的一大优点是不要求事先准备好整个迭代过程中所有的元素。迭代器仅仅在迭代到某个元素时才计算该元素，而在这之前或之后，元素可以不存在或者被销毁。这个特点使得它特别适合用于遍历一些巨大的或是无限的集合，比如几个G的文件

特点：

访问者不需要关心迭代器内部的结构，仅需通过next()方法不断去取下一个内容
不能随机访问集合中的某个值 ，只能从头到尾依次访问
访问到一半时不能往回退
便于循环比较大的数据集合，节省内存

>>> a = iter([1,2,3,4,5])
>>> a
<list_iterator object at 0x101402630>
>>> a.__next__()
1
>>> a.__next__()
2
>>> a.__next__()
3
>>> a.__next__()
4
>>> a.__next__()
5
>>> a.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration


2、生成器  yield:非常重要，需要再加强
一个函数调用时返回一个迭代器，那这个函数就叫做生成器（generator）；如果函数中包含yield语法，那这个函数就会变成生成器；

生成器，延迟技术，类似于响应式网页技术，遍历到的时候才输出，速度快，省内存
def foo():
    yield 1
    yield 2
    yield 3

re = foo()
for item in re:
    print item
    
    
def func():
    yield 1
    yield 2
    yield 3
    yield 4
上述代码中：func是函数称为生成器，当执行此函数func()时会得到一个迭代器。

>>> temp = func()
>>> temp.__next__()
1
>>> temp.__next__()
2
>>> temp.__next__()
3
>>> temp.__next__()
4
>>> temp.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

3、实例:利用生成器自定义range
def nrange(num):
    temp = -1
    while True:
        temp = temp + 1
        if temp >= num:
            return
        else:
            yield temp
'''
