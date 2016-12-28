#!/usr/bin/python 
# python tab file 
#使用时先将本脚本导入到python的模块目录，然后再import tab 
#一般目录在/usr/lib/python2.7;/usr/lib64/python2.7等地方
 
import sys 
import readline 
import rlcompleter 
import atexit 
import os 
# tab completion 
readline.parse_and_bind('tab: complete') 
# history file 
histfile = os.path.join(os.environ['HOME'], '.pythonhistory') 
try: 
    readline.read_history_file(histfile) 
except IOError: 
    pass 
atexit.register(readline.write_history_file, histfile) 
 
del os, histfile, readline, rlcompleter
