from flask import g
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from datetime import datetime

# 导入数据库会话对象db
from models import db
from models.article import Article
from models.article import ArticleContent
from models.article import Attitude
from models.article import Collection

from models.user import User
from models.user import Relation
from utils.constants import HOME_PRE_PAGE
from cache.user import UserFansCache


class ArticleListResource(Resource):
    def get(self):
        parser = RequestParser()
        parser.add_argument('channel_id', required=True,
                            type=int, location='args')
        parser.add_argument('timestamp', required=True,
                            type=int, location='args')
        args = parser.parse_args()

        # 获取参数
        channel_id = args.channel_id
        # 时间戳精确到毫秒
        timestamp = args.timestamp

        # 如果是推荐频道，先返回空数据
        if channel_id == 0:
            return {'pre_timestamp': 0, 'results': []}

        # 数据库中datetime对象的比较，不能使用时间戳，只能通过datetime对象比较
        date = datetime.fromtimestamp(timestamp * 0.001)

        # 设计到Article User两张表，所以用sqlalchemy本体的语法
        # 过滤条件: 频道id & 时间小于timestamp & 通过审核的文章
        data = db.session.query(
            Article.id, Article.title, Article.user_id,
            Article.ctime, User.name, Article.comment_count, Article.cover
        ).join(User, Article.user_id == User.id).filter(
            Article.ctime < date,
            Article.status == Article.STATUS.APPROVED,
            Article.channel_id == channel_id
        ).order_by(Article.ctime.desc()).limit(HOME_PRE_PAGE).all()

        # 序列化
        articles = [
            {
                'art_id': i.id,
                'title': i.title,
                'aut_id': i.user_id,
                'pubdate': i.ctime.isoformat(),
                'aut_name': i.name,
                'comm_count': i.comment_count,
                'cover': i.cover,
            } for i in data
        ]

        if data:
            pre_timestamp = int(data[-1].ctime.timestamp() * 1000)
        else:
            pre_timestamp = 0

        return {'pre_timestamp': pre_timestamp, 'results': articles}


class ArticleDetailResource(Resource):
    def get(self, article_id):
        # sqlalchemy 本体的做法
        data = db.session.query(
            Article.id, Article.title, Article.ctime, Article.user_id,
            User.name, User.profile_photo, ArticleContent.content
        ).join(
            User, Article.user_id == User.id
        ).join(
            ArticleContent, Article.id == ArticleContent.article_id
        ).filter(
            Article.id == article_id
        ).first()

        # 文章详情数据
        article_dict = {
            'art_id': data.id,
            'title': data.title,
            'pubdate': data.ctime.isoformat(),
            'aut_id': data.user_id,
            'aut_name': data.name,
            'aut_photo': data.profile_photo,
            'content': data.content,
            'is_followed': False,
            'attitude': -1,  # 不喜欢0 喜欢1 无态度-1
            'is_collected': False,
        }

        if g.userid:
            # 是否关注 用户是否关注了作者
            # rl = Relation.query.filter(
            #     Relation.user_id == g.userid,
            #     Relation.author_id == data.user_id,
            #     Relation.relation == Relation.RELATION.FOLLOW
            # ).first()

            article_dict['is_followed'] = True if UserFansCache(
                data.user_id).has_fans(g.userid) else False

            # 用户对文章的态度
            at = Attitude.query.filter(
                Attitude.user_id == g.userid,
                Attitude.article_id == data.id
            ).first()

            if not at:
                # 无态度
                article_dict['attitude'] = -1
            else:
                # 有记录， 脏数据at.attitude None at.attitude=0
                # 出现这种bug的原因，依赖隐含判断
                article_dict['attitude'] = at.attitude if at.attitude is not None else -1

            # 是否收藏
            cl = Collection.query.filter(
                Collection.user_id == g.userid,
                Collection.article_id == data.id,
                Collection.is_deleted == False
            ).first()

            article_dict['is_collected'] = True if cl else False

        return article_dict
