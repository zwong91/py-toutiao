import socketio

sio = socketio.Server(async_mode='eventlet', cors_allowed_origins='*')
app = socketio.Middleware(sio)
