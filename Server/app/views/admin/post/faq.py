from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity
from flask_restful import Api, request
from flasgger import swag_from

from app.docs.admin.post.faq import *
from app.models.account import AdminModel
from app.models.post import FAQModel
from app.views import BaseResource, admin_only, json_required

api = Api(Blueprint('admin-faq-api', __name__))
api.prefix = '/admin'


@api.resource('/faq')
class FAQManaging(BaseResource):
    @swag_from(FAQ_MANAGING_POST)
    @json_required
    @admin_only
    def post(self):
        """
        FAQ 업로드
        """
        title = request.json['title']
        content = request.json['content']

        admin = AdminModel.objects(id=get_jwt_identity()).first()
        faq = FAQModel(author=admin.name, title=title, content=content).save()

        return self.unicode_safe_json_response({
            'id': str(faq.id)
        }, 201)

    @swag_from(FAQ_MANAGING_PATCH)
    @json_required
    @admin_only
    def patch(self):
        """
        FAQ 수정
        """
        id = request.json['id']
        title = request.json['title']
        content = request.json['content']

        if len(id) != 24:
            return Response('', 204)

        faq = FAQModel.objects(id=id).first()
        if not faq:
            return Response('', 204)

        faq.update(title=title, content=content)

        return Response('', 200)

    @swag_from(FAQ_MANAGING_DELETE)
    @json_required
    @admin_only
    def delete(self):
        """
        FAQ 제거
        """
        id = request.json['id']

        if len(id) != 24:
            return Response('', 204)

        faq = FAQModel.objects(id=id).first()
        if not faq:
            return Response('', 204)

        faq.delete()

        return Response('', 200)
