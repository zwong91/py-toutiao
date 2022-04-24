from socket import socket
import socketio

JWT_SECRET = 'TPmi4aLWRbyVq8zu9v82dWYW17/z+UvRnYTt4P6fAXA'
RABBITMQ = 'amqp://admin:admin@localhost:5672'

# 创建读取rabbitmq的管理对象
mgr = socketio.KombuManager(RABBITMQ)

sio = socketio.Server(cors_allowed_origins='*',
                      async_mode='eventlet', client_manager=mgr)

app = socketio.Middleware(sio)
