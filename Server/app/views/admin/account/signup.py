from binascii import hexlify
from hashlib import pbkdf2_hmac

from flask import Blueprint, Response, current_app
from flask_restful import Api, request
from flasgger import swag_from

from app.docs.admin.account.signup import *
from app.models.account import StudentModel, AdminModel
from app.views import BaseResource, admin_only, json_required

api = Api(Blueprint('admin-signup-api', __name__))
api.prefix = '/admin'


@api.resource('/new-account')
class NewAccount(BaseResource):
    @swag_from(NEW_ACCOUNT_POST)
    @json_required
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