#encoding=utf-8
import unittest

from flask import abort

from messageBoard import app, db
from messageBoard.models import Message
from messageBoard.commands import forge,initdb



if __name__ == '__main__':
    app.run(debug=True)



# class MessageBoardTestCase(unittest.TestCase):
#
#     def setUp(self):
#         app.config.update(
#             TESTING=True,  #开启测试模
#             WTF_CSRF_ENABLED=Fase,  #关闭CSRF保护
#             SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
#         )
#         db.create_all()
#         self.client = app.test_client()  #创建测试客户端对象
#         self.runner = app.test_cli_runner()  #app.test_cli_runner（）方法用于在测试中调用命令函数、捕捉输出
#
#     def tearDown(self):
#         db.session.remove()
#         dv.drop_all()
#
#     def test_app_exist(self):
#         self.assertFalse(app is None)
#
#     def test_app_is_testing(self):
#         selfl.assertTrue(app.config['TESTING'])
#
#     def test_404_page(self):
#         response = self.client.get('/nothing')
#         data = response.get_data(as_text=True)
#         self.assertIn('404 Error', data)
#         self.assertIn('Go Back', data)






































