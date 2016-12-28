#!/usr/bin/env python
# coding=utf-8
list = [0, 1, 2, 'Kevien', '4', 5, 'Kevien', 7, 8, 9, 'Kevien', 't', 'h']
start=0
for i in range(list.count('Kevien')):
    output = list.index('Kevien',start)
    print "Kevien的索引号为：",output
    start = output + 1
    print start


