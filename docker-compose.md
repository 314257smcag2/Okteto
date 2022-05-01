# docker hub

## 操作系统

 - ubuntu
 - centos
 - debian
 - alpine
 - amazonlinux
 - oraclelinux
 - opensuse

## 编程环境

 - python
 - django
 - openjdk
 - maven
 - node
 - golang
 - php
 - gcc
 
## 应用

 - nginx
 - httpd
 - mysql
 - phpmyadmin
 - redis
 - redmine
 - odoo
 
# okteto

### tensorflow jupyter notebook
```
 services:   
  tf:   
    image: jupyter/tensorflow-notebook     
    ports:    
      - 8888:8888      
``` 
### jupyter notebook
```
 services:     
  jupyter:      
    image: jupyter/datascience-notebook
    ports:    
      - 8888:8888     
```     
### nginx
```
 services:   
  nginx:   
    image: nginx    
    restart : always     
    ports:    
      - 8080:8080    
      - 80:80      
```      
### httpd
```
 services:
  httpd:
    image: httpd
    ports:
      - 8080:8080
      - 80:80
```      
### baota
```
  baota:
    image: wwkiyyx/baota:ubuntu1
    ports:
      - 8888:8888
      - 80:80
```
```
services:
  baota:
    image: huxiansheng/baota
    ports:
      - 8080:8080
      - 80:80
      - 8888:8888
登陆地址 http://{{面板ip地址}}:8888
初始账号 username
初始密码 password
```
```
services:
  baota3:
    image: jangrui/baota
    ports:
      - 8080:8080
      - 80:80
      - 8888:8888
登陆地址 http://{{面板ip地址}}:8888
初始账号 username
初始密码 password
```
### appnode
 - docker pull sbwml/appnode
```
 docker run -dit --restart=always \
    --privileged \
    --cap-add SYS_ADMIN \
    -e container=docker \
    --network bridge \
    -p 8888:8888 \
    -p 443:443 \
    -p 80:80 \
    -v /data:/data \
    --name appnode \
    sbwml/appnode:latest \
    /usr/sbin/init
账户：admin
密码：admin
端口：8888
```
### mysql
```
version: '3.1'

services:

  db:
    image: mysql
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: example

  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
```
```
services:
  db:
    image: mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: wwk.567890
      MYSQL_DATABASE: mydb
  adminer:
    image: adminer     管理工具
    restart: always
    ports:
      - 8080:8080
```
```
services:
  db:
    image: mysql
    restart: always
    volumes:
      - mysqlfile:/var/lib/mysql      持久化保存数据
    environment:
      MYSQL_ROOT_PASSWORD: wwk.567890
      MYSQL_DATABASE: mydb
  phpmyadmin:
    image: phpmyadmin     管理工具
    restart: always
    ports:
      - 80:80
volumes:
  mysqlfile:           数据盘
```
### redis
```
services:
  redis:
    image: redis
    ports:
      - 6379:6379
    volumes:
      - redisfile:/data
  treenms:
    image: fuyong/treenms           管理工具
    ports:
      - 8080:8080
  phpredisadmin:
    image: erikdubbelboer/phpredisadmin                      管理工具
    environment:
      REDIS_1_HOST: redis
    ports:
      - 80:80
volumes:
  redisfile:
  treenms和phpredisadmin管理redis    带磁盘存储redis数据       拉取直接运行, 端口号为8080 默认用户名和密码都为treesoft
```
### theiaide
```
services:
  theiaide:
    image: theiaide/theia
    ports:
      - 3000:3000
      
services:
  theiaide:
    image: theiaide/theia-full
    volumes:
      - codefile:/home/project     持久化保存数据
    ports:
      - 3000:3000
      - 5000:5000
      - 80:80
      - 8080:8080
volumes:
  codefile:                 数据盘
```
### vscode
```
services:     
  code:    
    image: codercom/code-server   
    ports:        
      - 8080:8080 
```
```
services:     
  code:    
    image: codercom/code-server     
    command: code-server --auth none --bind-addr 0.0.0.0:8080     
    ports:        
      - 8080:8080          
```
### ttyd
 - cloudve/ttyd        tsl0922/ttyd          7681端口
 - ttyd -p 12345 bash
 - ttyd bash
 - https://github.com/tsl0922/ttyd
 - https://github.com/tsl0922/ttyd/releases/download/1.5.2/ttyd_linux.x86_64
 - https://github.com/tsl0922/ttyd/releases/download/1.6.3/ttyd.x86_64
```
wget -c -O ttyd https://github.com/tsl0922/ttyd/releases/download/1.6.3/ttyd.x86_64
chmod u+x ttyd
```
``` 
  sudo apt-get install build-essential cmake git libjson-c-dev libwebsockets-dev
  git clone https://github.com/tsl0922/ttyd.git
  cd ttyd && mkdir build && cd build
  cmake ..
  make && sudo make install
```
```
 services:
  ttyd:
    image: wwkiyyx/ttyd:ubuntu1
    ports:
      - 7681:7681
  ttyd1:
    image: tsl0922/ttyd
    ports:
      - 7681:7681
  ttyd2:
    image: cloudve/ttyd
    ports:
      - 7681:7681
```
### vnc
```
  ubuntulxde:
    image: dorowu/ubuntu-desktop-lxde-vnc
    ports:
      - 8080:80
      - 5900:5900
  ubuntuxfce:
    image: consol/ubuntu-xfce-vnc
    ports:
      - 8901:5901
      - 9901:6901
  centosxfce:
    image: consol/centos-xfce-vnc
    ports:
      - 8901:5901
      - 9901:6901
  xfce:
    image: christian773/xfce-vnc
    ports:
      - 8901:5901
      - 9901:6901
```
### ruoyi
 - spring-boot : https://gitee.com/y_project/RuoYi
 - vue : https://gitee.com/y_project/RuoYi-Vue
 - spring-cloud : https://gitee.com/y_project/RuoYi-Cloud
 - bootstrap : https://gitee.com/y_project/RuoYi-fast
 - vue : https://github.com/yangzongzhuan/RuoYi-Vue-fast
 - python : https://gitee.com/liqianglog/django-vue-admin
 - .net : https://github.com/liukuo362573/YiShaAdmin
```
services:
  redis:
    image: redis
  db:
    image: mysql
    restart: always
    volumes:
      - mysqlfile:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: wwk.567890
      MYSQL_DATABASE: ry
  phpmyadmin:
    image: phpmyadmin
    restart: always
    ports:
      - 80:80
  theiaide:
    image: theiaide/theia-full
    volumes:
      - codefile:/home/project
    ports:
      - 3000:3000
      - 8080:8080
      - 8081:1024
volumes:
  mysqlfile:
  codefile:
```
```
services:
  redis:
    image: redis
  db:
    image: mysql
    restart: always
    volumes:
      - mysqlfile:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: wwk.567890
      MYSQL_DATABASE: ry
  phpmyadmin:
    image: phpmyadmin
    restart: always
    ports:
      - 80:80
  theiaide:
    image: theiaide/theia-full
    volumes:
      - codefile:/home/project
      - jarfile:/home/project/RuoYi/ruoyi-admin/target
    ports:
      - 3000:3000
      - 8080:8080
      - 8081:1024
  java:
    image: openjdk
    command: java -jar /home/project/RuoYi/ruoyi-admin/target/ruoyi-admin.jar
    volumes:
      - jarfile:/home/project/RuoYi/ruoyi-admin/target
    ports:
      - 9090:8080
volumes:
  mysqlfile:
  codefile:
  jarfile:
```
## volumes 存储
```
services:
  tf:
    image: jupyter/tensorflow-notebook
    ports:
      - 8888:8888
    volumes:
      - files:/home/jovyan

volumes:
  files:
    driver_opts:
      size: 3Gi
```
## 网络
```
  owncloud:     
    image: owncloud:8.1    
    ports:     
      - 8080:80    
```