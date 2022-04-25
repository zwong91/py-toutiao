class DefaultConfig(object):
    """
    Flask默认配置

    """
    ERROR_404_HELP = False

    # 日志
    LOGGING_LEVEL = 'DEBUG'
    LOGGING_FILE_DIR = './logs'
    LOGGING_FILE_MAX_BYTES = 300 * 1024 * 1024
    LOGGING_FILE_BACKUP = 10

    # flask-sqlalchemy使用的参数
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:pwd@127.0.0.1/toutiao'  # 数据库
    SQLALCHEMY_BINDS = {
        'sz-m1': 'mysql://root:root@127.0.0.1:3306/toutiao',
        'sz-s1': 'mysql://root:root@127.0.0.1:3307/toutiao',
        'masters': ['sz-m1'],
        'slaves': ['sz-s1'],
        'default': 'sz-m1'
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 追踪数据的修改信号
    SQLALCHEMY_ECHO = True

    # redis 哨兵
    REDIS_SENTINELS = [
        ('172.17.0.4', '26379'),
        ('172.17.0.5', '26381'),
        ('172.17.0.6', '26380'),
    ]
    REDIS_SENTINEL_SERVICE_NAME = 'mymaster'

    # redis 集群
    REDIS_CLUSTER = [
        {'host': '127.0.0.1', 'port': '7000'},
        {'host': '127.0.0.1', 'port': '7001'},
        {'host': '127.0.0.1', 'port': '7002'},
    ]

    # 限流服务redis
    # RATELIMIT_STORAGE_URL = 'redis://127.0.0.1:6379/0'
    RATELIMIT_STORAGE_URL = 'redis+sentinel://127.0.0.1:26379,127.0.0.1:26380,127.0.0.1:26381/mymaster'
    RATELIMIT_STRATEGY = 'moving-window'
    # RATELIMIT_DEFAULT = ['200/hour;1000/day']

    # JWT
    JWT_SECRET = 'TPmi4aLWRbyVq8zu9v82dWYW17/z+UvRnYTt4P6fAXA'
    JWT_EXPIRY_HOURS = 2
    JWT_REFRESH_DAYS = 14

    # rpc
    class RPC:
        RECOMMEND = '172.17.0.134:9999'
        CHATBOT = '172.17.0.59:9999'

    # ES
    ES = [
        'http://127.0.0.1:9200'
    ]

    QINIU_ACCESS_KEY = 'SmdtGrstU8mkcHcfLIpY-C_lHIa8brda55Qz4j30'
    QINIU_SECRET_KEY = 'JWpOm6_E7cSgl_akYOVCSuiOs6JlqElRIaxx_JO7'
    QINIU_BUCKET_NAME = 'tbd45'
    QINIU_DOMAIN = 'http://pzm8w0o88.bkt.clouddn.com/'

    RABBITMQ = 'amqp://python:rabbitmqpwd@localhost:5672/toutiao'

    GEETEST_ID = ''
    GEETEST_KEY = ''

    # CORS
    # TODO 调试后要修改
    CORS_ORIGINS = '*'

    # Snowflake ID Worker 参数
    DATACENTER_ID = 0
    WORKER_ID = 0
    SEQUENCE = 0


class CeleryConfig(object):
    """
    Celery默认配置
    """
    broker_url = 'amqp://python:rabbitmqpwd@localhost:5672/toutiao'

    task_routes = {
        'sms.*': {'queue': 'sms'},
    }

    # 阿里短信服务
    DYSMS_ACCESS_KEY_ID = ''
    DYSMS_ACCESS_KEY_SECRET = ''


class MisDefaultConfig(DefaultConfig):
    # LOGGING_FILE_DIR = '/data/log'
    GEETEST_ID = ''
    GEETEST_KEY = ''
    SECRET_KEY = ''
    DEBUG = False
    IS_INIT = False
