from app.models import *


class VersionModel(Document):
    """
    Application newest version document
    
    platform
    1 : Web
    2 : Android
    3 : IOS
    """
    meta = {
        'collection': 'version'
    }

    platform = IntField(
        required=True,
        min_value=1,
        max_value=3
    )

    version = StringField(
        required=True
    )
