from flask import Blueprint, Response
from flask_restful import Api, request
from flasgger import swag_from

from app.docs.admin.point.rule import *
from app.models.point import PointRuleModel
from app.views import BaseResource, admin_only, json_required

api = Api(Blueprint('admin-point-rule-api', __name__))
api.prefix = '/admin/managing'


@api.resource('/rule')
class PointRuleManaging(BaseResource):
    @swag_from(POINT_RULE_MANAGING_GET)
    @admin_only
    def get(self):
        """
        상벌점 규칙 목록 조회
        """
        response = [{
            'id': str(rule.id),
            'name': rule.name,
            'minPoint': rule.min_point,
            'maxPoint': rule.max_point
        } for rule in PointRuleModel.objects]

        return self.unicode_safe_json_response(response)

    @swag_from(POINT_RULE_MANAGING_POST)
    @json_required('name', 'minPoint', 'maxPoint')
    @admin_only
    def post(self):
        """
        상벌점 규칙 추가
        """
        name = request.json['name']
        min_point = request.json['minPoint']
        max_point = request.json['maxPoint']

        rule = PointRuleModel(
            name=name,
            min_point=min_point,
            max_point=max_point
        ).save()

        return {
            'id': str(rule.id)
        }, 201

    @swag_from(POINT_RULE_MANAGING_PATCH)
    @json_required('ruleId', 'name', 'minPoint', 'maxPoint')
    @admin_only
    def patch(self):
        """
        상벌점 규칙 수정
        """
        rule_id = request.json['ruleId']
        if len(rule_id) != 24:
            return Response('', 204)

        rule = PointRuleModel.objects(id=rule_id).first()
        if not rule:
            return Response('', 204)

        name = request.json['name']
        min_point = request.json['minPoint']
        max_point = request.json['maxPoint']

        rule.update(
            name=name,
            min_point=min_point,
            max_point=max_point
        )

        return Response('', 200)

    @swag_from(POINT_RULE_MANAGING_DELETE)
    @json_required('ruleId')
    @admin_only
    def delete(self):
        """
        상벌점 규칙 삭제
        """
        rule_id = request.json['ruleId']
        if len(rule_id) != 24:
            return Response('', 204)

        rule = PointRuleModel.objects(id=rule_id).first()
        if not rule:
            return Response('', 204)

        rule.delete()

        return Response('', 200)
