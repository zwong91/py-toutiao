from requests import request
from setuptools import Require
from server import sio, JWT_SECRET
from werkzeug.wrappers import Request
from utils.jwt_util import verify_jwt


def verify_jwt_token(token):
    payload = verify_jwt(token, JWT_SECRET)
    if payload is None:
        return None
    else:
        return payload.get('user_id')


@sio.on('connect')
def on_connect_notify(sid, environ):
    """
    当客户端连接时被执行
    :param sid:
    :param environ: dict 解析客户端握手时的HTTP数据
    :return:
    """
    # 辅助werkzeug提供的Request类, 讲environ dict 转换为request对象
    request = Request(environ)

    # 查询字符串中的取出 jwt token
    token = request.args.get('token')
    print(token)
    # 验证jwt token, 有效取出user_id, 将用户添加到`user_id`的房间
    user_id = verify_jwt_token(token)
    if user_id is not None:
        sio.enter_room(sid, str(user_id))


@sio.on('disconnect')
def on_disconnect(sid):
    rooms = sio.rooms(sid)
    for room in rooms:
        sio.leave_room(sid, room)
