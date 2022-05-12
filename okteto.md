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