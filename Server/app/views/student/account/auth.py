from binascii import hexlify
from hashlib import pbkdf2_hmac
from uuid import uuid4

from flask import Blueprint, Response, current_app
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Api, abort, request
from flasgger import swag_from

from app.docs.student.account.auth import *
from app.models.account import StudentModel, RefreshTokenModel
from app.views import BaseResource, json_required, student_only

api = Api(Blueprint('student-auth-api', __name__))


@api.resource('/auth')
class Auth(BaseResource):
    @swag_from(AUTH_POST)
    @json_required
    def post(self):
        """
        학생 로그인
        """
        id = request.json['id']
        pw = request.json['pw']

        pw = hexlify(pbkdf2_hmac(
            hash_name='sha256',
            password=pw.encode(),
            salt=current_app.secret_key.encode(),
            iterations=100000
        )).decode('utf-8')
        # pbkdf2_hmac hash with salt(secret key) and 100000 iteration

        student = StudentModel.objects(id=id, pw=pw).first()

        if not student:
            student = StudentModel.objects(id=id).first()
            if not student:
                abort(401)
            else:
                # 비밀번호 암호화가 어떤 key로 salting되었는지 모르므로 id만 같다면 일단 pass시켜 줌
                # 새롭게 암호화된 비밀번호로 업데이트
                # TODO 비밀번호 암호화 관련 이슈를 해결하기 위한 것이므로 추후 제거해야 함
                student.update(pw=pw)

        # --- Auth success

        refresh_token = uuid4()
        RefreshTokenModel(
            token=refresh_token,
            token_owner=student,
            pw_snapshot=pw
        ).save()
        # Generate new refresh token made up of uuid4

        return self.unicode_safe_json_response({
            'accessToken': create_access_token(id),
            'refreshToken': create_refresh_token(str(refresh_token))
        }, 200)


@api.resource('/auth-check')
class AuthCheck(BaseResource):
    @swag_from(AUTH_CHECK_GET)
    @student_only
    def get(self):
        """
        로그인 상태(Access Token 만료 여부) 체크
        """
        return Response('', 200)
