# rinetd 端口转发

 - apt-get install rinetd
 - 编辑 /etc/rinetd.conf  0.0.0.0 1234 127.0.0.1 22     （ bindaddress bindport connectaddress connectport ）
 - rinetd -c /etc/rinetd.conf 
 - pkill rinetd 