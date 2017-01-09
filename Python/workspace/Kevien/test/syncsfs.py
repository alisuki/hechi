#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-21

import sys
import os

print "脚本名：", sys.argv[0]

   

os.mkdir('/tmp/sfs')
os.mkdir('/tmp/sys')

#挂载sfs文件
#os.system(mount -t squashfs sys.argv[1] '/tmp/sys')

print (sys.argv[1])

#挂载分区
#os.system(mount sys.argv[2] '/tmp/sys')

list= os.listdir('/tmp/sys')
#print "\n",sys.argv[2],"分区内包含以下文件将被删除：\n",list,"\n"
question = raw_input("是否确定继续 [Y/N]：" )


sys.exit()


'''

    if [ "$question" = "Y" ] ; then    
        #恢复数据
        echo $question
        os.system("rsync -avP --delete --include='dev' --include='lost+found' --include='proc' --include='sys' --include='tmp' --include='srv' --include='run" sfs/ $sys/)
        sudo umount $sfs $sys
        zenity --info --title="恢复成功" --text="\n已恢复完成，请检查fstab文件！"
    elif [ "$question" = "y" ]; then
        echo $question
        gksu -u root -D 正在恢复文件 "rsync -avP --delete --include='dev' --include='lost+found' --include='proc' --include='sys' --include='tmp' --include='srv' --include='run" $sfs/ $sys/
        sudo umount $sfs $sys
        zenity --info --title="恢复成功" --text="\n已恢复完成，请检查fstab文件！"
    else
        zenity --error --timeout=3 --text="本次操作已取消！"
        exit;
    fi
  



uuid=${uuid#*UUID=\"}
echo ${uuid:0:36}

b=${a//123/321}


'''