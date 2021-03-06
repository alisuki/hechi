#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-22

'''
------------------------------------------------------
模块，用一砣代码实现了某个功能的代码集合。 

类似于函数式编程和面向过程编程，函数式编程则完成一个功能，其他代码用来调用即可，提供了代码的重用性和代码间的耦合。而对于一个复杂的功能来，可能需要多个函数才能完成（函数又可以在不同的.py文件中），n个 .py 文件组成的代码集合就称为模块。

如：os 是系统相关的模块；file是文件操作相关的模块

----------------------------------------------------------------

导入模块有一下几种方法：
import module
from module.xx.xx import xx
from module.xx.xx import xx as rename 
from module.xx.xx import *

导入模块时是根据那个路径作为基准来进行的呢？即：sys.path
import sys
print sys.path

如果sys.path路径列表没有你想要的路径，可以通过 sys.path.append('路径') 添加。
import sys
import os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_path)

--------------------------------------------------------------

模块的常用方法：
from path import del        #从path导入模块del,del模块如果能被导入则path目录下必须得有这个文件：  __init__.py
del.remove()                #remove就是del模块里的一个函数
__name__                    #显示文件主次层级
if __name__ == '__main__'   #判断当前文件是否为主文件，常用于防止黑客攻击调用或破解
__file__                    #当前文件的路径
__doc__                     #当前文件的描述

------------------------------------------------------
模块分为三种：
    自定义模块
    内置模块
    第三方模块

自定义模块:略


内置模块：是Python自带的功能，在使用内置模块相应的功能时，需要【先导入】再【使用】

一、sys   --> 用于提供对Python解释器相关的操作：
sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0)
sys.version        获取Python解释程序的版本信息
sys.maxint         最大的Int值
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       返回操作系统平台名称
sys.stdin          输入相关
sys.stdout         输出相关
sys.stderror       错误相关


二、os    -->  用于提供系统级别的操作：
os.getcwd()                 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")         改变当前脚本工作目录；相当于shell下cd
os.curdir                   返回当前目录: ('.')
os.pardir                   获取当前目录的父目录字符串名：('..')
os.makedirs('dir1/dir2')    可生成多层递归目录
os.removedirs('dirname1')   若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')         生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')         删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')       列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()                 删除一个文件
os.rename("oldname","new")  重命名文件/目录
os.stat('path/filename')    获取文件/目录信息
os.sep                      操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep                  当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep                  用于分割文件路径的字符串
os.name                     字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")   运行shell命令，直接显示
os.environ                  获取系统环境变量
os.path.abspath(path)       返回path规范化的绝对路径
os.path.split(path)         将path分割成目录和文件名二元组返回
os.path.dirname(path)       返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)      返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)        如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)         如果path是绝对路径，返回True
os.path.isfile(path)        如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)         如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)      返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)      返回path所指向的文件或者目录的最后修改时间


三、hashlib    -->  用于加密相关的操作，代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法

import hashlib

# ######## md5 ########
hash = hashlib.md5()
# help(hash.update)
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())
print(hash.digest())
 
 
######## sha1 ########
hash = hashlib.sha1()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())
 
# ######## sha256 ########
hash = hashlib.sha256()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())
 
 
# ######## sha384 ########
hash = hashlib.sha384()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())
 
# ######## sha512 ########
hash = hashlib.sha512()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

以上加密算法虽然依然非常厉害，但时候存在缺陷，即：通过撞库可以反解。所以，有必要对加密算法中添加自定义key再来做加密。

# ######## md5 ########
hash = hashlib.md5(bytes('898oaFs09f',encoding="utf-8"))
hash.update(bytes('admin',encoding="utf-8"))
print(hash.hexdigest())

python内置还有一个 hmac 模块，它内部对我们创建 key 和 内容 进行进一步的处理然后再加密

import hmac
h = hmac.new(bytes('898oaFs09f',encoding="utf-8"))
h.update(bytes('admin',encoding="utf-8"))
print(h.hexdigest())

四、random   -->  生成随机码
import random
print(random.random())
print(random.randint(1, 2))
print(random.randrange(1, 10))


五、re  -->  python中re模块提供了正则表达式相关操作

字符：
　　. 匹配除换行符以外的任意字符
　　\w    匹配字母或数字或下划线或汉字
　　\s    匹配任意的空白符
　　\d    匹配数字
　　\b    匹配单词的开始或结束
　　^    匹配字符串的开始
　　$    匹配字符串的结束
次数：
　　* 重复零次或更多次
　　+    重复一次或更多次
　　?    重复零次或一次
　　{n}    重复n次
　　{n,}    重复n次或更多次
　　{n,m}    重复n到m次

Python中re模块中特殊转义序列（字符）
            \A    匹配字符串的开头
            \b    匹配一个空字符（仅对一个单词word的开始或结束有效）
            \B    与\b含义相反
            \d    匹配任何十进制数；它相当于类 [0-9]
            \D    匹配任何非数字字符；它相当于类 [^0-9]
            \s    匹配任何空白字符；它相当于类 [ \t\n\r\f\v]
            \S    匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]
            \w    匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]
            \W    匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
            \Z    匹配字符串的结尾
            
re.match  # match，从起始位置开始匹配，匹配成功返回一个对象，未匹配成功返回None
    match(pattern, string, flags=0)
     # pattern： 正则模型
     # string ： 要匹配的字符串
     # falgs  ： 匹配模式
         X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
         I  IGNORECASE  Perform case-insensitive matching.
         M  MULTILINE   "^" matches the beginning of lines (after a newline)
                        as well as the string.
                        "$" matches the end of lines (before a newline) as well
                        as the end of the string.
         S  DOTALL      "." matches any character at all, including the newline.
     
         A  ASCII       For string patterns, make \w, \W, \b, \B, \d, \D
                        match the corresponding ASCII character categories
                        (rather than the whole Unicode categories, which is the
                        default).
                        For bytes patterns, this flag is the only available
                        behaviour and needn't be specified.
          
         L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
         U  UNICODE     For compatibility only. Ignored for string patterns (it
                        is the default), and forbidden for bytes patterns.
    
    
    
re.search  -->  # search,浏览整个字符串去匹配第一个，未匹配成功返回None
    # search(pattern, string, flags=0)
    
    
re.findall  -->  # findall，在目标字符串查找符合规则的字符串,获取非重复的匹配列表；如果有一个组则以列表形式返回，且每一个匹配均是字符串；如果模型中有多个组，则以列表形式返回，且每一个匹配均是元祖；
    # 空的匹配也会包含在结果中
    # findall(pattern, string, flags=0)
    
sub  -->  # sub，替换匹配成功的指定位置字符串
    sub(pattern, repl, string, count=0, flags=0)
        # pattern： 正则模型
        # repl   ： 要替换的字符串或可执行对象
        # string ： 要匹配的字符串
        # count  ： 指定匹配个数
        # flags  ： 匹配模式
    
split  -->  # split，根据正则匹配分割字符串
    split(pattern, string, maxsplit=0, flags=0)
        # pattern： 正则模型
        # string ： 要匹配的字符串
        # maxsplit：指定分割个数
        # flags  ： 匹配模式
    
    
常用正则表达式：
    IP：
    ^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$
    手机号：
    ^1[3|4|5|8][0-9]\d{8}$
    邮箱：
    [a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+
    

六、序列化模块：用于序列化的两个模块  -->  json 和 pickle 

json，用于字符串 和 python数据类型间进行转换
pickle，用于python特有的类型 和 python的数据类型间进行转换

Json模块提供了四个功能：dumps、dump、loads、load
pickle模块提供了四个功能：dumps、dump、loads、load

pickle        #序列化模块，可将信息序列化后存进文件里，需要使用时反序列出来即可实现加密效果,同时还可用于内存数据共享交互
pickle.dump(li,open('./mypasswd','w'))    #将列表li序列化后存入文件--mypasswd
result = pickle.load(open('./mypasswd','r'))        #反序列化出来
print result

json        #同上，使用方法也都一样，但应用范围更广，可跨平台跨语言共享
name_dict = {'name':'Kevien','age':'32','sex':'man'}
obj = json.dumps(name_dict)
json.loads(obj)


七、configparser
configparser用于处理特定格式的文件，其本质上是利用open来操作文件。

 指定格式
1、获取所有节点
import configparser
 
config = configparser.ConfigParser()
config.read('xxxooo', encoding='utf-8')
ret = config.sections()
print(ret)

2、获取指定节点下所有的键值对
import configparser
 
config = configparser.ConfigParser()
config.read('xxxooo', encoding='utf-8')
ret = config.items('section1')
print(ret)

3、获取指定节点下所有的建
import configparser
 
config = configparser.ConfigParser()
config.read('xxxooo', encoding='utf-8')
ret = config.options('section1')
print(ret)

4、获取指定节点下指定key的值
import configparser
 
config = configparser.ConfigParser()
config.read('xxxooo', encoding='utf-8')

v = config.get('section1', 'k1')
# v = config.getint('section1', 'k1')
# v = config.getfloat('section1', 'k1')
# v = config.getboolean('section1', 'k1')
print(v)


5、检查、删除、添加节点
import configparser
 
config = configparser.ConfigParser()
config.read('xxxooo', encoding='utf-8')
 
# 检查
has_sec = config.has_section('section1')
print(has_sec)
 
# 添加节点
config.add_section("SEC_1")
config.write(open('xxxooo', 'w'))
 
# 删除节点
config.remove_section("SEC_1")
config.write(open('xxxooo', 'w'))


6、检查、删除、设置指定组内的键值对
import configparser
 
config = configparser.ConfigParser()
config.read('xxxooo', encoding='utf-8')
 
# 检查
has_opt = config.has_option('section1', 'k1')
print(has_opt)
 
# 删除
config.remove_option('section1', 'k1')
config.write(open('xxxooo', 'w'))
 
# 设置
config.set('section1', 'k10', "123")
config.write(open('xxxooo', 'w'))

八、XML
XML是实现不同语言或程序之间进行数据交换的协议，XML文件格式如下：
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2026</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>






----------------------------------------------------------

高级技术：
__import__ 反射技术，通过字串的形式导入模块，并以字串的形式执行函数
示例：
temp = 'sys'
model = __import__(temp)
func = getattr(model,'path')    #到model模块里找path函数,并传递给func
func()                    #相当于执行sys.path()



'''









