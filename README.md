# 说明

## 启动设置

### 开发模式
***Guido van Rossumm***
伟大的程序员必备三个优点：懒惰、暴躁和自负。
```shell
python虚拟环境安装
pip install virtualenv
pip install virtualenvwrapper
sudo apt install --reinstall virtualenv
# ~/.bashrc 添加如下:
#virtualenvwrapper存放虚拟环境目录
export WORKON_HOME="~/.virtualenvs"
export PROJECT_HOME=$HOME/py-toutiao
export VIRTUALENVWRAPPER_PYTHON="/usr/bin/python3"

#bin/virtualenvwrapper.sh
source $HOME/.local/bin/virtualenvwrapper.sh

lsvirtualenv
mkvirtualenv toutiao  -p python3
rmvirtualenv toutiao
workon toutiao
deactivate

pip list
pip install -r  requirements.txt 


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

+ docker 部署redis-cluster 集群
https://www.cnblogs.com/chenchuxin/p/8404699.html
docker搭建redis一主二从三哨兵
https://blog.csdn.net/weixin_41672684/article/details/122411917?share_token=336d7a4d-61c3-4e8f-9cce-0d735f1d6ad0
https://blog.csdn.net/qq_33067315/article/details/114995533

1. 启动redis-master容器, 同时启动redis-server
docker run  -d -p 6379:6379 -p 26379:26379  --restart always  -v ~/redis/redis_conf/redis-master.conf:/data/redis.conf -v ~/redis/redis_conf/sentinel.conf:/data/sentinel.conf --name redis-master redis:latest  redis-server redis.conf
2. 启动redis-slave-1容器 同时启动redis-server
docker run -d -p 6380:6380 -p 26380:26380 -v ~/redis/redis_conf/redis-slave-1.conf:/data/redis.conf -v ~/redis/redis_conf/sentinel2.conf:/data/sentinel.conf --name redis-slave-1 redis:latest redis-server redis.conf
3. 单独启动redis-slave-2容器 同时启动redis-server
docker run -d -p 6381:6381 -p 26381:26381 -v ~/redis/redis_conf/redis-slave-2.conf:/data/redis.conf -v ~/redis/redis_conf/sentinel3.conf:/data/sentinel.conf --name redis-slave-2 redis:latest redis-server redis.conf

docker exec -it redis-master bash
docker inspect --format='{{.NetworkSettings.IPAddress}}'  redis-master
docker logs -f -t --tail 100 redis-master
redis事务+watch命令 乐观锁，  redis cluster不支持事务，不支持多键操作如mset
failover  自动故障转移
6台redis,  cluster
官方多副本冗余和分布式分片方案 slot槽位16384

+ docker搭建MySQL主从  bin-log
https://www.cnblogs.com/nijunyang/p/14990169.html

MyIsam  插入查询， InnoDB事务ACID
读写分离对事务的影响
对于写操作包括开启事务和提交或回滚是要在一台机器上执行, 分散到多台master执行后数据库原生的单机事务失效了。
对于事务中同时包含读写操作, 与事务的隔离级别设置有关，如果事务隔离级别为read-uncommitted或read-committed，读写分离无影响;
如果事务隔离级别为repeateable-read, serializeable 读写分离有影响, 在slave上会看到新数据， 而正在进行事务中的master看不到新数据。


+ docker 搭建RabbitMQ
docker pull rabbitmq:management
docker run -p 15672:15672  -p  5672:5672 -d --hostname dnmp-rabbitmq --name dnmp-rabbitmq -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=admin rabbitmq:management

+ docker 搭建ES
https://blog.csdn.net/qq_40942490/article/details/111594267

+ 常用工具
socket.io  Firecamp ws调试工具 浏览器插件
Axsure  RP  浏览器插件
gunicorn 线上部署运行服务器
supervisor 进程守护工具

+ 生成pb文件  ***使用相对路径, 在上层路径下执行***
python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I.  protos/*.proto
python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I.  rpc/*.proto
python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I.  recommend/*.proto
```