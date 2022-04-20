from flask import g
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from datetime import datetime

from utils.decorators import login_required
from models.user import Relation, User
# 导入数据库会话对象db
from models import db
from cache.user import UserFollowingCache, UserCache, UserFansCache


class FollowUserResource(Resource):
    method_decorators = {'post': [login_required], 'get': [login_required]}

    def post(self):
        parser = RequestParser()
        parser.add_argument('target', required=True, location='json', type=int)
        args = parser.parse_args()
        author_id = args.target
        update_time = datetime.now()

        # 用户关注作者
        rl = Relation.query.filter(
            Relation.user_id == g.userid,
            Relation.author_id == author_id,
        ).first()

        # 添加关注记录
        if rl:
            # 记录存在
            if rl.relation == Relation.RELATION.FOLLOW:
                # 如果有关注记录，直接返回结果
                return {'target': author_id}
            rl.relation = Relation.RELATION.FOLLOW
            rl.update_time = update_time
        else:
            rl = Relation(
                user_id=g.userid,
                author_id=author_id,
                relation=Relation.RELATION.FOLLOW
            )
            db.session.add(rl)

        # 修改用户的关注数量
        User.query.filter_by(id=g.userid).update(
            {'following_count': User.following_count + 1})

        # 修改作者的粉丝数量
        User.query.filter(User.id == author_id).update(
            {'fans_count': User.fans_count + 1})

        # 提交事务
        db.session.commit()

        # 更新缓存
        # 清除用户对象数据
        UserCache(g.userid).clear()
        # 清除作者对象数据
        UserCache(author_id).clear()
        # 更新用户关注列表缓存, 关注
        UserFollowingCache(g.userid).update(
            author_id, update_time.timestamp(), is_follow=True)
        # 更新作者粉丝列表缓存
        UserFansCache(author_id).update(
            g.userid, update_time.timestamp(), is_follow=True)

        # TODO： 发送关注通知, 往rabbitmq中写入数据
        # current_app.sio_mgr.emit('follow notify', data=_data, room=str(target))
        return {'target': author_id}, 201

    def get(self):
        # 获取参数
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=10, location='args')
        args = parser.parse_args()
        page = args.page
        per_page = args.per_page

        # g.userid
        # 连接查询: flask-sqlalchemy
        # select * from user_basic as ub join user_relation as ur on ub.id=ur.author_id
        # where ur.user_id=8 order by ur.update_time desc limit 10;

        # 关注列表(用户数据name)
        author_ids = UserFollowingCache(g.userid).get(page, per_page)

        # 粉丝列表(只要id)
        # fans = Relation.query.filter(
        #     Relation.author_id==g.userid,
        #     Relation.relation == Relation.RELATION.FOLLOW
        # ).all()
        # 创建用户粉丝列表对象
        fans_obj = UserFansCache(g.userid)
        ret = fans_obj.get(1, 10)
        print(ret)

        results = []
        for author_id in author_ids:
            author = UserCache(author_id).get()
            author_dict = {
                'id': author_id,
                'name': author['name'],
                'photo': author['photo'],
                'fans_count': author['fans_count'],
                # 互相关注
                'mutual_follow': True if UserFansCache(g.userid).has_fans(author_id) else False,
            }

            results.append(author_dict)

        user = UserCache(g.userid).get()

        return {
            'results': results,
            'total_count': user['follow_count'],
            'page': page,
            'per_page': per_page
        }


class UnFollowUserResource(Resource):
    method_decorators = {'delete': [login_required]}

    def delete(self, target):
        update_time = datetime.now()
        # 取消关注
        rl = Relation.query.filter(
            Relation.user_id == g.userid,
            Relation.author_id == target,
        ).first()
        if rl.relation == Relation.RELATION.FOLLOW:
            # 修改记录
            rl.relation = Relation.RELATION.DELETE
            rl.update_time = update_time

            # 修改作者的粉丝数量
            User.query.filter(
                User.id == target
            ).update({'fans_count': User.fans_count - 1})

            # 修改用户关注数量
            User.query.filter_by(id=g.userid).update(
                {'following_count': User.following_count - 1})

            # 提交事务
            db.session.commit()

            # 更新缓存
            # 清除用户对象数据
            UserCache(g.userid).clear()
            # 清除作者对象数据
            UserCache(target).clear()
            # 更新用户关注列表缓存, 取消关注
            UserFollowingCache(g.userid).update(
                target, update_time.timestamp(), is_follow=False)
            # 更新作者粉丝列表缓存
            UserFansCache(target).update(
                g.userid, update_time.timestamp(), is_follow=False)

        return {}, 204
