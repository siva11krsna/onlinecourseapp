from flask_restx import Resource, Api, Namespace, fields
from flask import jsonify, request, make_response


from ..models.course import *

from app import app
from app import db
from ..library import util

api = Api(app)
# ns = api.namespace('/courses/','course apis')

coursemodel = CourseModel()
courseschema = CourseSchema()
courses_schema = CourseSchema(many=True)


@api.route('/courses')
class Course(Resource):
    def get(self):
        courses = coursemodel.query.all()
        return jsonify(courses_schema.dump(courses))

    def post(self):
        course_data = request.get_json()
        course_new = CourseModel(**course_data)
        db.session.add(course_new)
        db.session.commit()
        course_data['id']=str(course_new.id)
        return course_data


@api.route('/courses/<uuid:id>')
@api.param('id', 'course identifier')
class CourseById(Resource):
    def put(self,id):
        course_update = coursemodel.query.get(id)
        util.validate_request(request, courseschema)
        util.merge_request_with_model(course_update, request, courseschema)
        db.session.merge(course_update)
        db.session.commit()
        return courseschema.dump(course_update)






