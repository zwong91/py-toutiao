from flask import g
from flask_restful.inputs import natural, regex
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from utils.decorators import login_required
from models.article import Comment, Article
from models.user import User
# 导入数据库会话对象db
from models import db


class CommentsResource(Resource):
    method_decorators = {'post': [login_required]}

    def post(self):
        # 获取参数
        parser = RequestParser()
        parser.add_argument('target', type=int, required=True, location='json')
        parser.add_argument('content', required=True, location='json')
        parser.add_argument('parent_id', default=0,
                            type=natural, location='json')
        args = parser.parse_args()
        target = args.target   # 文章id
        content = args.content  # 评论内容
        parent_id = args.parent_id if args.parent_id is not None else 0  # 父评论id 0表示的是一级评论

        # 发布评论数据(评论-回复)
        comment = Comment(
            user_id=g.userid,
            article_id=target,
            parent_id=parent_id,
            content=content
        )
        db.session.add(comment)

        if parent_id > 0:
            # 评论的回复数加1
            Comment.query.filter(Comment.id == parent_id).update(
                {'reply_count': Comment.reply_count + 1})
        else:
            # 文章的评论数加1
            Article.query.filter_by(id=target).update(
                {'comment_count': Article.comment_count + 1})

        # 提交事务
        db.session.commit()

        # 返回结果
        return {'com_id': comment.id, 'target': target, 'parent_id': parent_id}, 201

    def get(self):
        # 获取参数
        parser = RequestParser()
        parser.add_argument('source', type=int, required=True, location='args')
        parser.add_argument('offset', type=int, default=0, location='args')
        parser.add_argument('limit', type=int, default=10, location='args')
        parser.add_argument('type', required=True,
                            location='args', type=regex(r'[ac]'))
        args = parser.parse_args()

        type = args.type  # 如果type = a，source就表示文章id type=c, source表示评论的id
        source = args.source  # 文章id
        offset = args.offset  # 上一页最大的评论的id
        limit = args.limit    # 每页返回的数量

        if type == 'a':
            # 查询评论列表
            # 过滤条件 文章id = source & 评论id>offset & parent_id == 0
            data = db.session.query(
                Comment.id, Comment.user_id, Comment.ctime,
                Comment.content, Comment.reply_count, Comment.like_count,
                User.name, User.profile_photo
            ).join(User, User.id == Comment.user_id).filter(
                Comment.article_id == source,
                Comment.id > offset,
                Comment.parent_id == 0
            ).order_by(Comment.id.asc()).limit(limit).all()

            # 评论的总数量
            total_count = Comment.query.filter(
                Comment.article_id == source, Comment.parent_id == 0).count()

            # 最后一条评论的id, 前端用于判断是否剩余评论, 无值返回None
            end_comment = Comment.query.filter(
                Comment.article_id == source,
                Comment.parent_id == 0
            ).order_by(Comment.id.desc()).first()
        else:
            # 获取评论的回复数
            data = db.session.query(
                Comment.id, Comment.user_id, Comment.ctime,
                Comment.content, Comment.reply_count, Comment.like_count,
                User.name, User.profile_photo
            ).join(User, User.id == Comment.user_id).filter(
                Comment.id > offset,
                Comment.parent_id == source  # source是评论id
            ).order_by(Comment.id.asc()).limit(limit).all()

            # 回复的总数量
            total_count = Comment.query.filter(
                Comment.parent_id == source).count()

            # 最后一条评论的id, 前端用于判断是否剩余评论, 无值返回None
            end_comment = Comment.query.filter(
                Comment.parent_id == source
            ).order_by(Comment.id.desc()).first()

        # 序列化
        comment_list = [
            {
                'com_id': i.id,
                'aut_id': i.user_id,
                'aut_name': i.name,
                'aut_photo': i.profile_photo,
                'pubdate': i.ctime.isoformat(),
                'content': i.content,
                'reply_count': i.reply_count,
                'like_count': i.like_count,
            } for i in data
        ]

        # 本次请求最后一条评论的id, 作为下次请求的offset, 无值返回None
        last_id = data[-1].id if len(data) > 0 else None

        end_id = end_comment.id if end_comment is not None else None

        return {
            'total_count': total_count,
            'last_id': last_id,
            'end_id': end_id,
            'results': comment_list,
        }
