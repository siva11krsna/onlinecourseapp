import os

class Config(object):

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost:5432/courses"
    SQLALCHEMY_TRACK_MODIFICATIONS = False