import os

class Config(object):

    SQLALCHEMY_DATABASE_URI = "postgresql:///ptest"
    SQLALCHEMY_TRACK_MODIFICATIONS = False