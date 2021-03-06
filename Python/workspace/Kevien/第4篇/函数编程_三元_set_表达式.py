#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-21

print '三元运算:是对简单的条件语句的缩写。'
# 书写格式 
print "result = 值1 if 条件 else 值2"
# 如果条件成立，那么将 “值1” 赋值给result变量，否则，将“值2”赋值给result变量

result = '大于' if 1>2 else '小于'        #如果为真则返回前面的值，否则返回后面的值。
print result

print '---------------------------------------'



print '''
set集合{}： 
set = {'test','fdsa','test','fewq'}
特点：类似于字典，无序，元素不重复
功能：关系测试，去重

set.add                          set.issubset
set.clear                        set.issuperset
set.copy                         set.mro
set.difference                   set.pop
set.difference_update            set.remove
set.discard                      set.symmetric_difference
set.intersection                 set.symmetric_difference_update
set.intersection_update          set.union
set.isdisjoint                   set.update


set集合运算：
x = {1,2,3,4}
y = {3,4,5,6}
x & y    #求交集，输出 x与y 里面都有的
x | y    #求并集，输出 x与y 去重
x - y    #求差集，输出 x的内容 与y不重复的部分
x ^ y    #求对称差集，输出x与y里面不重复的部分
  
  
基本操作：  

s = set(序列)        #创建一个set集合：s 
s = set('aaabbccdddddddddd')    #创建一个唯一字符的集合,结果：{'a','b','c','d'}
  
t.add('x')            # 添加一项  
  
s.update([10,37,42])  # 在s中添加多项    
  
t.remove('H')  #使用remove()可以删除一项，不存在报错
t.discard(*args, **kwargs): # 移除指定元素，不存在不会报错

len(s)          #set 的长度  
  
x in s          #测试 x 是否是 s 的成员  
  
x not in s      #测试 x 是否不是 s 的成员  
  
s.issubset(t)  或：s <= t    测试是否 s 中的每一个元素都在 t 中  
  
s.issuperset(t)  或：s >= t    测试是否 t 中的每一个元素都在 s 中  
  
s.union(t)  或：s | t    返回一个新的 set 包含 s 和 t 中的每一个元素  
  
s.intersection(t)   或： s & t    返回一个新的 set 包含 s 和 t 中的公共元素  
  
s.difference(t)  或：s - t   A中存在，B中不存在; 返回一个新的 set 包含 s 中有但是 t 中没有的元素  
s.difference_update(*args, **kwargs)    # 从当前集合中删除和B中相同的元素

s.symmetric_difference(t)   或：s ^ t    返回一个新的 set 包含 s 和 t 中不重复的元素  
  
s.copy()  #返回 set “s”的一个浅复制

s.clear()  #删除 set “s”中的所有元素

----------------------------------------------
'''


t = set(['a','b','c'])
s = set(['Hello Word!'])
print t
print s
print len(t)
 
print '''

函数编程：
def show1(arg)        #默认参数，如果要从数据库内读取传入100000个参数咋办？则使用以下参数
def show2(*arg)        #可变参数，未知实际需要传入多少个参数，此种这情况下，将多个参数封装成一个列表，然后传入
def show3(**arg)    #可变参数，同上，将字典作为参数传入
return                #返回跳出函数体
return('函数结束!')    #返回信息：'函数结束!'


'''

print "\n示例一："
def show1(arg):
    print arg
show1('Kevien')


print "\n示例二："
def show2(*list):
    for item in list:
        print item
        
list = range(5)
show2(*list)


print "\n示例三："
def show3(**dict):
    for item in dict:
        print item
        
dict = {'name':'Kevien','age':'28','sex':'man','job':'Boss'}
show3(**dict)        


print '------------------------------------------------'

print "\nlambda表达式:"
temp = lambda x,y,z:x*y+z        #  : 前为参数，: 后为运算
print temp
test2 = map(lambda x:x*2,range(10))
print test2

print "\n递归:"
'''
利用函数编写如下数列：

斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368...
'''
def func(arg1,arg2):
    if arg1 == 0:
        print arg1, arg2
    arg3 = arg1 + arg2
    print arg3
    if arg3 > 10000:
        return '运行结束！'
    func(arg2, arg3)        #调用函数本身进行循环
    
func(0, 1)

