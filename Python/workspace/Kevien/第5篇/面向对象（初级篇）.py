#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-22
'''
模块说明：
    1. 
'''

'''
概述

面向过程：根据业务逻辑从上到下写垒代码
函数式：将某功能代码封装到函数中，日后便无需重复编写，仅调用函数即可
面向对象：对函数进行分类和封装，让开发“更快更好更强...”
面向过程编程最易被初学者接受，其往往用一长段代码来实现指定功能，开发过程中最常见的操作就是粘贴复制，即：将之前实现的代码块复制到现需功能处。

创建类和对象

面向对象编程是一种编程方式，此编程方式的落地需要使用 “类” 和 “对象” 来实现，所以，面向对象编程其实就是对 “类” 和 “对象” 的使用。

　　类就是一个模板，模板里可以包含多个函数，函数里实现一些功能

　　对象则是根据模板创建的实例，通过实例对象可以执行类中的函数
'''

#class 创建类
class Person(object):       #Person为类名
    '''
    类的注释
    '''
    # def  __init__ 实例初始化类的函数，包含：name,age,sex,job
    def __init__(self, name,age,sex,job):
        '''
        Constructor
        '''
        self.name = name
        self.age = age
        self.sex = sex
        self.job = job
        
    # self 为特殊参数，必填！类中定义的函数叫做 “方法”
    def Bar(self)     　　     
        print 'Bar'
    #类中的函数第一个参数必须是self（详细见：类的三大特性之封装）
    def Hello(self, name):      
        print 'i am %s' %name

obj = Person()          # 根据类Foo创建对象obj
obj.Bar()               #执行Bar方法
obj.Hello('wupeiqi')    #执行Hello方法　

        
person1 = Person('Kevien','28','男','Boss')      #此处person1相当于形式参数self
person2 = Person('Jack','33','男','test')
print person1.name,person1.age,person1.sex,person1.job
print person2.name,person2.age,person2.sex,person2.job




#类：
class MyClass(obj):                    #class 创建类

    test0 = "这是一个静态字段，即变量"    #test0 即：静态字段
    def Pro(self,name,age,sex):
        self.name = name            

test1 = MyClass('Kevien','22','男')    #test1 就是对象
print test1.name                      #self.name 就是动态字段


@staticmethod
def test2():                        #静态方法
    print "注意这是没有传参数的函数"


@property
def    test3(self):                #动态方法
    print self.name    

print test1.test3()        

#非常重要：私有字段与方法：主要为了考虑安全性，比如说认证方式，不让别人从外部访问，要不容易被人破解
#私有字段：只有在类的内部才能调用
self.__show1 = flag

#私有方法：只有在类的内部才能调用
def __show2(self):



























'''

