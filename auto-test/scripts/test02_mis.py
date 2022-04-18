from api.api_mis import ApiMis
from tools.get_log import GetLog
from tools.tools import Tool

log = GetLog.get_logger()


class TestMis:
    # 1. 初始化
    def setup_class(self):
        # 获取ApiMis对象
        self.mis = ApiMis()

    # 2. 登录接口测试方法
    def test01_mis_login(self, account="testid", password="testpwd123"):
        # 1. 调用登录接口
        r = self.mis.api_mis_login(account, password)
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

    # 3. 查询 接口测试方法
    def test02_mis_find(self):
        # 1. 调用查询接口
        r = self.mis.api_mis_find()
        try:
            # 2. 断言 200:为int 不能加引号
            Tool.common_assert(r, status_code=200)
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise

    # 4. 审核 接口测试方法
    def test03_mis_audit(self):
        # 1. 调用审核接口
        r = self.mis.api_mis_audit()
        try:
            # 2. 断言
            Tool.common_assert(r)
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise
