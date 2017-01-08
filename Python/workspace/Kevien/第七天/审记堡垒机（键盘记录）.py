#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-30
'''
模块说明：
    1. 记录所有用户的键盘操作记录
'''
'''
源码下载：https://github.com/paramiko/paramiko.git 或：wget https://codeload.github.com/paramiko/paramiko/zip/master
再启动:demos/demos.py

安全机制：用户登陆后就记录，并且无法退出
类似于clonezilla的菜单功能

可通过用户的环境变量设置：$HOME/.bashrc
增加以下：
/usr/bin/python /home/hechi/menu.py        #用户登陆就自启动
logout                #彻底退出用户


*** 通过浏览器登陆主机终端： sudo apt-get install shellinabox
    启动：shellinaboxd -t
    默认端口：4022
    登陆：192.168.1.102:4200


'''