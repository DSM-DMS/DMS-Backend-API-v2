from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity
from flask_restful import Api, request
from flasgger import swag_from

from app.docs.student.survey.survey import *
from app.models.account import StudentModel
from app.models.survey import AnswerModel, QuestionModel, SurveyModel
from app.views import BaseResource, json_required, student_only

api = Api(Blueprint('student-survey-api', __name__))


@api.resource('/survey')
class Survey(BaseResource):
    @swag_from(SURVEY_GET)
    @student_only
    def get(self):
        """
        설문지 리스트 조회
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()

        student_number = student.number

        response = [{
            'id': str(survey.id),
            'creationTime': str(survey.creation_time)[:10],
            'description': survey.description,
            'title': survey.title,
            'startDate': str(survey.start_date)[:10],
            'endDate': str(survey.end_date)[:10]
        } for survey in SurveyModel.objects if int(student_number / 1000) in survey.target]

        return self.unicode_safe_json_response(response)
        # Filter by student number


@api.resource('/survey/question')
class Question(BaseResource):
    @swag_from(QUESTION_GET)
    @student_only
    def get(self):
        """
        설문지의 질문 리스트 조회
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()

        survey_id = request.args['surveyId']
        if len(survey_id) != 24:
            return Response('', 204)

        survey = SurveyModel.objects(id=survey_id).first()
        if not survey:
            return Response('', 204)

        response = [{
            'id': str(question.id),
            'title': question.title,
            'isObjective': question.is_objective,
            'choicePaper': question.choice_paper if question.is_objective else None
        } for question in QuestionModel.objects(survey=survey)]

        for question in response:
            answer = AnswerModel.objects(
                question=QuestionModel.objects(id=question['id']).first(),
                answer_student=student
            ).first()

            if answer:
                question['answer'] = answer.content
            else:
                question['answer'] = None

        return self.unicode_safe_json_response(response)

    @swag_from(QUESTION_POST)
    @json_required('questionId', 'answer')
    @student_only
    def post(self):
        """
        설문지 질문의 답변 업로드
        """
        student = StudentModel.objects(id=get_jwt_identity()).first()

        question_id = request.json['questionId']
        if len(question_id) != 24:
            return Response('', 204)

        question = QuestionModel.objects(id=question_id).first()
        if not question:
            # Question doesn't exist
            return Response('', 204)

        answer = request.json['answer']

        AnswerModel.objects(question=question, answer_student=student).delete()
        # Delete existing document

        AnswerModel(question=question, answer_student=student, content=answer).save()
        # Insert new answer data

        return Response('', 201)
