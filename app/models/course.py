from app import db
from sqlalchemy_utils import UUIDType
import uuid

class Course(db.Model):
    id=db.Column(UUIDType(binary=False),primary_key=True,default=uuid.uuid4)
    code=db.Column(db.String(64),index=True,unique=True)
    title=db.Column(db.String(64),unique=True)
    age_group=db.Column(db.String(64))
    creaets=db.Column(db.DateTime)
    updatets=db.Column(db.DateTime)