from flask import Blueprint
from flask_jwt_extended import get_jwt_identity
from flask_restful import Api, abort, request
from flasgger import swag_from

from app.docs.student.report.facility_report import *
from app.models.account import StudentModel
from app.models.report import FacilityReportModel
from app.views import BaseResource, json_required, student_only

api = Api(Blueprint('student-facility-report-api', __name__))


@api.resource('/report/facility')
class FacilityReport(BaseResource):
    @swag_from(FACILITY_REPORT_POST)
    @json_required('title', 'content', 'room')
    @student_only
    def post(self):
        """
        시설고장 신고
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()

        title = request.json['title']
        content = request.json['content']
        room = request.json['room']

        if not 200 < room < 519:
            abort(400)

        report = FacilityReportModel(author=student.name, title=title, content=content, room=room).save()

        return self.unicode_safe_json_response({
            'id': str(report.id)
        }, 201)
