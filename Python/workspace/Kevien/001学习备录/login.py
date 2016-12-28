#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-18


def login(username):
    if username == 'Kevien':
        return '登陆成功'
    else:
        return '登陆失败'



user_name = raw_input("请输入用户名：")

#调用函数返回的信息赋值到变量
return_login = login(user_name)

if __name__ == '__main__':
    if return_login == '登陆成功':
        print return_login,'你现在可以干活了'
    else:
        print return_login
else:
    print '非法调用！'  










