from sqlalchemy_utils import UUIDType
from flask_marshmallow import Marshmallow

from app import db
from app import app
from .Audit import AuditModel
import uuid

class CourseModel(db.Model, AuditModel):
    __tablename__ = 'courses'
    id=db.Column(UUIDType(binary=False),primary_key=True,default=uuid.uuid4)
    code=db.Column(db.String(64),index=True,unique=True)
    title=db.Column(db.String(64),unique=True)
    min_age=db.Column(db.Integer)
    max_age=db.Column(db.Integer)

ma = Marshmallow(app)

class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CourseModel