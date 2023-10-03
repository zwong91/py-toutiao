# 说明

- backend-service 业务后端服务, 接口 api
- chat-service 聊天机器人, NLP 处理
- reco-service 推荐系统服务, 用户画像, 数据分析 bigdata hadoop/hdfs/map-reduce/flink/hbase

## 启动设置

### 开发模式

**_Guido van Rossumm_**
伟大的程序员必备三个优点：懒惰、暴躁和自负。

````shell
python虚拟环境安装
pip3 install virtualenv virtualenvwrapper
sudo apt install --reinstall virtualenv
# ~/.bashrc 添加如下:
```sh
# virtualenvwrapper存放虚拟环境目录
export WORKON_HOME="/opt/toutiao/.virtualenvs"
export PROJECT_HOME=$HOME/py-toutiao
export VIRTUALENVWRAPPER_PYTHON="/usr/bin/python3"
# bin/virtualenvwrapper.sh
source /opt/toutiao/.local/bin/virtualenvwrapper.sh
````

lsvirtualenv
mkvirtualenv toutiao -p python3
rmvirtualenv toutiao
workon toutiao
deactivate

pip list
pip install django==
pip install -r requirements.txt

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

### docker-compose 管理所有实例服务

- docker 部署 redis-cluster 集群

* docker-compose 三主三从
* docker run 一主二从三哨兵

- docker 搭建 MySQL 主从 bin-log

- docker 搭建 RabbitMQ

- docker 搭建 ES + Kibana

- 生成 pb 文件 **_使用相对路径, 在上层路径下执行_**
  python3 -m grpc*tools.protoc --python_out=. --grpc_python_out=. -I. protos/*.proto
  python3 -m grpc*tools.protoc --python_out=. --grpc_python_out=. -I. rpc/*.proto
  python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. recommend/\*.proto

```

+ 常用工具
socket.io  Firecamp 浏览器插件
Excalidraw 在线白板工具
gunicorn 21 线上部署运行服务器

supervisor 4.2.5  fork/exec***前端***进程子进程守护工具，自动添加到systemd, 用Systemd管Supervisord
```

vim /usr/lib/systemd/system/supervisor.service

# systemctl daemon-reload

# systemctl start supervisor.service

# systemctl status supervisor.service

# systemctl enable supervisor.service

```

```
