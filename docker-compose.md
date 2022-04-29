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
### redis

### theiaide

### vscode

services:     
  code:    
    image: codercom/code-server   
    ports:        
      - 8080:8080             

services:     
  code:    
    image: codercom/code-server     
    command: code-server --auth none --bind-addr 0.0.0.0:8080     
    ports:        
      - 8080:8080          

### ttyd
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
### ruoyi

## volumes 存储

## 网络
```
  owncloud:     
    image: owncloud:8.1    
    ports:     
      - 8080:80    
```