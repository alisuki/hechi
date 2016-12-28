#!/usr/bin/env python
# coding=utf8
'''
Created on 2016-12-19

@author: hechi
'''
#class 创建类
class Person(object):
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
        
person1 = Person('Kevien','28','男','Boss')
person2 = Person('Jack','33','男','test')
print person1.name,person1.age,person1.sex,person1.job
print person2.name,person2.age,person2.sex,person2.job