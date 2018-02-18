from binascii import hexlify
from hashlib import pbkdf2_hmac
from uuid import uuid4

from flask import Blueprint, Response
from flask_restful import Api, current_app, request
from flasgger import swag_from

from app.docs.admin.account.account_control import *
from app.models.account import SignupWaitingModel, StudentModel, AdminModel
from app.views import BaseResource, admin_only, json_required

api = Api(Blueprint('admin-account-control-api', __name__))
api.prefix = '/admin'


@api.resource('/account-control/student')
class StudentAccountControl(BaseResource):
    @swag_from(STUDENT_ACCOUNT_CONTROL_DELETE)
    @json_required('number')
    @admin_only
    def delete(self):
        """
        학생 계정 제거 후 새로운 UUID 생성
        """
        number = request.json['number']

        signup_waiting = SignupWaitingModel.objects(number=number).first()
        if signup_waiting:
            return {
                'uuid': signup_waiting.uuid
            }, 200

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


@api.resource('/account-control/admin')
class AdminAccountControl(BaseResource):
    @swag_from(ADMIN_ACCOUNT_CONTROL_POST)
    @json_required('id', 'pw', 'name')
    @admin_only
    def post(self):
        """
        새로운 관리자 계정 생성
        """
        id = request.json['id']
        pw = request.json['pw']
        name = request.json['name']

        student = StudentModel.objects(id=id).first()
        admin = AdminModel.objects(id=id).first()
        if any((student, admin)):
            return Response('', 204)

        # --- Create new admin account

        hashed_pw = hexlify(pbkdf2_hmac(
            hash_name='sha256',
            password=pw.encode(),
            salt=current_app.secret_key.encode(),
            iterations=100000
        )).decode('utf-8')
        # pbkdf2_hmac hash with salt(secret key) and 100000 iteration

        AdminModel(id=id, pw=hashed_pw, name=name).save()

        return Response('', 201)

    @swag_from(ADMIN_ACCOUNT_CONTROL_DELETE)
    @json_required('id')
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
