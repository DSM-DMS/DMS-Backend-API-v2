from binascii import hexlify
from hashlib import pbkdf2_hmac
from uuid import uuid4

from flask import Blueprint, current_app
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Api, abort, request
from flasgger import swag_from

from app.docs.admin.account.auth import *
from app.models.account import AdminModel, RefreshTokenModel
from app.views import BaseResource, json_required

api = Api(Blueprint('admin-auth-api', __name__))
api.prefix = '/admin'


@api.resource('/auth')
class Auth(BaseResource):
    @swag_from(AUTH_POST)
    @json_required
    def post(self):
        """
        관리자 로그인
        """
        id = request.json['id']
        pw = request.json['pw']

        hashed_pw = hexlify(pbkdf2_hmac(
            hash_name='sha256',
            password=pw.encode(),
            salt=current_app.secret_key.encode(),
            iterations=100000
        )).decode('utf-8')
        # pbkdf2_hmac hash with salt(secret key) and 100000 iteration

        admin = AdminModel.objects(id=id, pw=hashed_pw).first()

        if not admin:
            abort(401)

        # --- Auth success

        refresh_token = uuid4()
        RefreshTokenModel(
            token=refresh_token,
            token_owner=admin,
            pw_snapshot=hashed_pw
        ).save()
        # Generate new refresh token made up of uuid4

        return {
            'accessToken': create_access_token(id),
            'refreshToken': create_refresh_token(str(refresh_token))
        }, 200
