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

### mysql

### redis

### theiaide

### vscode

 - 3e872a66951f52dcae42e84b

### ttyd

 services:
  ttyd1:
    image: tsl0922/ttyd
    ports:
      - 7681:7681
      
 services:
  ttyd2:
    image: cloudve/ttyd
    ports:
      - 7681:7681

### ruoyi

## volumes 存储

## 网络