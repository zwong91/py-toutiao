class DefaultConfig(object):
    """
    Flask默认配置

    """
    ERROR_404_HELP = False

    # 日志
    LOGGING_LEVEL = 'DEBUG'
    LOGGING_FILE_DIR = '/opt/toutiao/logs'
    LOGGING_FILE_MAX_BYTES = 500 * 1024 * 1024 # 500M
    LOGGING_FILE_BACKUP = 10

    # flask-sqlalchemy使用的参数, 读写分离配置
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:pwd@127.0.0.1/toutiao'  # 数据库
    SQLALCHEMY_BINDS = {
        'sz-m1': 'mysql://root:123456@127.0.0.1:13306/toutiao',
        'sz-s1': 'mysql://root:123456@127.0.0.1:13307/toutiao',
        # 'masters': 'sz-m1',
        # 'slaves':  'sz-s1',
        # 'default': 'sz-m1'
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 追踪数据的修改信号
    SQLALCHEMY_ECHO = True

    # redis 3哨兵
    REDIS_SENTINELS = [
        ('172.17.0.4', '26379'), # master
        ('172.17.0.2', '26380'), # slave1
        ('172.17.0.3', '26381'), # slave2
    ]
    REDIS_SENTINEL_SERVICE_NAME = 'local-master'

    # redis 3主3从 集群
    REDIS_CLUSTER = [
        {'host': '127.0.0.1', 'port': 7001},
        {'host': '127.0.0.1', 'port': 7002},
        {'host': '127.0.0.1', 'port': 7003},
    ]

    # 限流服务redis
    # RATELIMIT_STORAGE_URL = 'redis://127.0.0.1:6379/15'
    RATELIMIT_STORAGE_URL = f'redis+sentinel://127.0.0.1:26379,127.0.0.1:26380,127.0.0.1:26381/{REDIS_SENTINEL_SERVICE_NAME}'
    RATELIMIT_STRATEGY = 'moving-window'
    # RATELIMIT_DEFAULT = ['200/hour;1000/day']

    # JWT
    JWT_SECRET = 'TPmi4aLWRbyVq8zu9v82dWYW17/z+UvRnYTt4P6fAXA'
    JWT_EXPIRY_HOURS = 2
    JWT_REFRESH_DAYS = 14

    # rpc
    RPC_RECOMMEND = '172.17.0.134:19999'
    ##RPC_CHATBOT = '172.17.0.59:20000'

    # ES
    ES = [
        'http://172.22.0.2:9200'
    ]

    # 七牛OSS对象存储
    QINIU_ACCESS_KEY = 'SmdtGrstU8mkcHcfLIpY-C_lHIa8brda55Qz4j30'
    QINIU_SECRET_KEY = 'JWpOm6_E7cSgl_akYOVCSuiOs6JlqElRIaxx_JO7'
    QINIU_BUCKET_NAME = 'tbd45'
    QINIU_DOMAIN = 'http://pzm8w0o88.bkt.clouddn.com/'

    # 消息队列
    RABBITMQ = 'amqp://python:rabbitmqpwd@localhost:5672/toutiao'

    # <TODO> CORS调试后要修改
    CORS_ORIGINS = '*'

    # Snowflake ID Worker 参数
    DATACENTER_ID = 0
    WORKER_ID = 0
    SEQUENCE = 0


class CeleryConfig(object):
    """
    Celery默认配置
    broker_url: 指定消息队列的位置, toutiao为virtualhost, 添加一个然后放开权限
    result_backend: 默认值
    task_routes: 指定队列名称为sms, direct routingkeys
    """
    broker_url = 'amqp://admin:123456@localhost:5672/toutiao'

    task_routes = {
        'sms.*': {'queue': 'sms'},
    }

    #broker_connection_retry = True
    broker_connection_retry_on_startup = True
    # 阿里大鱼短信服务
    DYSMS_ACCESS_KEY_ID = ''
    DYSMS_ACCESS_KEY_SECRET = ''


class MisDefaultConfig(DefaultConfig):
    GEETEST_ID = ''
    GEETEST_KEY = ''
    SECRET_KEY = ''
    DEBUG = False
    IS_INIT = False
