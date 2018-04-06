from app.models import *


class ApplyBase(EmbeddedDocument):
    """
    Apply data of student base document
    """
    meta = {
        'allow_inheritance': True,
        'abstract': True
    }

    apply_date = DateTimeField(
        required=True
    )


class ExtensionApplyModel(ApplyBase):
    """
    Extension apply data of student document includes 11st, 12nd extension apply
    """
    meta = {
        'collection': 'apply_extension'
    }

    class_ = IntField(
        required=True
    )
    seat = IntField(
        required=True
    )


class GoingoutApplyModel(ApplyBase):
    """
    Goingout apply data of student document
    """
    meta = {
        'collection': 'apply_goingout'
    }

    on_saturday = BooleanField(
        required=True,
        default=False
    )
    on_sunday = BooleanField(
        required=True,
        default=False
    )


class StayApplyModel(ApplyBase):
    """
    Stay apply data of student document
    1 : Friday homecoming
    2 : Saturday homecoming
    3 : Saturday dormitory coming
    4 : Stay
    """
    meta = {
        'collection': 'apply_stay'
    }
    value = IntField(
        required=True,
        default=4
    )
