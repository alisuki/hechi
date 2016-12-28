#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-23
'''
模块说明：
    1. 
'''
   
#mysqldb    
import time, MySQLdb    
   
#连接  mysql  
conn=MySQLdb.connect(host="localhost",user="root",passwd="")  
cursor = conn.cursor()   #创建游标 
n = cursor.execute("create database test;")     #创建数据库
n = cursor.execute("use test;")                 #使用test库
n = cursor.execute("create table person(id int(1),name varchar(255),created date);")   #创建数据表

#写入    
sql = "insert into user(id,name,created) values(%d,%s,%s)"   
param = ("aaa",int(time.time()))    
n = cursor.execute(sql,param)    
print n    
   
#更新    
sql = "update user set name=%s where id=3"   
param = ("bbb")    
n = cursor.execute(sql,param)    
print n    
   
#查询    
n = cursor.execute("select * from user")    
for row in cursor.fetchall():    
    for r in row:    
        print r    
   
#删除    
sql = "delete from user where name=%s"   
param =("aaa")    
n = cursor.execute(sql,param)    
print n    
cursor.close()    
   
#关闭    
conn.close() 