#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-18


import hashlib
hashmd5 = hashlib.md5()
print hashmd5

hashmd5.update('admin')
print hashmd5.hexdigest()   #输出16进制
print hashmd5.digest()      #













