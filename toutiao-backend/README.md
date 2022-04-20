# 说明

## 启动设置

### 开发模式

```shell

export FLASK_ENV=development
export TOUTIAO_WEB_SETTINGS=/path/to/config/file
```

### 线上模式

```shell
export FLASK_ENV=production
export TOUTIAO_WEB_SETTINGS=/path/to/config/file
export TOUTIAO_CELERY_SETTINGS=/path/to/config/file
```

***Guido van Rossumm***

```shell
python虚拟环境安装

伟大的程序员必备三个优点：懒惰、暴躁和自负。

pip install virtualenv
pip install virtualenvwrapper

#写入~/.bashrc
#virtualenvwrapper存放虚拟环境目录
export WORKON_HOME="~/.virtualenvs"
export VIRTUALENVWRAPPER_PYTHON="/usr/bin/python3"
#bin/virtualenvwrapper.sh
source $HOME/.local/bin/virtualenvwrapper.sh

mkvirtualenv toutiao  -p  python3
pip  install  flask
pip list

workon
deactivate

rmvirtualenv toutiao

pip install -r  requirements.txt 

docker搭建redis一主二从三哨兵
https://blog.csdn.net/weixin_41672684/article/details/122411917?share_token=336d7a4d-61c3-4e8f-9cce-0d735f1d6ad0
https://blog.csdn.net/qq_33067315/article/details/114995533

#启动redis-master, 同时启动redis-server
docker run  -d -p 6379:6379 -p 26379:26379  --restart always  -v ~/redis/redis_conf/redis-master.conf:/data/redis.conf -v ~/redis/redis_conf/sentinel.conf:/data/sentinel.conf --name redis-master redis:latest  redis-server redis.conf
#启动redis-slave-1容器 同时启动redis-server
docker run -d -p 6380:6380 -p 26380:26380 -v ~/redis/redis_conf/redis-slave-1.conf:/data/redis.conf -v ~/redis/redis_conf/sentinel2.conf:/data/sentinel.conf --name redis-slave-1 redis:latest redis-server redis.conf
#单独启动redis-slave-2容器 同时启动redis-server
docker run -d -p 6381:6381 -p 26381:26381 -v ~/redis/redis_conf/redis-slave-2.conf:/data/redis.conf -v ~/redis/redis_conf/sentinel3.conf:/data/sentinel.conf --name redis-slave-2 redis:latest redis-server redis.conf

docker exec -it redis-master bash
docker inspect --format='{{.NetworkSettings.IPAddress}}'  redis-master
docker logs -f -t --tail 100 redis-master

docker搭建MySQL主从  bin-log
https://www.cnblogs.com/nijunyang/p/14990169.html

docker 搭建RabbitMQ
docker pull rabbitmq:management
docker run -p 15672:15672  -p  5672:5672 -d --hostname dnmp-rabbitmq --name dnmp-rabbitmq -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=admin rabbitmq:management

docker 搭建ES
https://blog.csdn.net/qq_40942490/article/details/111594267

socket.io  Firecamp ws调试工具 浏览器插件
Axsure  RP  浏览器插件

# 生成pb文件
python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. *.proto


```