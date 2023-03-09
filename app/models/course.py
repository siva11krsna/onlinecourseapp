from sqlalchemy_utils import UUIDType
from flask_marshmallow import Marshmallow
import datetime

from app import db
from app import app
import uuid

class CourseModel(db.Model):
    __tablename__ = 'courses'
    id=db.Column(UUIDType(binary=False),primary_key=True,default=uuid.uuid4)
    code=db.Column(db.String(64),index=True,unique=True)
    title=db.Column(db.String(64),unique=True)
    age_group=db.Column(db.String(64))
    createts=db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updatets=db.Column(db.DateTime, default=datetime.datetime.utcnow)

ma = Marshmallow(app)

class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CourseModel