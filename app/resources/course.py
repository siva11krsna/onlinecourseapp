from flask_restx import Resource, Api, Namespace, fields
from flask import jsonify, request

from ..schemas import course as courseschema
from ..models import course as course
from app import app

api = Api(app)
courses = courseschema(many=True)


class Course:

    @app.route('/courses')
    def getCourses(self):
        courses = course.query.all()
        return jsonify(courseschema.dump(courses))





