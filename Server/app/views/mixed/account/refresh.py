from flask import Blueprint, Response
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity, jwt_refresh_token_required
from flask_restful import Api
from flasgger import swag_from

from app.docs.mixed.account.refresh import *
from app.models.account import RefreshTokenModel
from app.views import BaseResource

api = Api(Blueprint('mixed-refresh-api', __name__))


@api.resource('/refresh')
class Refresh(BaseResource):
    @swag_from(REFRESH_POST)
    @jwt_refresh_token_required
    def post(self):
        """
        새로운 Access Token 획득
        """
        token = RefreshTokenModel.objects(token=get_jwt_identity()).first()

        if not token or token.token_owner.pw != token.pw_snapshot:
            # Invalid token or the token issuing password is different from the current password
            # Returns status code 205 : Reset Content
            return Response('', 205)

        return {
            'accessToken': create_access_token(token.token_owner.id)
        }, 200
