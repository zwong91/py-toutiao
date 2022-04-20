from app import db
from utils.decorators import login_required
from models.article import UserChannel, Channel
from flask import g, request
from flask_restful import Resource
from sqlalchemy.orm import load_only

from models.article import Channel


class AllChannelResource(Resource):
    def get(self):
        channels = Channel.query.options(load_only(
            Channel.id,
            Channel.name
        )).all()
        channel_list = [i.to_dict() for i in channels]
        return {'channels': channel_list}


class UserChannelResource(Resource):
    method_decorators = {'put': [login_required]}

    def get(self):
        if g.userid:
            # 获取用户的所有频道
            # 两表查询, 连接查询
            channels = Channel.query.join(UserChannel, Channel.id == UserChannel.channel_id).filter(
                UserChannel.user_id == g.userid,
                UserChannel.is_deleted == False
            ).order_by(UserChannel.sequence.asc()).all()
            if len(channels) == 0:
                # 如果用户清空了频道，就给他默认频道
                channels = Channel.query.filter(
                    Channel.is_default == True).all()
        else:
            # 没有登录，就获取默认频道
            channels = Channel.query.filter(Channel.is_default == True).all()

        channel_list = [i.to_dict() for i in channels]

        # 在最开始的地方，插入推荐频道
        channel_list.insert(0, {'id': 0, 'name': '推荐'})

        # 返回结果
        return {'channels': channel_list}

    def put(self):
        # 获取channels参数
        channels = request.json.get('channels')

        # 删除用户的所有频道
        UserChannel.query.filter(
            UserChannel.user_id == g.userid).update({'is_deleted': True})

        for channel in channels:  # channel: {"id":1, "seq": 1}
            # id 是频道id 加上条件 UserChannel.user_id == g.userid
            user_channel = UserChannel.query.filter(
                UserChannel.channel_id == channel['id'],
                UserChannel.user_id == g.userid
            ).first()
            if user_channel:
                # 如果存在，修改逻辑删和序列号
                user_channel.is_deleted = False
                user_channel.sequence = channel.get('seq')
            else:
                # 如果不存在，就创建
                user_channel = UserChannel(
                    channel_id=channel['id'],
                    sequence=channel['seq'],
                    user_id=g.userid
                )

            db.session.add(user_channel)

        # 提交事务
        db.session.commit()

        return {'channels': channels}
