#encoding=utf-8
import os

from messageBoard import app

dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')  #sqlite绝对路径格式

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 不追踪对象的修改
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)



