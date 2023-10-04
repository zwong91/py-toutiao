- docker 搭建 MySQL 主从 bin-log

1. 创建配置文件

```sh
mkdir -p msql-master/conf
mkdir -p msql-master/log
mkdir -p msql-master/data

mkdir -p msql-slave/conf
mkdir -p msql-slave/log
mkdir -p msql-slave/data
```

2. 启动容器

```sh
docker-compose up -d

docker network inspect mysql_conf_mynet
# "Name": "mysql-master", "IPv4Address": "172.19.0.3/16",

docker ps
docker stop $(docker ps -a -q)

docker inspect -f='{{.Name}} {{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}} {{.HostConfig.PortBindings}}' $(docker ps -aq)
```

3. 部署容器

```sh
# 进入master容器
docker exec -it mysql-master bash
mysql -uroot -p123456
#查看server_id是否生效
mysql> show variables like '%server_id%';
#看master信息 File 和 Position 从服务上要用
mysql> show master status;
#分配权限
mysql> grant replication slave,replication client on *.* to 'slave'@'%' identified by "123456";
mysql> flush privileges;

# 进入slave容器
docker exec -it mysql-slave bash
mysql -uroot -p123456
#查看server_id是否生效
mysql> show variables like '%server_id%';

# 连接主mysql服务 master_log_file 和 master_log_pos的值要填写主master里查出来的值
mysql> change master to master_host='172.19.0.3',master_user='slave',master_password='123456',master_port=3306,master_log_file='mysql-bin.000003', master_log_pos=25912,master_connect_retry=30;

Query OK, 0 rows affected, 2 warnings (0.04 sec)

#启动slave
mysql> start slave;
mysql> show slave status \G;
        Relay_Master_Log_File: mysql-bin.000003
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes

#设置从服务器slave为只读模式
mysql> SHOW VARIABLES LIKE '%read_only%';  #查看只读状态
mysql> SET GLOBAL super_read_only=1;       #super权限的用户只读状态 1.只读 0：可写
mysql> SET GLOBAL read_only=1;             #普通权限用户读状态 1.只读 0：可写

#测试
stop slave;
start slave;
show slave status\G;

chown -R mysql:mysql /var/lib/mysql
create database toutiao
source /home/wang/py-toutiao/backend-service/common/models/init.sql
```

4. Q & A
   在主服务器上最重要的二进制日志设置是 sync_binlog，这使得 mysql 在每次提交事务的时候把二进制日志的内容同步到磁盘上，即使服务器崩溃也会把事件写入日志中。
   sync_binlog 这个参数是对于 MySQL 系统来说是至关重要的，他不仅影响到 Binlog 对 MySQL 所带来的性能损耗，而且还影响到 MySQL 中数据的完整性。对于`"sync_binlog"`参数的各种设置的说明如下：
   sync_binlog=0，当事务提交之后，MySQL 不做 fsync 之类的磁盘同步指令刷新 binlog_cache 中的信息到磁盘，而让 Filesystem 自行决定什么时候来做同步，或者 cache 满了之后才同步到磁盘。
   sync_binlog=n，当每进行 n 次事务提交之后，MySQL 将进行一次 fsync 之类的磁盘同步指令来将 binlog_cache 中的数据强制写入磁盘。

   在 MySQL 中系统默认的设置是 sync_binlog=0，也就是不做任何强制性的磁盘刷新指令，这时候的性能是最好的，但是风险也是最大的。因为一旦系统 Crash，在 binlog_cache 中的所有 binlog 信息都会被丢失。而当设置为“1”的时候，是最安全但是性能损耗最大的设置。因为当设置为 1 的时候，即使系统 Crash，也最多丢失 binlog_cache 中未完成的一个事务，对实际数据没有任何实质性影响。

   从以往经验和相关测试来看，对于高并发事务的系统来说，"sync_binlog"设置为 0 和设置为 1 的系统写入性能差距可能高达 5 倍甚至更多。

   MyIsam 快速插入查询，InnoDB 事务 ACID
   读写分离对事务的影响
   对于写操作包括开启事务和提交或回滚是要在一台机器上执行, 分散到多台 master 执行后数据库原生的单机事务失效了。
   对于事务中同时包含读写操作, 与事务的隔离级别设置有关，如果事务隔离级别为 read-uncommitted 或 read-committed，读写分离无影响;
   如果事务隔离级别为 repeateable-read, serializeable 读写分离有影响, 在 slave 上会看到新数据， 而正在进行事务中的 master 看不到新数据。
