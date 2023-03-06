from flask_marshmallow import Marshmallow
from ..models  import course
from app import app

ma = Marshmallow(app)

class course(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = course