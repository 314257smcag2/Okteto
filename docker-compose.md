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

 services:   
  tf:   
    image: jupyter/tensorflow-notebook     
    ports:    
      - 8888:8888      
      
### jupyter notebook

 services:     
  jupyter:      
    image: jupyter/datascience-notebook
    ports:    
      - 8888:8888     
      
### nginx

 services:   
  nginx:   
    image: nginx    
    restart : always     
    ports:    
      - 8080:8080    
      - 80:80      
      
### httpd

 services:
  httpd:
    image: httpd
    ports:
      - 8080:8080
      - 80:80
      
### baota

  baota:
    image: wwkiyyx/baota:ubuntu1
    ports:
      - 8888:8888
      - 80:80

### mysql

### redis

### theiaide

### vscode

 - wwkiyyx/vscode:codeserver 密码 3e872a66951f52dcae42e84b
 - wwkiyyx/vscode:rooter 密码 1e4f218a91f701b18d4d5af4

### ttyd

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

### ruoyi

## volumes 存储

## 网络

    
  owncloud:     
    image: owncloud:8.1    
    ports:     
      - 8080:80    