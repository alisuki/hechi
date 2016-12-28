#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-20

import getpass

for i in range(3):
    user_name = raw_input('请输入用户名：')
    user_passwd = getpass.getpass('请输入密码：')
    
    if user_name == 'Kevien' and user_passwd == '123':
        print '登陆成功！'
        
    else:
        print '你还剩',i+1,'次机会，请重试！'
