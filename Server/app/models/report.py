from app.models import *


class ReportBase(Document):
    """
    Report document base
    """
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    report_time = DateTimeField(
        required=True
    )

    author = StringField(
        required=True
    )

    content = StringField(
        required=True
    )


class BugReportModel(ReportBase):
    """
    Bug report document
    
    platform
    1 : Web
    2 : Android
    3 : IOS
    """
    meta = {
        'collection': 'report_bug'
    }

    platform = IntField(
        required=True,
        min_value=1,
        max_value=3
    )


class FacilityReportModel(ReportBase):
    """
    Facility report document
    """
    meta = {
        'collection': 'report_facility'
    }

    room = IntField(
        required=True,
        min_value=200,
        max_value=519
    )
