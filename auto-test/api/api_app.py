import requests
import time

import api
from tools.get_log import GetLog

log = GetLog.get_logger()


class ApiApp:
    # 1. 初始化
    def __init__(self):
        # 登录url
        self.url_login = api.HOST + "/app/v1_0/authorizations"
        log.info("正在初始化app登录url：{}".format(self.url_login))
        # 查询文章url
        self.url_article = api.HOST + "/app/v1_1/articles"
        log.info("正在初始化app查询文章url：{}".format(self.url_article))

        # 2. 登录接口封装

    def api_app_login(self, mobile, code):
        # 请求参数
        data = {"mobile": mobile, "code": code}
        log.info("正在调用app登录接口，请求数据：{} 请求信息头：{}".format(data, api.headers))
        # 调用post方法
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 3. 查询文章接口封装
    def api_app_article(self):
        # 请求参数
        data = {"channel_id": api.channel_id, "timestamp": int(time.time()), "with_top": 0}  # 1:包含置顶 0：不包含置顶
        log.info("正在调用app查询文章接口，请求数据：{} 请求信息头：{}".format(data, api.headers))
        # 调用get方法
        return requests.get(url=self.url_article, params=data, headers=api.headers)
