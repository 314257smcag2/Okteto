# docker

## 命令

### 拉取镜像

 - docker pull 镜像名
 - docker pull ubuntu
 - docker search httpd  （查找镜像）
 - docker rmi hello-world  （删除镜像）

### 列出镜像

 - docker images
 - docker image ls -a

### 运行容器

 - docker run 镜像名 命令 参数
 - docker run ubuntu /bin/echo "hello"

### 运行交互式容器

 - docker run -i -t ubuntu /bin/bash       退出 exit
 - docker run -i -t --name ubuntu_bash -p 80:80 ubuntu /bin/bash
 - --name 容器名
 - -p 开放端口
 - -i 允许stdin输入 in
 - -t 使用终端 terminal

### 后台运行容器

 - docker run -d --name hello ubuntu /bin/sh -c "while true; do echo hello; sleep 1; done"
 - docker run -d --name hello python /bin/sh -c "rm -rf okteto && git clone https://github.com/wwkiyyx/okteto && python ./okteto/app.py"
 - docker restart 容器名或ID  （重启容器）
 - docker restart hello
 - docker start 容器名或ID  （启动容器）
 - docker start hello 
 - docker stop 容器名或ID  （停止容器）
 - docker stop hello
 - docker logs 容器名或ID （查看输出）
 - docker logs hello
 - docker attach 容器  （进入容器）
 - docker exec -it 容器 /bin/bash  （在容器内运行命令）
 - docker export 容器 > ubuntu.tar  （导出容器）
 - docker port 容器  （查看容器端口）

### 列出容器

 - docker containers ls -a
 - docker ps -a
 
### 删除容器

 - docker rm -f hello

### 提交容器成为镜像

 - docker commit -m="baota" -a="wangwenkai" baota wwkiyyx/bt:baota_ubuntu  （容器名 -> 用户名/仓库:版本）
 - -m 说明信息 message
 - -a 作者 author

### 登录并推送镜像到 docker hub

 - docker login
 - docker logout
 - docker push 用户名/仓库:版本
 - docker push username/ubuntu:18.04
 - docker tag 860c279d2fec runoob/centos:dev  (建标签)
 - docker tag local-image:tagname new-repo:tagname
 - docker push new-repo:tagname

### 联网

 - docker network create -d bridge test-net
 - docker run -itd --name test1 --network test-net 网络 ubuntu /bin/bash                
 - ping test1
 - docker network ls    （列出w）

### DockerFile

 - docker build -t runoob/centos:6.7 .      
 - docker build -t wwkiyyx/ttyd:ubuntu_df .

Dockerfile                
--------------------------------------------------------------         
```bash          
FROM ubuntu        
EXPOSE 7681        
RUN apt update \     
    && apt upgrade -y \    
    && apt install wget -y \     
    && wget -c -O ttyd https://github.com/tsl0922/ttyd/releases/download/1.6.3/ttyd.x86_64 \     
    && chmod u+x ttyd        
```     
--------------------------------------------------------------           

docker pull ubuntu         
docker pull centos       

     