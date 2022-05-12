# okteto

 - https://cloud.okteto.com/
 - 现在可以使用git仓库里的docker-compose.yml定义
 - https://github.com/okteto/python-docker-compose
 - https://github.com/okteto/compose-getting-started
 - https://github.com/okteto
 - https://github.com/okteto/movies
 - https://github.com/okteto/react-getting-started
 - https://github.com/okteto/go-getting-started
 - https://github.com/okteto/aspnetcore-getting-started
 - https://github.com/okteto/java-maven-spring-redis
 - https://github.com/okteto/filemanager
 - https://github.com/okteto/python-getting-started
 - https://github.com/okteto/php-getting-started
 - https://github.com/okteto/ruby-getting-started
 - https://github.com/okteto/rust-getting-started
 - https://github.com/okteto/node-getting-started
 - https://github.com/okteto/c-getting-started
 - https://github.com/okteto/java-gradle-getting-started
 - https://github.com/okteto/java-maven-getting-started
 - https://github.com/okteto/spring-microservices
 - https://github.com/okteto/tensorflow-notebook-getting-started
 - window 下载 : https://downloads.okteto.com/cli/okteto.exe
 - github release : https://github.com/okteto/okteto/releases
 - https://github.com/okteto/okteto/releases/download/2.2.1/okteto.exe
 - https://github.com/okteto/okteto/releases/download/2.2.1/okteto-Linux-x86_64


## play with docker 

 - docker pull wwkiyyx/baota:ubuntu
 - docker run -d --name baota1 -p 8888:8888 -p 80:80 wwkiyyx/baota:ubuntu /bin/sh -c "/etc/init.d/ssh start; bt 1; while true; do sleep 100; done"
 - 安装nginx、PHP、okteto-cli
 - docker commit -m="baota" -a="wwkiyyx" baota wwkiyyx/okteto:baota
 - docker push wwkiyxx/okteto:baota
```
入口:wwkiyyx
用户:wwkiyyx
密码:880510
```
```

Linux 下载安装脚本 : curl https://get.okteto.com -sSfL | sh

cd /root
export OKTETO_TOKEN=PIvcZLzke6uwKVnuyfu8605hYjW7eqMbjClM3Xv2V8yJaRcB
okteto context use https://cloud.okteto.com
okteto version
okteto context list
okteto namespace wwkiyyx
okteto namespace a-wwkiyyx
okteto namespace b-wwkiyyx
okteto namespace c-wwkiyyx
okteto namespace d-wwkiyyx
okteto up
okteto down

```

```

root@vscode-7c8c874f8f-8sg4w:/home/coder# curl https://get.okteto.com -sSfL | sh
> Downloading https://github.com/okteto/okteto/releases/latest/download/okteto-Linux-x86_64
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 61.0M  100 61.0M    0     0   198k      0  0:05:15  0:05:15 --:--:--  124k
> Installing /usr/local/bin/okteto
> Okteto successfully installed!

root@vscode-7c8c874f8f-8sg4w:/home/coder# export OKTETO_TOKEN=PIvcZLzke6uwKVnuyfu8605hYjW7eqMbjClM3Xv2V8yJaRcB

root@vscode-7c8c874f8f-8sg4w:/home/coder# okteto context use https://cloud.okteto.com
 ✓  Context 'cloud.okteto.com' created
 ✓  Using context wwkiyyx @ cloud.okteto.com

root@vscode-7c8c874f8f-8sg4w:/home/coder# okteto version
okteto version 2.2.2 

root@vscode-7c8c874f8f-8sg4w:/home/coder# okteto context list
Name                        Namespace  Builder                               Registry
https://cloud.okteto.com *  wwkiyyx    tcp://buildkit.cloud.okteto.net:1234  registry.cloud.okteto.net

root@vscode-7c8c874f8f-8sg4w:/home/coder# okteto namespace list
Namespace  Status
a-wwkiyyx  Active
b-wwkiyyx  Active
c-wwkiyyx  Active
d-wwkiyyx  Active
wwkiyyx *  Active
root@vscode-7c8c874f8f-8sg4w:/home/coder# okteto namespace wwkiyyx
 ✓  Using context wwkiyyx @ cloud.okteto.com

root@vscode-7c8c874f8f-8sg4w:/home/coder# okteto init
 i  Using wwkiyyx @ cloud.okteto.com as context
 ✓  Okteto manifest (okteto.yml) deploy and build configured successfully
 ?  Do you want to launch your development environment? [y/n]: y
 i  Images were already built. To rebuild your images run 'okteto build' or 'okteto deploy --build'
 ?  Do you want to configure your development containers? [y/n]: y
 ✓  Okteto manifest (okteto.yml) configured successfully
 i  Run 'okteto up' to activate your development container


```
```
name: coder

# The build section defines how to build the images of your development environment
# More info: https://www.okteto.com/docs/reference/manifest/#build
# build:
#   my-service:
#     context: .


# The deploy section defines how to deploy your development environment
# More info: https://www.okteto.com/docs/reference/manifest/#deploy
deploy:
  commands:
    - name: Deploy
      command: echo 'Replace this line with the proper 'helm' or 'kubectl' commands to deploy your development environment'

# The dependencies section defines other git repositories to be deployed as part of your development environment
# More info: https://www.okteto.com/docs/reference/manifest/#dependencies
# dependencies:
#   - https://github.com/okteto/sample
# The dev section defines how to activate a development container
# More info: https://www.okteto.com/docs/reference/manifest/#dev
# dev:
#   sample:
#     image: okteto/dev:latest
#     command: bash
#     workdir: /usr/src/app
#     sync:
#       - .:/usr/src/app
#     environment:
#       - name=$USER
#     forward:
#       - 8080:80


```