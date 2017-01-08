
sudo rsync libpepflashplayer.so /usr/lib/chromium/ 
sudo chmod 755 /usr/lib/chromium/libpepflashplayer.so 
sudo rsync -av default /etc/chromium.d/default

然后到
chrome://plugins/
启用 Adobe Flash Player 始终充许运行
