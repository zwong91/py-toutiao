import unittest
import json

from sqlalchemy import union

from toutiao import create_app
from settings.testing import TestingConfig

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR))
sys.path.insert(0, os.path.join(BASE_DIR, 'common'))


class SuggestionTestCase(unittest.TestCase):
    """
    用于测试搜索建议接口的用例
    """

    def setUp(self) -> None:
        """
        在其他测试方法之前被执行
        :return:
        """
        flask_app = create_app(TestingConfig)
        self.test_client = flask_app.test_client()

    def test_normal_request(self):
        """
        测试接口正常请求的场景
        """
        # 构造一个http的请求
        # 使用框架程序提供的单元测试客户端(flask_app.test_client), 请求/v1_0/suggestion
        resp = self.test_client.get('/v1_0/suggestion?q=python%20web')
        # 接收视图处理的响应消息
        # 判断响应消息的数据是否符合预期
        # 添加一个预期断言, 如果视图结果符合预期, 收到的状态码为200
        self.assertEqual(resp.status_code, 200)  # 响应状态码
        resp_json = resp.data
        resp_dict = json.loads(resp_json)

        self.assertIn('message', resp_dict)
        self.assertIn('data', resp_dict)
        data = resp_dict['data']
        self.assertIn('options', data)

    def test_missing_request_param_q(self):
        """"
        测试接口请求时缺少参数q的场景
        :return:
        """
        resp = self.test_client.get('/v1_0/suggestion')
        self.assertEqual(resp.status_code, 400)  # 响应状态码

    def test_request_param_q_length_error(self):
        """
        测试接口请求时q参数超过长度限制
        """
        resp = self.test_client.get('/v1_0/suggestion?q='+'e'*51)
        self.assertEqual(resp.status_code, 400)  # 响应状态码


if __name__ == '__main__':
    unittest.main()
