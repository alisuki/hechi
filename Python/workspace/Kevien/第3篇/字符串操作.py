#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-20

msg = '''aaaaaa--bbbb|||ccccc 
text.capitalize  
text.isalnum     
text.lstrip      text.splitlines
text.center      text.isalpha     text.partition   text.startswith
text.count       text.isdigit     text.replace     text.strip
text.decode      text.islower     text.rfind       text.swapcase
text.encode      text.isspace     text.rindex      text.title
text.endswith    text.istitle     text.rjust       text.translate
text.expandtabs  text.isupper     text.rpartition  text.upper
text.find        text.join        text.rsplit      text.zfill
text.format      text.ljust       text.rstrip      
text.index       text.lower       text.split
'''
print "\n",'#首字母大写'
print msg.capitalize()

print "\n",'#字串串对齐排列'
for str in msg.split():     #msg.split() 为分割字串
    print '#后面的左对齐',str.ljust(30,' ')  #宽度50,用空格填充
for str in msg.split():
    print '#后面的居中对齐',str.center(30,' ')  #宽度50,用空格填充
for str in msg.split():
    print "#后面的右对齐",str.rjust(30)
    

print "\n",'#查找文本中字串xt的索引位置'
print msg.find('xt')   

print "\n",'#统计文本中字串text的个数'
print msg.count('text')

print "\n",'#将字串text替换成msg'
print msg.replace('text', 'msg')

print "\n",'#替换空格'
print msg.replace(' ','')

print "\n","#移除首尾的空白"
print '  注意前后空格    '
print '  注意前后空格  '.strip()

print "\n","#移除左侧空白"
print '  注意前后空格   '.lstrip()

print "\n","#移除右侧空白"
print '  注意前后空格    '.rstrip()


print "\n",'#分割字符串,默认以空格分割'
print msg.split('--')    
 
print "\n",'#分割成前，中，后三部分'
print msg.partition('count')

print "\n",'#按行分割成列表,参数True则保留换行符，默认为Flase'
print msg.splitlines(True)


print "\n",'#查找center的索引'
print msg.index('center')

print "\n",'''#字符串合并：'分隔符'.join('字符串或列表或元组或字典等')'''
lists = ['Kevien','test','dksa','age']
print ' | '.join(lists)

#



























