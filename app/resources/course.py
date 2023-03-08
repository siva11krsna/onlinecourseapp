from flask_restx import Resource, Api, Namespace, fields
from flask import jsonify, request

from ..models.course import *

from app import app

api = Api(app)
# ns = api.namespace('courses','course list')

coursemodel = CourseModel()
coursesschema = CourseSchema(many=True)
@api.route('/courses')
class Course(Resource):
    def get(self):
        print('get courses hit..')
        courses = coursemodel.query.all()
        return jsonify(coursesschema.dump(courses))





