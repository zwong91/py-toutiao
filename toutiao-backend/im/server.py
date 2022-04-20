from socket import socket
import socketio

JWT_SECRET = 'TPmi4aLWRbyVq8zu9v82dWYW17/z+UvRnYTt4P6fAXA'
#RABBITMQ = 'amqp://python:rabbitmqpwd@localhost:5672/toutiao'

# 创建读取rabbitmq的管理对象
#mgr = socketio.KombuManager(RABBITMQ)

# sio = socketio.Server(cors_allowed_origins='*',
#                       async_mode='eventlet', client_manager=mgr)
sio = socketio.Server(cors_allowed_origins='*',
                      async_mode='eventlet')
app = socketio.Middleware(sio)
