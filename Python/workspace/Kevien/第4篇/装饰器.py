#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-19


#装饰器：为原有函数增加装饰内容
def warter(fun):
    def newfun(arg):
        print "验证信息"
        fun(arg)
    return newfun

@warter     #关联并将src1作为参数传递给 fun
def src1(arg):
    print "内容操作:1",arg
    
@warter     #关联并将src2作为参数传递给 fun
def src2(arg):
    print "内容操作2",arg
    
@warter     #关联并将src3作为参数传递给 fun
def src3(arg):
    print "内容操作3",arg
    

src1('Kevien')
src2('jack')
src3('susse')



