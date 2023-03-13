from app import db
import datetime

class AuditModel:
    createts=db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updatets=db.Column(db.DateTime, default=datetime.datetime.utcnow)