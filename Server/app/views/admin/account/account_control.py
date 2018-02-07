from uuid import uuid4

from flask import Blueprint, Response
from flask_restful import Api, request
from flasgger import swag_from

from app.docs.admin.account.account_control import *
from app.models.account import SignupWaitingModel, StudentModel, AdminModel
from app.views import BaseResource, admin_only, json_required

api = Api(Blueprint('admin-account-control-api', __name__))
api.prefix = '/admin'


@api.resource('/account-control')
class AccountControl(BaseResource):
    @swag_from(ACCOUNT_CONTROL_POST)
    @json_required
    @admin_only
    def post(self):
        """
        학생 계정 제거 후 새로운 UUID 생성
        """
        number = request.json['number']

        signup_waiting = StudentModel.objects(number=number).first()
        if signup_waiting:
            return Response('', 205)

        student = StudentModel.objects(number=number).first()
        if not student:
            return Response('', 204)

        name = student.name
        student.delete()

        while True:
            uuid = str(uuid4())[:4]

            if not SignupWaitingModel.objects(uuid=uuid):
                SignupWaitingModel(
                    uuid=uuid,
                    name=name,
                    number=number
                ).save()

                break

        return {
            'uuid': uuid
        }, 201

    @swag_from(ACCOUNT_CONTROL_DELETE)
    @json_required
    @admin_only
    def delete(self):
        """
        관리자 계정 삭제 
        """
        id = request.json['id']

        admin = AdminModel.objects(id=id).first()
        if not admin:
            return Response('', 204)

        admin.delete()
        return Response('', 200)
