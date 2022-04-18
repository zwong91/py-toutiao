from api.api_app import ApiApp
from tools.get_log import GetLog
from tools.tools import Tool
import api

log = GetLog.get_logger()


class TestApp:
    # 初始化
    def setup_class(self):
        # 获取ApiApp对象
        self.app = ApiApp()

    # 登录接口 测试
    def test01_app_login(self, mobile=api.mobile, code=api.code):
        # 1. 调用登录接口
        r = self.app.api_app_login(mobile, code)
        try:
            # 2. 提取token
            Tool.common_token(r)
            # 3. 断言
            Tool.common_assert(r)
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise

    # 查询接口 测试
    def test02_app_article(self):
        # 调用查询接口
        r = self.app.api_app_article()
        try:
            # 断言
            Tool.common_assert(r, status_code=200)
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise
