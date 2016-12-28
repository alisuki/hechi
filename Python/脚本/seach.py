#!/usr/bin/env python
# coding=utf-8

creat_file = file('test.txt','w')
creat_file.write('''root:x:0:0:root:/root:/bin/bash
                 daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
                 bin:x:2:2:bin:/bin:/usr/sbin/nologin
                 sys:x:3:3:sys:/dev:/usr/sbin/nologin
                 sync:x:4:65534:sync:/bin:/bin/sync
                 games:x:5:60:games:/usr/games:/usr/sbin/nologin
                 man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
                 lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
                 mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
                 news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
                 uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
                 proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
                 www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
                 backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
                 list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
                 irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
                 gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
                 nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
                 systemd-timesync:x:100:103:systemd Time Synchronization,,,:/run/systemd:/bin/false
                 systemd-network:x:101:104:systemd Network Management,,,:/run/systemd/netif:/bin/false
                 systemd-resolve:x:102:105:systemd Resolver,,,:/run/systemd/resolve:/bin/false
                 systemd-bus-proxy:x:103:106:systemd Bus Proxy,,,:/run/systemd:/bin/false
                 messagebus:x:104:111::/var/run/dbus:/bin/false
                 avahi:x:105:112:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
                 Debian-exim:x:106:114::/var/spool/exim4:/bin/false
                 statd:x:107:65534::/var/lib/nfs:/bin/false
                 colord:x:108:117:colord colour management daemon,,,:/var/lib/colord:/bin/false
                 dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/bin/false
                 geoclue:x:110:118::/var/lib/geoclue:/bin/false
                 speech-dispatcher:x:111:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/sh
                 pulse:x:112:120:PulseAudio daemon,,,:/var/run/pulse:/bin/false
                 rtkit:x:113:122:RealtimeKit,,,:/proc:/bin/false
                 saned:x:114:123::/var/lib/saned:/bin/false
                 usbmux:x:115:46:usbmux daemon,,,:/var/lib/usbmux:/bin/false
                 lightdm:x:116:124:Light Display Manager:/var/lib/lightdm:/bin/false
                 hplip:x:117:7:HPLIP system user,,,:/var/run/hplip:/bin/false
                 hechi:x:1000:1000:hechi,,,:/home/hechi:/bin/bash
                 mysql:x:999:999::/home/mysql:/bin/sh
                 ''')
creat_file.close()

f = file('test.txt','r')


seach = raw_input("请输入你要搜索的内容：")

for line in f.xreadlines():
    line = line.strip('\n')
    
    if line.find(seach)>0:
        print line.replace(seach,'''\033[0;31;40m%s\033[0m''' % seach)
