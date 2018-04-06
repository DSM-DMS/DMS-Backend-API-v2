from app.models import *
from app.models.account import StudentModel


class SurveyModel(Document):
    """
    Survey information document
    """
    meta = {
        'collection': 'survey'
    }

    creation_time = DateTimeField(
        required=True
    )

    title = StringField(
        required=True
    )

    description = StringField(
        required=True
    )

    start_date = DateTimeField(
        required=True
    )
    end_date = DateTimeField(
        required=True
    )

    target = ListField(
        IntField()
    )

    questions = ListField(
        ReferenceField(
            document_type=QuestionModel
        )
    )

    answers = ListField(
        ReferenceField(
            document_type=AnswerModel
        )
    )


class QuestionModel(Document):
    """
    Each questions in a survey document
    """

    meta = {
        'collection': 'survey_question'
    }

    title = StringField(
        required=True
    )
    is_objective = BooleanField(
        required=True
    )
    choice_paper = ListField()


class AnswerModel(Document):
    """
    Answer data for each question document
    """

    meta = {
        'collection': 'survey_answer'
    }

    answer_student = ReferenceField(
        document_type=StudentModel,
        required=True,
        reverse_delete_rule=CASCADE
    )
    content = StringField(
        required=True
    )
