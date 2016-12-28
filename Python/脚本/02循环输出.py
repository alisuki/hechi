#!/usr/bin/env python
# coding=utf-8

print_num = input('请输入要打印的次数：')
count = 0
while count < 20:
    if count == print_num: 
        choice = raw_input('是否还继续打印？')
        if choice == 'n':
            break
        else:
            print_num = input('请输入要打印的次数:')

            while print_num < count:
                print "刚才已经打印过了"
                print_num = input('请输入要打印的次数:')
    else:
        print count
        count +=1
else:
    print "已计算完成了"
