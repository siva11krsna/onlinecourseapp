from flask_restx import Resource, Api, Namespace, fields
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy

from ..models.course import *

from app import app
from app import db

api = Api(app)
# ns = api.namespace('courses','course list')

coursemodel = CourseModel()
courseschema = CourseSchema(many=True)

@api.route('/courses')
class Course(Resource):
    def get(self):
        courses = coursemodel.query.all()
        return jsonify(courseschema.dump(courses))

    def post(self):
        course_data = request.get_json()
        course_new = CourseModel(**course_data)
        db.session.add(course_new)
        db.session.commit()
        course_data['id']=str(course_new.id)
        return course_data






