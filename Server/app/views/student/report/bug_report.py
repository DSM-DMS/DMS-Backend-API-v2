from flask import Blueprint
from flask_jwt_extended import get_jwt_identity
from flask_restful import Api, request
from flasgger import swag_from

from app.docs.student.report.bug_report import *
from app.models.account import StudentModel
from app.models.report import BugReportModel
from app.views import BaseResource, json_required, student_only

api = Api(Blueprint('student-bug-report-api', __name__))


@api.resource('/report/bug')
class BugReport(BaseResource):
    @swag_from(BUG_REPORT_POST)
    @json_required
    @student_only
    def post(self):
        """
        버그 신고
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()

        title = request.json['title']
        content = request.json['content']

        report = BugReportModel(author=student.name, title=title, content=content).save()

        return self.unicode_safe_json_response({
            'id': str(report.id)
        }, 201)
