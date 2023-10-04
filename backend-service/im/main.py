# notify模块 必须在前面, chat 模块在后, 先加入房间分组, 然后再指定分组发消息
import notify
import chat

from server import app
import eventlet.wsgi
import socketio
import sys
import os
import eventlet
# 将所有用到的系统标准io函数替换成eventlet提供的同名函数，方便eventlet可以自动切换协程
eventlet.monkey_patch()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'common'))


# 通过sys模块 获取启动命令中的参数  sys.argv
# # python main.py 8001 ...
# sys.argv -> ['main.py', '8001', ...]
if len(sys.argv) < 2:
    # 表示启动时缺少端口号参数
    print('Usage: python main.py [port]')
    exit(1)  # 表示程序异常退出


port = int(sys.argv[1])

# 通过导入事件处理模块的方法，让主程序知道事件处理方法的存在

# 创建协程服务并启动
# python server.py [port]
SERVER_ADDRESS = ('', port)
sock = eventlet.listen(SERVER_ADDRESS)
eventlet.wsgi.server(sock, app)
