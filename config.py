# -*- coding: utf-8 -*-
# @Date    : 16-9-8
# @Author  : Ezi
# @Email   : Ezi4zy@163.com
# @File    : config.py


class Config(object):
    pass


class ProductConfig(object):
    pass


class DevelopConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev-database.db"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
