#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-22


'''
一、打开文件
文件句柄 = open('文件路径', '模式')
打开文件时，需要指定文件路径和以何等方式打开文件，打开后，即可获取该文件句柄，日后通过此文件句柄对该文件操作。

打开文件的模式有：

r ，只读模式【默认】
w，只写模式【不可读；不存在则创建；存在则清空内容；】
x， 只写模式【不可读；不存在则创建，存在则报错】
a， 追加模式【可读；   不存在则创建；存在则只追加内容；】
"+" 表示可以同时读写某个文件

r+， 读写【可读，可写】
w+，写读【可读，可写】
x+ ，写读【可读，可写】
a+， 写读【可读，可写】
 "b"表示以字节的方式操作

rb  或 r+b
wb 或 w+b
xb 或 w+b
ab 或 a+b
 注：以b方式打开时，读取到的内容是字节类型，写入时也需要提供字节类型
 
二、操作文件 （3.x）
class TextIOWrapper(_TextIOBase):

    def close(self, *args, **kwargs): # real signature unknown
        关闭文件
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        文件描述符  
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        刷新文件内部缓冲区
        pass

    def isatty(self, *args, **kwargs): # real signature unknown
        判断文件是否是同意tty设备
        pass

    def read(self, *args, **kwargs): # real signature unknown
        读取指定字节数据
        pass

    def readable(self, *args, **kwargs): # real signature unknown
        是否可读
        pass

    def readline(self, *args, **kwargs): # real signature unknown
        仅读取一行数据
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        指定文件中指针位置
        pass

    def seekable(self, *args, **kwargs): # real signature unknown
        指针是否可操作
        pass

    def tell(self, *args, **kwargs): # real signature unknown
        获取指针位置
        pass

    def truncate(self, *args, **kwargs): # real signature unknown
        截断数据，仅保留指定之前数据
        pass

    def writable(self, *args, **kwargs): # real signature unknown
        是否可写
        pass

    def write(self, *args, **kwargs): # real signature unknown
        写内容
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
三、管理上下文

为了避免打开文件后忘记关闭，可以通过管理上下文，即：
with open('log','r') as f:      
    ...
如此方式，当with代码块执行完毕时，内部会自动关闭并释放文件资源。

在Python 2.7 及以后，with又支持同时对多个文件的上下文进行管理，
即：
with open('log1') as obj1, open('log2') as obj2:
    pass


'''  

