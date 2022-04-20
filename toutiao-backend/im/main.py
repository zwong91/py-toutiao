import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'common'))

import eventlet
from server import app
import eventlet.wsgi
#import chat
import notify
eventlet.monkey_patch()

# 创建socketIO服务器
# 步骤：
# 1、使用eventlet异步库
# 2、创建socketIO对象，指定异步的方式执行，用来接收事件，返回消息
# 3、创建服务器对象
# 4、绑定主机和端口
addr = ('', 8000)
sock = eventlet.listen(addr)
# 5、启动服务器
eventlet.wsgi.server(sock, app)
