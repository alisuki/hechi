#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open('pickle.py','r')
t = f.read().split('\n')
text = ''
for i in t:
#	print i[3:]
	text = text + i[3:] + '\n'

new = open('newfile.py','w')
new.write(text)
new.close()
f.close()
