# 说明

## 启动设置

### 开发模式

```shell

# 生成pb文件
python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. *.proto

export FLASK_ENV=development
export TOUTIAO_WEB_SETTINGS=/path/to/config/file
```

### 线上模式

```shell
export FLASK_ENV=production
export TOUTIAO_WEB_SETTINGS=/path/to/config/file
export TOUTIAO_CELERY_SETTINGS=/path/to/config/file
```
